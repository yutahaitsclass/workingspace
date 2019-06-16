# import urllib.request
# import requests
# url = urllib.request.urlopen('https://www.google.com/search?q=a&rlz=1C1NDCM_jaJP739JP740&source=lnms&tbm=isch&sa=X&ved=0ahUKEwilsL66y7HiAhUkxYsBHf2NDx0Q_AUIDygC&biw=738&bih=609')
from bs4 import BeautifulSoup
# headers = {
#         "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"
#         }

# request = urllib.request.Request(url=url, headers=headers)
# response = urllib.request.urlopen(request)
# soup = BeautifulSoup(response, "html.parser")
# # for div in soup.find_all('div', class_="title _ellipsis"):
# #     print(div.text)
# header2 = soup.find("h2")
# print(header2)

#!/usr/bin/python3
import urllib.request

url = "https://www.google.com/search?q=a&rlz=1C1NDCM_jaJP739JP740&source=lnms&tbm=isch&sa=X&ved=0ahUKEwilsL66y7HiAhUkxYsBHf2NDx0Q_AUIDygC&biw=738&bih=609"
headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
        }

request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
html = response.read().decode('utf-8')
header2 = html.find("h1")
print(header2)