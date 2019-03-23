from bs4 import BeautifulSoup
from urllib.request import urlopen
import collections
import pickle

ndtv = collections.defaultdict(list)
with open("factual.pickle", "rb") as handle:
    factual = pickle.load(handle)

factual = list(factual.keys())

for date in factual:
    date = date.split("-")
    date = date[2] + "-" + date[1]
    url = f"http://archives.ndtv.com/articles/{date}.html"
    date = ""
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    headlines = soup.find("div", class_="related").find_all("a")
    for headline in headlines:
        text = headline.get_text()
        link = headline.get('href')
        if link == 'javascript:void(0);':
            date = text
        else:
            ndtv[date].append(link)

print(ndtv)
print(len(ndtv))
