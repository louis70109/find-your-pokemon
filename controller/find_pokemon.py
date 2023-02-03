import logging
import os, re
import requests
from bs4 import BeautifulSoup
from utils import sqlite

from linebot.models import FlexSendMessage, TextSendMessage
from utils.flex import skill_list, specific_flex
from utils.poke_crawler import arrange_text, find_pokemon_image, pokemon_wiki, find_pokemon_name


logger = logging.getLogger(__file__)


def find_specific_pokemon_all_status(pokemon_name="Roaring Moon"):

    series_search_name = pokemon_name
    # Force to change name to %20 (e.g. Roaring Moon)
    if re.findall("\w+\s+\w+", pokemon_name):
        poke_split = series_search_name.split(' ')
        series_search_name = f'{poke_split[0]}%20{poke_split[1]}'.lower()
    series = os.getenv('SERIES')
    url = "https://www.pikalytics.com/pokedex/"+series+'/'+series_search_name
    logger.debug('Pokemon series web crawler query: ' + url)

    rs = requests.get(url=url)
    specific_soup = BeautifulSoup(rs.text, "html.parser")
    details = specific_soup.select('.pokedex-category-wrapper')
    logger.debug(pokemon_name+' record start...')

    if len(details) == 0:
        logger.info(pokemon_name+' is not in this series.')
        return TextSendMessage(f'賽季 {series} 沒有 {pokemon_name}')
    else:
        contents = []
        # 或許可以把對應 API 都放在 mapping 裏面
        pikalytic_mapping = {1: '招式', 2: '隊友', 3: '物品', 4: '特性', 5: '努力值'}
        for index in range(1, len(details)):
            s = details[index].select('.pokedex-move-entry-new')
            item, items = '', []
            logger.debug(f'搜尋 {pikalytic_mapping[index]}')
            # 整理爬蟲下來各個清單對應的陣列
            for entry_idx in range(0, len(s)):
                if index == 5 and entry_idx == 5:
                    break

                item = arrange_text(s[entry_idx].text)
                if item[0] == 'Other':
                    break
                items.append(item)

            if index == 1:
                with sqlite.connect() as con:
                    for it in items:
                        item_query = sqlite.exec_one(
                            con,
                            f"SELECT name_zh, category FROM t_move WHERE name_en == '{it[0]}'")
                        it[0] = item_query['name_zh']
                        it[1] = item_query['category']
                logger.info('Move query result: ' + str(items))
            elif index == 3:
                # 針對物品欄把 request 拉出來寫在放入函式
                # 若之後重複可單獨在包裝
                with sqlite.connect() as con:
                    for it in items:
                        item_query = sqlite.exec_one(
                            con,
                            f"SELECT name_zh, img_url FROM t_item WHERE name_en == '{it[0]}'")
                        it[0] = item_query['name_zh']
                logger.debug('Item query result: ' + str(items))
            elif index == 4:
                with sqlite.connect() as con:
                    for it in items:
                        item_query = sqlite.exec_one(
                            con,
                            f"SELECT name_zh, effect FROM t_ability WHERE name_en == '{it[0]}'")
                        it[0] = item_query['name_zh']
                logger.debug('Ability query result: ' + str(items))
            elif index == 5:  # 努力值, 長度==8
                with sqlite.connect() as con:
                    for it in items:
                        item_query = sqlite.exec_one(
                            con,
                            f"SELECT name_zh FROM t_nature WHERE name_en == '{it[0]}'")
                        it[0] = item_query['name_zh']
                logger.debug('Nature query result: ' + str(items))
            # 輸出成 Flex，若 API 有圖片可能需要另外處理
            contents.append(skill_list(
                name=pikalytic_mapping[index], abilities=items, url=url))
        logger.info('Ready to generate FlexMessage...')
        return FlexSendMessage(alt_text=pokemon_name, contents={
            "type": "carousel",
            "contents": contents
        })


def search_specific_pokemon_by_wiki(pokemon_name='快龍'):
    pokemon_row_list = pokemon_wiki(pokemon_name)

    if pokemon_row_list is not None and len(pokemon_row_list) > 0:
        eng_name, poke_img = find_pokemon_image(pokemon_row_list)
        logger.info(poke_img)
        with sqlite.connect() as con:
            poke_query = sqlite.exec_one(
                con,
                f"SELECT idx, name_zh FROM t_pokemon WHERE name_en == '{eng_name}'")
            logger.info(
                "Specific Pokemon query from sqlite: "+str(poke_query))
            poke_detail = sqlite.exec_one(
                con,
                """
                SELECT * FROM t_pokemon_detail_base_stat WHERE idx == '{}'
                """.format(poke_query.get("idx")))
        logger.info('The Pokemon status is: '+str(poke_detail))

        Zh_name, _ = find_pokemon_name(eng_name)
        # showdown = requests.get(
        #     'https://play.pokemonshowdown.com/data/pokedex.json')
        # pokemon_dict = showdown.json()[eng_name.replace(' ', '').lower()]
        # logger.info(pokemon_dict)
        response_flex = specific_flex(
            image=poke_img, name=[Zh_name, eng_name], body=poke_detail)
        return FlexSendMessage(
            alt_text=eng_name, contents=response_flex)
    else:
        logger.info('關鍵字找不到' + pokemon_name)
        return TextSendMessage('找不到'+pokemon_name)
