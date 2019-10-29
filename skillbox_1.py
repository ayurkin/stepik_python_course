import requests

for i in range(1000):
    r = requests.get("https://habr.com/ru/")
    print(r.text)