# a program that uses get request 

import requests 


response = requests.get("https://api.github.com")
print(response.status_code)
# print(response.text)

data = response.json()
print(data.get("current_user_url"))