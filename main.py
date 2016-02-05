#!/usr/bin/env python
#!coding: utf-8

from __future__ import print_function
from colorama import init, Fore
import requests
import re

init()

my_games = [r"Lego.*Pirates",
            r"Lego.*Star Wars", 
            r"Creed.*III",
            r"GTA.*(V|5)"]

PATH = "http://www.xbox.com/en-US/xbox-one/backward-compatibility/bcglist.js"

got = requests.get(PATH)

games = re.findall(r"title:.*'(.*)'", got.content, re.M)

games = [ game.strip() for game in games]

games = sorted(games)

def contains(game):
    for my_game in my_games:
        if re.search(my_game.lower(), game.lower(), re.IGNORECASE):
            return True
    return False

has_games = [ game for game in games if contains(game) ]

for game in has_games:
    print(Fore.GREEN + game)
