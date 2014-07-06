#! /usr/bin/python3

from htm_status import *

for i in range(500):
    try:
        get_status(i, 'import')
    except:
        pass
