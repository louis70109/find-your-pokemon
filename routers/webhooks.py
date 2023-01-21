import os
from typing import List, Optional
import requests

from fastapi import APIRouter, HTTPException, Header, Request
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import TextMessage, MessageEvent, FlexSendMessage, TextSendMessage
from pydantic import BaseModel

from utils.flex import specific_flex
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


@handler.add(MessageEvent, message=TextMessage)
def message_text(event):
    message = event.message.text
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
        response = FlexSendMessage(alt_text=eng_name, contents=response_flex)
    else:
        print('找不到')
        response = TextSendMessage('找不到')

    line_bot_api.reply_message(
        event.reply_token,
        response
    )
