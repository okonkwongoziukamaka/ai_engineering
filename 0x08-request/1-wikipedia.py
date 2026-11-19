# a program that uses request to go to wikipedia and search for the istory of Aristotle

import requests

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
response = requests.get("https://en.wikipedia.org/wiki/Aristotle", headers=header)
print(response.status_code)
print(response.text)

# data = response.json()
# print(data.url("current_user_url"))

