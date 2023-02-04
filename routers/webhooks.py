import logging
import os
from typing import List, Optional
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

from utils.poke_crawler import find_pokemon_name

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
def message_text(event):
    message = event.message.text
    logger.debug('LINE Bot reply message is: '+message)
    if message == '屬性':
        image_url = 'https://raw.githubusercontent.com/louis70109/find-your-pokemon/main/pokemon.jpg'
        response = ImageSendMessage(image_url, image_url)
    elif message == 'TOP':
        url = "https://www.pikalytics.com/pokedex/"
        r = requests.get(url=url)
        soup = BeautifulSoup(r.text, "html.parser")
        all_rank = soup.select('span.pokemon-name')
        all_trending = soup.select('.float-right.margin-right-20')

        trending = []
        for i in range(len(all_rank)):
            en_name = all_rank[i].text.rstrip()
            trend_percent = all_trending[i].text.rstrip()
            trending.append([en_name, trend_percent])

        response = FlexSendMessage(
            alt_text='賽季排行榜', contents=top_list('排行榜', trending))
    elif message == 'Heal':
        # Healthy check by reply message
        res = requests.get(os.getenv('HEAL_URL'))
        response = TextSendMessage(str(res.json()))
    elif re.findall("^find\s*.*\s*.*", message):
        msg_split = message.split(' ')
        message = msg_split[1].lower() if len(
            msg_split) == 1 else f'{msg_split[1]} {msg_split[2]}'.lower()
        contents: list = find_specific_pokemon_all_status(pokemon_name=message)
        response = FlexSendMessage(alt_text=message, contents={
            "type": "carousel",
            "contents": contents
        })
    else:
        response = search_specific_pokemon_by_wiki(pokemon_name=message)
    line_bot_api.reply_message(
        event.reply_token,
        response
    )
