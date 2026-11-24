# a program that call an API

import requests

def call_api(url):
    res = requests.get(url)
    return res.json()

try:
    response = call_api("https://jsonplaceholder.typicode.com/posts")
except ConnectionError:
    print("network issues")
else:
    print(f"success: {response}")
finally:
    print("cleaning up resources")

