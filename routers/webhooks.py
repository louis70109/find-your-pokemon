import logging
import os
from typing import List, Optional, Union
import re
import requests
from controller.find_pokemon import find_specific_pokemon_all_status, search_specific_pokemon_by_wiki
from fastapi import APIRouter, HTTPException, Header, Request
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import TextMessage, MessageEvent, ImageSendMessage, TextSendMessage, FlexSendMessage
from pydantic import BaseModel
from bs4 import BeautifulSoup
from utils.flex import top_list
from utils.openai import generate_random_image


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


@handler.add(MessageEvent, message=TextMessage)
def message_text(event: MessageEvent) -> None:
    message: str = event.message.text
    logger.debug(f'LINE Bot reply message is: {message}')

    if message == '屬性':
        image_url: str = 'https://raw.githubusercontent.com/louis70109/find-your-pokemon/main/pokemon.jpg'
        response: ImageSendMessage = ImageSendMessage(image_url, image_url)

    elif message.lower() == 'vgc':
        url: str = 'https://docs.google.com/spreadsheets/d/1axlwmzPA49rYkqXh7zHvAtSP-TKbM0ijGYBPRflLSWw/edit#gid=313573250'
        response: TextSendMessage = TextSendMessage(url)

    elif message.lower() == 'top':
        url: str = 'https://www.pikalytics.com/pokedex/'
        response: FlexSendMessage = get_pokemon_trending(url)

    elif message.lower() == 'heal':
        # Health check
        response: TextSendMessage = check_health()

    elif re.findall('^find\s*.*\s*.*', message):
        response: FlexSendMessage = get_pokemon_status(message)
    else:
        response: TextSendMessage = search_pokemon_wiki(message)

    logger.debug(f'LINE bot response JSON: {str(response)}')
    line_bot_api.reply_message(event.reply_token, response)


def get_pokemon_trending(url: str) -> FlexSendMessage:
    try:
        r: requests.Response = requests.get(url=url)
        soup: BeautifulSoup = BeautifulSoup(r.text, 'html.parser')
        all_rank: List[BeautifulSoup] = soup.select('span.pokemon-name')
        all_trending: List[BeautifulSoup] = soup.select(
            '.float-right.margin-right-20')

        trending: List[List[str]] = []
        for i in range(len(all_rank)):
            en_name: str = all_rank[i].text.rstrip()
            trend_percent: str = all_trending[i].text.rstrip()
            trending.append([en_name, trend_percent])

        return FlexSendMessage(alt_text='賽季排行榜', contents=top_list('排行榜', trending))
    except Exception as e:
        logger.warning(f'Get pokemon trending fails, see exception: {e}')
        return TextSendMessage(text=f'想看更多趨勢？\n請看 {url}')


def check_health() -> TextSendMessage:
    # Health check by reply message
    res: requests.Response = requests.get(os.getenv('HEAL_URL'))
    return TextSendMessage(str(res.json()))


def get_pokemon_status(message: str) -> Union[FlexSendMessage, TextSendMessage]:
    msg_split: List[str] = message.split(' ')
    name: str = msg_split[1].lower()
    if len(msg_split) == 3:
        name: str = f'{msg_split[1]} {msg_split[2]}'.lower()
    try:
        contents: list = find_specific_pokemon_all_status(pokemon_name=name)
        return FlexSendMessage(alt_text=name, contents={"type": "carousel", "contents": contents})
    except Exception as e:
        logger.error(f'Could not find specific pokemon status, see error: {e}')
        return TextSendMessage('查無此寶可夢特性')


def search_pokemon_wiki(pokemon_name: str) -> TextSendMessage:
    pokemon = search_specific_pokemon_by_wiki(pokemon_name)
    if pokemon is None:
        try:
            image_url = generate_random_image(pokemon=pokemon_name)
            pokemon = ImageSendMessage(image_url, image_url)
        except Exception as e:
            logger.warning('Maybe OpenAI budget not enough.')
            logger.info(e)
            return """
                - `heal`: 健康檢查
                - `top`: 尋找最多人雙打使用的寶可夢
                - `vgc`: 尋找組隊資訊
                - `皮卡丘`: 手動輸入想找的寶可夢名字，尋找個體值
                - `屬性`: 屬性剋制表
                - `find pikachu`: 尋找對戰細節
            """

    return pokemon
