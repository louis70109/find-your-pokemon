import logging
import os

if os.getenv('API_ENV') != 'production':
    from dotenv import load_dotenv

    load_dotenv()

import uvicorn
import requests
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
import tempfile
from routers import webhooks


app = FastAPI()
logging.basicConfig(level=os.getenv('LOG', 'INFO'))
logger = logging.getLogger(__file__)

templates = Jinja2Templates(directory="templates")

# Read Firebase cert from env variable JSON string
firebase_cred = tempfile.NamedTemporaryFile(suffix='.json')
try:
    GOOGLE_KEY = os.environ.get('FIREBASE_CRED', '{}')
    firebase_cred.write(GOOGLE_KEY.encode())
    firebase_cred.seek(0)
    os.environ['FIREBASE_CREDENTIALS'] = firebase_cred.name
    logger.debug(os.environ['FIREBASE_CREDENTIALS'])
except Exception as e:
    logger.error('Firebase key write fail.')
    logger.error(e)
    firebase_cred.close()


app.include_router(webhooks.router)


@app.get("/")
async def root():
    res_showdown = requests.get(
        'https://play.pokemonshowdown.com/data/pokedex.json')
    res_portal = requests.get(
        'https://tw.portal-pokemon.com/play/pokedex/api/v1?key_word=%E5%A6%99%E8%9B%99%E7%A8%AE%E5%AD%90')
    res_wiki = requests.get('https://wiki.52poke.com/wiki/%E4%B8%BB%E9%A1%B5')
    res_lytic = requests.get('https://www.pikalytics.com/pokedex/')
    return {
        'showdown_json': 'up' if res_showdown.json() else 'down',
        'tw_web_portal': 'up' if res_portal.json()['pokemons'] else 'down',
        'wiki': 'up' if res_wiki.status_code == 200 else 'down',
        'pokelytic': 'up' if res_lytic.status_code == 200 else 'down'
    }


@app.get("/healthz")
async def healthz():
    return {"message": "Hello World!"}


@app.get("/season")
async def season():
    return os.getenv('SERIES')


if __name__ == "__main__":
    port = os.environ.get('PORT', default=8080)
    debug = True if os.environ.get(
        'API_ENV', default='develop') == 'develop' else False
    logging.info('Application will start...')
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=debug)
