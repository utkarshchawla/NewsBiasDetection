from factual_titles import get_titles
import pickle
import time
import requests
from bs4 import BeautifulSoup

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

dd_titles, dd_date, dd_links = get_titles()


def helper(news_site):
    rlinks = []
    last_req = time.time()
    for title in dd_titles:
        extra = "&aqs=chrome..69i57j69i58.24088j0j4&sourceid=chrome&ie=UTF-8"
        query = f'site%3A{news_site}+' + title.replace(" ", "+") + extra
        r = requests.get(f"https://www.google.com/search?q={query}", headers=headers)
        soup = BeautifulSoup(r.content, "html5lib")
        links = soup.findAll("div", {"class": "r"})
        for link in links:
            link_href = link.find('a').get('href')
            if link_href == None:
                rlinks.append("not found")
            else:
                rlinks.append(link_href)
            break
        now = time.time()
        delay = last_req + 0.600 - now
        last_req = now
        if delay >= 0:
            time.sleep(delay)
    return rlinks


ndtv_links = helper("www.ndtv.com")
tn_links = helper("www.timesnownews.com")
print(dd_links)
print(ndtv_links)
print(tn_links)

with open('dd.pickle', 'wb') as f:
    pickle.dump(dd_links, f)
with open('dd_date.pickle', 'wb') as f:
    pickle.dump(dd_date, f)
with open('ndtv.pickle', 'wb') as f:
    pickle.dump(ndtv_links, f)
with open('tn.pickle', 'wb') as f:
    pickle.dump(tn_links, f)
