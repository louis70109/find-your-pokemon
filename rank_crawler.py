import requests
import re
from bs4 import BeautifulSoup

print('排名查詢 TOP...')

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

print('-------Find one--------')
print('可放入特定的名字')
series = 'gen9vgc2023series1'


def arrange_text(text: str):
    return list(filter(None, text.rstrip().split('\n')))


rs = requests.get(url=url+series+'/meowscarada')
specific_soup = BeautifulSoup(rs.text, "html.parser")
print(specific_soup.select('.pokedex-category-wrapper'))
print('=====技能=====')
skills = specific_soup.select('.pokedex-category-wrapper')[1]  # skills
skill = skills.select('.pokedex-move-entry-new')[0].text
skill_text = arrange_text(skill)

print(skill_text)


print('-------隊友-------')
teammates = specific_soup.select('.pokedex-category-wrapper')[2]  # teammates
teammate = teammates.select('.pokedex-move-entry-new')[0].text
print(arrange_text(teammate))

print('-------物品-------')
items = specific_soup.select('.pokedex-category-wrapper')[3]
item = items.select('.pokedex-move-entry-new')[0].text
print(arrange_text(item))

print('-------能力-------')
abilities = specific_soup.select('.pokedex-category-wrapper')[4]
ability = abilities.select('.pokedex-move-entry-new')[0].text
print(arrange_text(ability))

print('-------努力值-------')
evs = specific_soup.select('.pokedex-category-wrapper')[5]
ev = evs.select('.pokedex-move-entry-new')[0].text
print(arrange_text(ev))
