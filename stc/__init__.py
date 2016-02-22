import os
from steam import WebAPI

import sys

basedir = os.path.abspath(os.path.dirname(__file__))
keypath = os.path.join(basedir, 'steamapi.key')


def get_key():
    if os.path.isfile(keypath):
        f = open(keypath, 'r')
        return str(f.readline())
    return None


steamKey = get_key()
if not steamKey:
    sys.exit('Steam API key was not provided.')

steamApp = WebAPI(key=steamKey)

from stc import steamcore
