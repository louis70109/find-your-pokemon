import os

if os.getenv('API_ENV') != 'production':
    from dotenv import load_dotenv

    load_dotenv()

import uvicorn

from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

from routers import webhooks

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.include_router(webhooks.router)


@app.get("/")
async def root():
    return {"message": "Hello World!"}


if __name__ == "__main__":
    port = os.environ.get('PORT', default=8080)
    debug = True if os.environ.get('API_ENV', default='develop') == 'develop' else False
    print('==========start===========')
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=debug)
