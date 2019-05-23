#!/usr/bin/env python
#!coding: utf-8
"""
Updates games.json and starts up the angular site
usage:
    ./manage.py (runserver [--update]|update-games-list) [-v]

options:
    runserver           Start Angular app 
    update-games-list   Update games list
    -v                  Verbose [default: True]
    --update            Same as update-games-list but update before run server
"""

from __future__ import print_function
import sys
import re
import requests
import json
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
from docopt import docopt

GAMES_FILE="src/assets/games.json"

def update_games_list(verbose=False):
    path = "https://www.xbox.com/en-US/xbox-one/backward-compatibility/js/bc-GamesList.js"
    if verbose:
        print("Getting {path}".format(path=path))
    response = requests.get(path)
    file_content = response.content
    found = re.search(r"bcGames = (\[.*\])", file_content, flags=re.DOTALL)
    if found:
        print("Games found")
        games_list = found.group(1)
        games_list = re.sub("\s{2,}(\w+):", "\"\\1\":", games_list)
        games_list = re.sub("(\s)'", "\g<1>\"", games_list)
        games_list = re.sub(r"'([\s|,])", "\"\g<1>", games_list)
        games_list = re.sub(r"\"(,)\s+}", "\"}", games_list)
        
        print(games_list)
        games_list = json.loads(games_list)
        
        for game in games_list:
            game['title'] = game['title'].strip()
        
        with open(GAMES_FILE, "w") as games_file:
            json.dump(games_list, games_file, indent=4, sort_keys=True)
    return 0
    
def run_server(verbose=False):
    HandlerClass = SimpleHTTPRequestHandler
    ServerClass  = BaseHTTPServer.HTTPServer
    Protocol     = "HTTP/1.0"
    port         = 8000
    server_address = ('', port)

    HandlerClass.protocol_version = Protocol
    httpd = ServerClass(server_address, HandlerClass)

    sa = httpd.socket.getsockname()
    print("Serving HTTP on", sa[0], "port", sa[1], "...")
    httpd.serve_forever()    
    
def main(config):
    """Main program"""
    
    if config["runserver"]:
        if config["--update"]:
            update_games_list(verbose=config["-v"])
        return run_server(verbose=config["-v"])
    elif config["update-games-list"]:
        return update_games_list(verbose=config["-v"])


if __name__ == "__main__":
    CONFIG = docopt(__doc__)
    sys.exit(int(main(CONFIG) or 0))
