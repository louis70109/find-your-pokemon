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


def pokemon_wiki(pokemon_name, language='zh'):
    url = "https://wiki.52poke.com/{}/{}".format(
        'zh-hant' if language == 'zh' else 'en',
        '%E5%AE%9D%E5%8F%AF%E6%A2%A6%E5%88%97%E8%A1%A8%EF%BC%88%E5%9C%A8%E5%85%B6%E4%BB%96%E8%AF%AD%E8%A8%80%E4%B8%AD%EF%BC%89')
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    pokemon_table = soup.select('table')[1]
    pokemon_rows = pokemon_table.select('tr')[2:]
    
    for row in pokemon_rows:
        if language == 'en':
            name = row.select('td')[7].text
        else:
            name = row.select('td')[2].text
        
        if pokemon_name in name:
            logger.debug(f"Found Pokemon '{pokemon_name}' in row: {row}")
            return row
    
    logger.debug("Pokemon '{}' not found in wiki".format(pokemon_name))
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
