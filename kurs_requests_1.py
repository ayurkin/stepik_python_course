import requests
import lxml.html as parser

A = "https://stepic.org/media/attachments/lesson/24472/sample1.html"
B = "https://stepic.org/media/attachments/lesson/24472/sample2.html"
# A = input()
# B = input()


answer = "No"
sub_sub_links = []


def links_getter(url: str):
    try:
        res = requests.get(url)
        html = parser.document_fromstring(res.text)
        if res.status_code == 200:
            return html.xpath("//a/@href")
    finally:
        return []


sub_links = links_getter(A)


if sub_links:
    for i in sub_links:
        sub_sub_links += links_getter(i)

    if B in sub_sub_links:
        answer = "Yes"

print(answer)

