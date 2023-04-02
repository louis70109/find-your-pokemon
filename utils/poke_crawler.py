import logging
import requests
from typing import Tuple
from bs4 import BeautifulSoup


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
            logger.debug(f"Found Pokemon '{pokemon_name}'")
            return row

    logger.debug("Pokemon '{}' not found in wiki".format(pokemon_name))
    return None


def find_pokemon_image(pokemon_row_list: BeautifulSoup) -> Tuple[str, str]:
    eng_name = pokemon_row_list.select('td')[7].text.rstrip()
    poke_image_name = "".join(eng_name.replace("-", "")).lower()
    poke_img = f'https://play.pokemonshowdown.com/sprites/gen5/{poke_image_name}.png'
    logger.debug(f'Pokemon image url is: {poke_img}')
    return eng_name, poke_img


def arrange_text(text: str):
    return list(filter(None, text.rstrip().split('\n')))
