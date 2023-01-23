import requests
import re
from bs4 import BeautifulSoup

url = "https://www.pikalytics.com/pokedex/"
r = requests.get(url=url)
soup = BeautifulSoup(r.text, "html.parser")
all_rank = soup.select('span.pokemon-name')
all_trending = soup.select('.float-right.margin-right-20')

# print(all_rank[0].text.rstrip())

# print(all_trending[0].text.rstrip())
for i in range(len(all_rank)):
  print(all_rank[i].text.rstrip()+" "+all_trending[i].text.rstrip())
  print()

# print(poke_trending)
# poke_usage = soup.select('.pokemon-ind-summary-text')
# print(poke_usage[0].text)
# print(poke_usage[1].text)

# https://www.pikalytics.com/pokedex/gen9vgc2023series1/meowscarada


# hp = poke_soup.select('tr.bgl-HP')[0].select('div')[1].text
# attack = poke_soup.select('tr.bgl-攻击')[0].select('div')[1].text
# defense = poke_soup.select('tr.bgl-防御')[0].select('div')[1].text
# s_attack = poke_soup.select('tr.bgl-特攻')[0].select('div')[1].text
# s_defense =  poke_soup.select('tr.bgl-特防')[0].select('div')[1].text
# speed = poke_soup.select('tr.bgl-速度')[0].select('div')[1].text 
# print(hp)
# print(attack)
# print(defense)
# print(s_attack)
# print(s_defense)
# print(speed)