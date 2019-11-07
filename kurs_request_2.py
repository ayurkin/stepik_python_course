import requests
import lxml.html as parser
import re

A = "http://pastebin.com/raw/2mie4QYa"
# A = input()


def links_getter(url: str):
    try:
        res = requests.get(url)

        if res.status_code == 200:
            return re.findall(r"(?:<a.+href=['\"](?:(?:https?)|(?:ftp))*(?::\/\/)*([\w\.-]{3,})(?:[:\/])?(?:.)*(?:['\"]\s*>))",
                    res.text)
        else:
            return []
    except:
        return []


links = list(set(links_getter(A)))
links.sort()

for link in links:
    print(link)




