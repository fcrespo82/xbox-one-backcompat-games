#!coding: utf-8

import requests
import re

my_games = [r"Lego.*Pirates",
            r"Lego.*Star Wars", 
            r"Creed.*III",
            r"GTA.*(V|5)"]

PATH = "http://www.xbox.com/en-US/xbox-one/backward-compatibility/bcglist.js"

got = requests.get(PATH)

games = re.findall(r"title:.*'(.*)'", got.content, re.M)

games = [ game.strip() for game in games]

games = sorted(games)

print(games)

def contains(game):
    for my_game in my_games:
        if re.search(my_game.lower(), game.lower(), re.IGNORECASE):
            return True
    return False

games = filter(contains, games)

for game in games:
    print(game)
