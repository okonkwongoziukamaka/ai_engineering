# a program that uses dump to write inside the file

import json

data = {
    "name": "Amaka",
    "gender": "Female",
    "is_married": True,
}
with open("0x08-request/dump.json", "w+") as f:
    json.dump(data, f, indent=2) 