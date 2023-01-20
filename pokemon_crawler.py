import requests
import re
from bs4 import BeautifulSoup

url = "https://wiki.52poke.com/zh-hant/%E5%AE%9D%E5%8F%AF%E6%A2%A6%E5%88%97%E8%A1%A8%EF%BC%88%E5%9C%A8%E5%85%B6%E4%BB%96%E8%AF%AD%E8%A8%80%E4%B8%AD%EF%BC%89"
r = requests.get(url=url)
soup = BeautifulSoup(r.text, "html.parser")
pokemon_table = soup.select('table')[1]
pokemon_rows = pokemon_table.select('tr')[1003] # need loop
zh_name = pokemon_rows.select('td')[2].text

message = '賽富豪'
reg = f"{message}.*"
x = re.findall(reg, zh_name)
print(x)

if len(x) > 0:
  zh_name_url = pokemon_rows.select('td')[2].findChild('a')['href']
  eng_name = pokemon_rows.select('td')[7].text
  poke_url = 'https://wiki.52poke.com'+zh_name_url
  print('------------------')
  print(zh_name)
  print(poke_url)
  print(eng_name)
  print('------------------')
else:
  print('找不到')




poke_res = requests.get(url=poke_url)
poke_soup = BeautifulSoup(poke_res.text, "html.parser")

print('****************')

hp = poke_soup.select('tr.bgl-HP')[0].select('div')[1].text
attack = poke_soup.select('tr.bgl-攻击')[0].select('div')[1].text
defense = poke_soup.select('tr.bgl-防御')[0].select('div')[1].text
s_attack = poke_soup.select('tr.bgl-特攻')[0].select('div')[1].text
s_defense =  poke_soup.select('tr.bgl-特防')[0].select('div')[1].text
speed = poke_soup.select('tr.bgl-速度')[0].select('div')[1].text 
print(hp)
print(attack)
print(defense)
print(s_attack)
print(s_defense)
print(speed)