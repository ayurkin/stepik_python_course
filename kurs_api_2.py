import requests
import json

url_template = "https://api.artsy.net/api/artists/{}"

client_id = 'b2768ca246c1fe350567'
client_secret = '3c94f6b6f38d9c5de476d4a4456e9a60'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]


# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}
# инициируем запрос с заголовком
authors_dict = dict()
with open("dataset_24476_4(1).txt") as f:
    for line in f:
        line = line.strip()

        r = requests.get(url_template.format(line), headers=headers)
        j = json.loads(r.text)
        authors_dict[j['sortable_name']] = int(j['birthday'])



authors_dict=sorted(authors_dict.items(), key=lambda x: (x[1], x[0]))

for author in authors_dict:
    print(author[0])