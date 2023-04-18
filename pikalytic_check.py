import requests
import os
from bs4 import BeautifulSoup
import sys

# 检查参数个数
if len(sys.argv) < 2:
    print("Usage: python script.py [arg1] [arg2] ...")
    sys.exit(1)

# 获取参数
LINE_ADMIN = sys.argv[1]
LINE_CHANNEL_ACCESS_TOKEN = sys.argv[2] if len(sys.argv) > 2 else None
SERIES = 'gen9vgc2023regc'

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

print(f"Pokemon Scarlet & Violet 的 ID 為：{value}")

r = requests.post(
    url='https://api.line.me/v2/bot/message/push',
    headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {LINE_CHANNEL_ACCESS_TOKEN}"},
    json={"to": LINE_ADMIN,
          "messages": [
              {
                  "type": "text",
                  "text": f"Production Series: {SERIES}\nPikalytics Series: {value}"
              }
          ]})
print(r.json())
