#!coding: utf-8

import requests
from bs4 import BeautifulSoup
import re

my_games = [r"Lego.*Pirates",
            r"Lego.*Star Wars", 
            r"Creed.*III",
            r"GTA.*(V|5)"]

print("start")
PATH = "http://www.xbox.com/pt-BR/xbox-one/backward-compatibility/available-games"

session = requests.Session()

got = session.get(PATH)

soup = BeautifulSoup(got.content, "html.parser")

print(soup.contents)

games = soup.find_all(attrs={"class":"game"})

print(games)

games = sorted(map(lambda x: x.text, games))

print(games)

def contains(game):
    for my_game in my_games:
        if re.search(my_game.lower(), game.lower(), re.IGNORECASE):
            return True
    return False

games = filter(contains, games)

for game in games:
    print(game)
