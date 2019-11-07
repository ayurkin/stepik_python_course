import requests
import lxml.html as parser

A = "https://stepic.org/media/attachments/lesson/24472/sample0.html"
B = "https://stepic.org/media/attachments/lesson/24472/sample2.html"
# A = input()
# B = input()
# print(A)
# print(B)

answer = "No"

def links_getter(url: str):
    try:
        res = requests.get(url)
    except Exception:
        return []
    if not res.status_code == 200:
        return []
    else:
        html = parser.document_fromstring(res.text)
        return html.xpath("//a/@href")


sub_links = links_getter(A)
sub_sub_links = []
if len(sub_links) == 0:
    print("No")
else:
    for i in sub_links:
        sub_sub_links += links_getter(i)

    if B in sub_sub_links:
        print("Yes")
    else:
        print("No")


# def links_searcher(url:str):
#     # URL = "https://stepic.org/media/attachments/lesson/24472/sample0.html"
#     # try:
#     # page = requests.get(url)
#     # except :
#
#     soup = BeautifulSoup(page.content, features='lxml')
#     all_links = [link.get("href") for link in soup("a")]
#     return all_links
#
# print(links_searcher(A))
