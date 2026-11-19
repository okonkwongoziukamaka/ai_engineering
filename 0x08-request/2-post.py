# a prgram that uses post request

import requests

payload = {"Username": "Bryana", "Password": "ngozi4z"}
response = requests.post("https://httpbin.org/post", data=payload)
print(response.text)