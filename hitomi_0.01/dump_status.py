#! /usr/bin/python3

from htm_status import *

for i in range(500):
    try:
        get_status(i, 'dump')
    except Exception as ex:
        print(ex)
