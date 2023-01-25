import logging
import os
from typing import List, Optional
import requests
import re
from bs4 import BeautifulSoup
from utils import sqlite
from fastapi import APIRouter, HTTPException, Header, Request
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import TextMessage, MessageEvent, FlexSendMessage, TextSendMessage
from pydantic import BaseModel

from utils.flex import skill_list, specific_flex
from utils.poke_crawler import find_pokemon_image, pokemon_wiki

line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(os.getenv('LINE_CHANNEL_SECRET'))

logger = logging.getLogger(__file__)

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
        logger.info('=====技能=====')
        skills = specific_soup.select('.pokedex-category-wrapper')
        contents = []
        logger.info(message+' 相關戰績')
        # 或許可以把對應 API 都放在 mapping 裏面
        pikalytic_mapping = {1: '招式', 2: '隊友', 3: '物品', 4: '特性', 5: '努力值'}
        for index in range(1, len(skills)-1):
            s = skills[index].select('.pokedex-move-entry-new')
            item, items = '', []
            logger.info(f'搜尋 {pikalytic_mapping[index]}')
            # 整理爬蟲下來各個清單對應的陣列
            for entry_idx in range(0, len(s)-1):
                item = arrange_text(s[entry_idx].text)
                items.append(item)
            if index == 1:
                with sqlite.connect() as con:
                    for it in items:
                        item_query = sqlite.exec_one(con, 
                        f"SELECT name_zh, category FROM t_move WHERE name_en == '{it[0]}'")
                        it[0] = item_query[0]
                        it[1] = item_query[1]
                logger.info('Move query result: '+ str(items))
            if index == 3:
                # 針對物品欄把 request 拉出來寫在放入函式
                # 若之後重複可單獨在包裝
                with sqlite.connect() as con:
                    for it in items:
                        item_query = sqlite.exec_one(con, 
                        f"SELECT name_zh, img_url FROM t_item WHERE name_en == '{it[0]}'")
                        logger.info('Item query: '+str(item_query))
                        it[0] = item_query[0]
                logger.info('Item query result: '+ str(items))
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
            logger.info(poke_img)
            logger.info('The Pokemon status is:')

            showdown = requests.get(
                'https://play.pokemonshowdown.com/data/pokedex.json')
            pokemon_dict = showdown.json()[eng_name.replace(' ', '').lower()]
            logger.info(pokemon_dict)

            response_flex = specific_flex(
                image=poke_img, name=pokemon_dict['name'], body=pokemon_dict['baseStats'])
            response = FlexSendMessage(
                alt_text=eng_name, contents=response_flex)
        else:
            logger.info('關鍵字找不到' + message)
            response = TextSendMessage('找不到'+message)

    line_bot_api.reply_message(
        event.reply_token,
        response
    )
