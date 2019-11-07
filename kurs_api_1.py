import requests
import sys
url_template = "http://numbersapi.com/{}/math?json=true"

with open("dataset_24476_3(1).txt") as f:
    for line in f:
        line = line.strip()
        # print(line)
        number = int(line)
        res = requests.get(url_template.format(number))
        data = res.json()
        if data['found']:
            print('Interesting')
        else:
            print('Boring')
