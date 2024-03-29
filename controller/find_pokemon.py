import logging
import os
import re
from typing import Any, Dict, List, Union

import requests
from bs4 import BeautifulSoup
from linebot.models import FlexSendMessage, TextSendMessage

from utils import sqlite
from utils.flex import skill_list, specific_flex
from utils.language import Language
from utils.pikalytics import Pikalytics
from utils.poke_crawler import (
    arrange_text,
    find_pokemon_image,
    pokemon_wiki,
)

logger = logging.getLogger(__file__)


def find_specific_pokemon_all_status(pokemon_name: str = "Roaring Moon") -> List[Dict[str, Any]]:
    series_search_name: str = pokemon_name
    # Force to change name to %20 (e.g. Roaring Moon)
    if re.findall("\w+\s+\w+", pokemon_name):
        poke_split: List[str] = series_search_name.split(' ')
        series_search_name = f'{poke_split[0]}%20{poke_split[1]}'.lower()
    series: str = os.getenv('SERIES')
    url: str = f"https://www.pikalytics.com/pokedex/{series}/{series_search_name}"
    logger.debug('Pokemon series web crawler query: ' + url)

    rs: requests.Response = requests.get(url=url)
    specific_soup: BeautifulSoup = BeautifulSoup(rs.text, "html.parser")
    details: List[BeautifulSoup] = specific_soup.select(
        '.pokedex-category-wrapper')
    logger.debug(pokemon_name+' record start...')

    if len(details) == 0:
        logger.info(pokemon_name+' is not in this series.')
        return [{
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": f"賽季 {series} 沒有 {pokemon_name} 出場紀錄..",
                        "weight": "bold",
                        "size": "md",
                        "wrap": True
                    }
                ]
            }
        }]
    else:
        contents: List[Dict[str, Any]] = []
        # 或許可以把對應 API 都放在 mapping 裏面
        for index in range(1, len(details)):
            s: List[BeautifulSoup] = details[index].select(
                '.pokedex-move-entry-new')
            item: str = ''
            items: List[str] = []
            # 整理爬蟲下來各個清單對應的陣列
            for entry_idx in range(0, len(s)):
                if index == 5 and entry_idx == 5:
                    break

                item = arrange_text(s[entry_idx].text)
                if item[0] == 'Other':
                    break
                items.append(item)

            pika: Pikalytics = Pikalytics(index=index, url=url)
            pika.poke_mapping(items)

            logger.debug('Pokemon all body status: ' + str(pika.template))

            # 輸出成 Flex，若 API 有圖片可能需要另外處理
            contents.append(skill_list(
                name=pika.template['name'],
                abilities=pika.template['abilities'],
                url=url))
        logger.debug('Ready to generate FlexMessage...')
        return contents


def search_specific_pokemon_by_wiki(pokemon_name: str = '快龍') -> Union[FlexSendMessage, TextSendMessage]:
    # If found, return SQL data.
    # If not, return None.

    language = Language(pokemon_name)
    name_location, _ = language.match()
    pokemon_row_list: List[Dict[str, str]] = pokemon_wiki(
        pokemon_name=pokemon_name, language=name_location)

    if pokemon_row_list and len(pokemon_row_list) > 0:
        eng_name, poke_img = find_pokemon_image(pokemon_row_list)
        logger.debug(f'Pokemon image url" {poke_img}')
        try:
            with sqlite.connect() as con:
                poke_query: Dict[str, str] = sqlite.exec_one(
                    con,
                    f"SELECT idx, name_zh FROM t_pokemon WHERE name_en = '{eng_name}'")
                logger.info(
                    f"Specific Pokemon query from sqlite: {poke_query}")
                poke_detail: Dict[str, Union[int, str]] = sqlite.exec_one(
                    con,
                    f"SELECT * FROM t_pokemon_detail_base_stat WHERE idx = '{poke_query.get('idx')}'"
                )
                logger.info(f"The Pokemon status is: {poke_detail}")

            # zh_name, _ = find_pokemon_name(eng_name)
            response_flex: Dict[str, Any] = specific_flex(
                image=poke_img, name=[pokemon_name, eng_name], body=poke_detail)
            return FlexSendMessage(alt_text=eng_name, contents=response_flex)
        except:
            logger.info(f'{pokemon_name} not in SQL')
            return None
    else:
        logger.info(f"Keyword {pokemon_name} not found.")
        return None
