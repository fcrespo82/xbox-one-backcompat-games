#!/usr/bin/env python
#!coding: utf-8
"""usage:
    main.py [--all] [--color]

options:
    --all               List all games
    --color             Colorize the games you have
"""

from __future__ import print_function
from colorama import init, Fore
import requests
import re
import docopt
import sys

ARGS = docopt.docopt(__doc__)

init(autoreset=True, strip=False)

MY_GAMES = [r"Lego.*Pirates",
            r"Lego.*Star Wars",
            r"Creed.*III",
            r"GTA.*(V|5)",
            r"Just.*Dance.*2015"]

PATH = "http://www.xbox.com/en-US/xbox-one/backward-compatibility/bcglist.js"

def get_games():
    """Get the games from the web"""
    got = requests.get(PATH)
    games = re.findall(r"title:.*'(.*)'", got.content, re.M)
    games = [game.strip() for game in games]

    return sorted(games)

def contains(game):
    """Filter a list of games with the ones that I have"""
    for my_game in MY_GAMES:
        if re.search(my_game.lower(), game.lower(), re.IGNORECASE):
            return True
    return False

def main():
    """Main logic for the script"""
    all_games = get_games()
    has_games = [game for game in all_games if contains(game)]

    if ARGS.has_key("--all") and ARGS["--all"]:
        backcompat_games = [game for game in all_games if game not in has_games]
        for game in backcompat_games:
            print(game)
    for game in has_games:
        if ARGS.has_key("--color") and ARGS["--color"]:
            print(Fore.GREEN + game)
        else:
            print(game)

if __name__ == "__main__":
    sys.exit(int(main() or 0))


