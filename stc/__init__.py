import os
from steam import WebAPI


def get_key():
    if os.path.isfile('steamapi.key'):
        f = open('steamapi.key', 'r')
        return str(f.readline())
    return ''

steamKey = get_key()
steamApp = WebAPI(key=steamKey)


from stc import steamcore
