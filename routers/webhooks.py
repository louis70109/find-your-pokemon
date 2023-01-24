import os
from typing import List, Optional
import requests
import re
from bs4 import BeautifulSoup

from fastapi import APIRouter, HTTPException, Header, Request
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import TextMessage, MessageEvent, FlexSendMessage, TextSendMessage
from pydantic import BaseModel
from utils.commons import find_CN_by_EN_name

from utils.flex import skill_list, specific_flex
from utils.poke_crawler import find_pokemon_image, pokemon_wiki

line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(os.getenv('LINE_CHANNEL_SECRET'))

router = APIRouter(
    prefix="/webhooks",
    tags=["chatbot"],
    responses={404: {"description": "Not found"}},
)


class Line(BaseModel):
    destination: str
    events: List[Optional[None]]


@router.post("/line")
async def callback(request: Request, x_line_signature: str = Header(None)):
    body = await request.body()
    try:
        handler.handle(body.decode("utf-8"), x_line_signature)
    except InvalidSignatureError:
        raise HTTPException(
            status_code=400, detail="chatbot handle body error.")
    return 'OK'


def arrange_text(text: str):
    return list(filter(None, text.rstrip().split('\n')))


@handler.add(MessageEvent, message=TextMessage)
def message_text(event):
    message = event.message.text

    if re.findall("^find\s+.*", message):
        message = message.split(' ')[1].lower()
        series = os.getenv('SERIES')
        url = "https://www.pikalytics.com/pokedex/"+series+'/'+message
        rs = requests.get(url=url)
        specific_soup = BeautifulSoup(rs.text, "html.parser")
        print('=====技能=====')
        skills = specific_soup.select('.pokedex-category-wrapper')
        contents = []
        print(message+'戰績------')
        # 或許可以把對應 API 都放在 mapping 裏面
        pikalytic_mapping = {1: '招式', 2: '隊友', 3: '物品', 4: '特性', 5: '努力值'}
        for index in range(1, len(skills)-1):
            s = skills[index].select('.pokedex-move-entry-new')
            item, items = '', []
            print(f'搜尋 {pikalytic_mapping[index]}')
            # 整理爬蟲下來各個清單對應的陣列
            for entry_idx in range(0, len(s)-1):
                item = arrange_text(s[entry_idx].text)
                items.append(item)
            if index == 3:
                # 針對物品欄把 request 拉出來寫在放入函式
                # 若之後重複可單獨在包裝
                it_req = requests.get('https://pokemon.fantasticmao.cn/item/list').json()
                for it in items:
                    CN_name = find_CN_by_EN_name(it_req, it[0])
                    it[0] = CN_name['nameZh']
            # 輸出成 Flex，若 API 有圖片可能需要另外處理
            contents.append(skill_list(
                name=pikalytic_mapping[index], abilities=items, url=url))
        response = FlexSendMessage(alt_text=message, contents={
            "type": "carousel",
            "contents": contents
        })
    else:
        pokemon_row_list = pokemon_wiki(message)

        if pokemon_row_list is not None and len(pokemon_row_list) > 0:
            eng_name, poke_img = find_pokemon_image(pokemon_row_list)
            print(poke_img)
            print('The Pokemon status is:')

            showdown = requests.get(
                'https://play.pokemonshowdown.com/data/pokedex.json')
            pokemon_dict = showdown.json()[eng_name.replace(' ', '').lower()]
            print(pokemon_dict)

            response_flex = specific_flex(
                image=poke_img, name=pokemon_dict['name'], body=pokemon_dict['baseStats'])
            response = FlexSendMessage(
                alt_text=eng_name, contents=response_flex)
        else:
            print('找不到')
            response = TextSendMessage('找不到')

    line_bot_api.reply_message(
        event.reply_token,
        response
    )
