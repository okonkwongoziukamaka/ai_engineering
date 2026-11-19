# a program that loads a json

import json

with open("0x08-request/data.json") as f:
    data=json.load(f)
    print(data)
    