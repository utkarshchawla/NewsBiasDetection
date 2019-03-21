import requests
from bs4 import BeautifulSoup
import re

# headers = requests.utils.default_headers()
# headers.update({
#     'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
# })
#
#
# print(headers)
# query = "Goa+CM+Pramod+Sawant+wins+floor+test+\"www.ndtv.com\""
query = "hola"
goog_search = f"https://www.google.co.in/search?q={query}"
headers = {
    "Host": "www.google.co.in",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Cookie": "CGIC=EhQxQzFDSEJGX2VuSU43NzNJTjc3MyJ2dGV4dC9odG1sLGFwcGxpY2F0aW9uL3hodG1sK3htbCxhcHBsaWNhdGlvbi94bWw7cT0wLjksaW1hZ2Uvd2VicCxpbWFnZS9hcG5nLCovKjtxPTAuOCxhcHBsaWNhdGlvbi9zaWduZWQtZXhjaGFuZ2U7dj1iMw; OGPC=19008862-1:19002757-25:19009950-2:19010494-2:19010659-4:; OGP=-19010494:-19010659:; CONSENT=YES+IN.en+; HSID=AkTrkI86ErYsjG02-; SSID=A8JlNwxKYnqMTV1GE; APISID=YP3PDMTiF-PWckkK/AKfHDOhdAkhyPKDXw; SAPISID=lWlR8IUVVsG1etHj/A9tB1Ln3GUuzSVQYU; SID=LQeTrReFu2ZCaIFAHS4JsWsDJmLGYutazoIbEQOIcUmyQZ5tE2WsSB7nH_21JXiwvSuLHA.; NID=164=M6RkkvuPlZ0-t2LiyZDqyKFQqBAhG_nI7y2GuzDib1J6UPxDRqL6VBh11ZKxYSDmvscpgMClSyCqKCgQU0JdvNrLl5n4QBkpqI3GYBmmPFhcsgv-e1U-yjusTmeJZrS0q4Bb2QBChJehcVUxLQnVpB1xJNa7a9wDq9WcXsr5DrxU72FTrFEfa-KXOcjUGkHjOsaj1dxNWGAnUAI0tOyuINonaMrHmg; 1P_JAR=2019-3-20-11; DV=w6rkd-0K9F5XwGsmhb-xJuVTxd-umdYFTGEHJ-SZVwEAAMBLUjyomhJKWgEAADjhRiddubM3WQAAAN5kcmikS5qgFwAAAA; SIDCC=AN0-TYs0GnxmvB4KZVUG17JsFv4QSUSf746uTWkmI80-VvraQr5mNpylIjNcr7dxglKt02xL",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
}
r = requests.get(goog_search, headers=headers)
print(r)
soup = BeautifulSoup(r.content, "html5lib")
# print(soup)
links = soup.findAll("div", {"class": "r"})
# print(links)
for link in links:
    link_href = link.find('a').get('href')
    print(link_href)
    break   
