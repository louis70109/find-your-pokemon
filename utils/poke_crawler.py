import logging
import requests
import re
from bs4 import BeautifulSoup

from utils import sqlite

logger = logging.getLogger(__file__)


def find_pokemon_name(pokemon_name):
    # Find pokemon zh-hant name
    res = requests.get(
        'https://tw.portal-pokemon.com/play/pokedex/api/v1?key_word='+pokemon_name)
    logger.debug('Find pokemon name is: '+pokemon_name)
    result = res.json()['pokemons']
    if not result:
        logger.info('Could not find TW name: ' + pokemon_name)
        return pokemon_name, None
        # with sqlite.connect() as con:
        #     item_query = sqlite.exec(con,
        #     f"SELECT name_zh FROM t_pokemon WHERE name_en == '{pokemon_name}'")
        #     logger.info('Could not find TW name, query from Sqlite: '+ str(item_query))
        #     return item_query[0]
    else:
        return result[0]['pokemon_name'], result[0]['pokemon_type_name']


def pokemon_wiki(pokemon, lang='zh'):
    url = "https://wiki.52poke.com/zh-hant/%E5%AE%9D%E5%8F%AF%E6%A2%A6%E5%88%97%E8%A1%A8%EF%BC%88%E5%9C%A8%E5%85%B6%E4%BB%96%E8%AF%AD%E8%A8%80%E4%B8%AD%EF%BC%89"
    r = requests.get(url=url)
    soup = BeautifulSoup(r.text, "html.parser")
    pokemon_table = soup.select('table')[1]
    pokemon_rows = pokemon_table.select('tr')
    for pok in range(2, len(pokemon_rows)):
        if lang == 'en':
            zh_name = pokemon_rows[pok].select('td')[7].text
        else:
            zh_name = pokemon_rows[pok].select('td')[2].text

        reg = f"{pokemon}.*"
        if len(re.findall(reg, zh_name)) > 0:
            logger.debug('Found Pokemon...' + str(pokemon_rows))
            return pokemon_rows[pok]
    logger.debug('Maybe got WIKI problem, need to check wiki status.')
    return None


def find_pokemon_image(pokemon_row_list):
    zh_name_url = pokemon_row_list.select('td')[2].findChild('a')['href']
    eng_name = pokemon_row_list.select('td')[7].text.rstrip()

    poke_url = 'https://wiki.52poke.com'+zh_name_url
    logger.debug('* Finding the pokemon image...')
    poke_res = requests.get(url=poke_url)
    poke_soup = BeautifulSoup(poke_res.text, "html.parser")

    poke_img = 'https:' + \
        poke_soup.select('table.roundy.bgwhite')[0].find('img')['data-url']
    logger.debug('Pokemon image url is: '+poke_img)
    return eng_name, poke_img


def arrange_text(text: str):
    return list(filter(None, text.rstrip().split('\n')))
