#!/usr/bin/env python
#!coding: utf-8
"""
Updates games.json and starts up the angular site
usage:
    ./start.py [-v]

options:
    -v          Verbose [default: True]
"""

from __future__ import print_function
import sys
import re
import requests
import json
from docopt import docopt


def main(config):
    """Main program"""
    path = "http://www.xbox.com/en-US/xbox-one/backward-compatibility/bcglist.js"
    if config['-v']:
        print("Getting {path}".format(path=path))
    response = requests.get(path)
    file_content = response.content
    found = re.search(r"var bcgames = (\[.*\]);", file_content, flags=re.DOTALL)
    if found:
        games_list = found.group(1)
        games_list = games_list.replace("image:", "\"image\":")
        games_list = games_list.replace("url:", "\"url\":")
        games_list = games_list.replace("title:", "\"title\":")
        games_list = games_list.replace(r"(\s)(\')", "\1\"")
        games_list = games_list.replace(r"(\')([\s|,])", "\"\2")
        print(games_list)
        #print(json.loads("""[{"image":"http://download.xbox.com/content/images/66acd000-77fe-1000-9115-d802584111e9/1033/boxartlg.jpg","url":"http://marketplace.xbox.com/en-US/Product/Zumas-Revenge/66acd000-77fe-1000-9115-d802584111e9","title": 'Zumas Revenge!'}]"""))
    return 0


if __name__ == "__main__":
    ARGS = docopt(__doc__)
    sys.exit(int(main(ARGS) or 0))
