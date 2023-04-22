import requests
import logging
import os
from bs4 import BeautifulSoup
import sys

logging.basicConfig(level=os.getenv('LOG', 'INFO'))

if len(sys.argv) < 3:
    logging.warning("Usage: python pikalytic_check.py [arg1] [arg2] [arg3]...")
    sys.exit(1)

SERIES = requests.get(sys.argv[1]).json()
LINE_ADMIN = sys.argv[2]
LINE_CHANNEL_ACCESS_TOKEN = sys.argv[3] if len(sys.argv) > 2 else None

# 設定目標 URL
url = 'https://www.pikalytics.com/pokedex'

# 發送 HTTP GET 請求
res = requests.get(url)

# 將 HTML 轉換成 BeautifulSoup 物件
soup = BeautifulSoup(res.text, 'html.parser')

# 找到目標 select 元素
select = soup.find('select', id='format_dd')

# 找到目標 optgroup 元素
optgroup = select.find('optgroup', label='Pokemon Scarlet & Violet')

# 找到 optgroup 中的第一個 option 元素，並取出其 value 屬性值
value = optgroup.find('option')['value'].split('-')[0]

logging.info(f"Pokemon Scarlet & Violet 的 ID 為：{value}")

if SERIES != value:
    logging.warning("Need to change SERIES")
    r = requests.post(
        url='https://api.line.me/v2/bot/message/push',
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {LINE_CHANNEL_ACCESS_TOKEN}"},
        json={
            "to": LINE_ADMIN,
            "messages": [
                {
                    "type": "text",
                    "text": f"Need to change env var.\nProduction Series: {SERIES}\nPikalytics Series: {value}"
                }
            ]})
