import logging
import os
from typing import List, Optional
import requests
import re
from bs4 import BeautifulSoup
from controller.find_pokemon import find_specific_pokemon_all_status, search_specific_pokemon_by_wiki
from utils import sqlite
from fastapi import APIRouter, HTTPException, Header, Request
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import TextMessage, MessageEvent, FlexSendMessage, TextSendMessage, ImageSendMessage
from pydantic import BaseModel

from utils.flex import skill_list, specific_flex
from utils.poke_crawler import find_pokemon_image, pokemon_wiki, find_pokemon_name

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
    elif re.findall("^find\s+.*", message):
        message = message.split(' ')[1].lower()
        response = find_specific_pokemon_all_status(pokemon_name=message)
    else:
        response = search_specific_pokemon_by_wiki(pokemon_name=message)
    line_bot_api.reply_message(
        event.reply_token,
        response
    )
