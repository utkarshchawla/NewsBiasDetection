from bs4 import BeautifulSoup
from urllib.request import urlopen
import collections
import pickle
import datetime
import os

cat = "Sports"

ndtv = collections.defaultdict(list)
with open(f"factual-{cat}.pickle", "rb") as handle:
    factual = pickle.load(handle)

dates = []
for date in factual:
    date = date.split("-")
    date = date[2] + "-" + date[1]
    dates.append(date)

for date in set(dates):
    url = f"http://archives.ndtv.com/articles/{date}.html"
    date = ""
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    headlines = soup.find("div", class_="related").find_all("a")
    for headline in headlines:
        title = headline.get_text()
        link = headline.get('href')
        if link == 'javascript:void(0);':
            date = title
        else:
            ndtv[date].append((title, link))

for date in list(ndtv.keys()):
    new_date = datetime.datetime.strptime(date, '%d %B %Y').strftime('%d-%m-%Y')
    ndtv[new_date] = ndtv.pop(date)


def get_match(title, date):
    hi = 0
    rl = None
    translationtable = str.maketrans("", "", "!@#$%^&*()-_+=|/<>.`~,:\"")
    title = title.translate(translationtable).lower().split(" ")

    prev = datetime.datetime.strptime(date, '%d-%m-%Y') - datetime.timedelta(1)
    prev = prev.strftime('%d-%m-%Y')

    next = datetime.datetime.strptime(date, '%d-%m-%Y') + datetime.timedelta(1)
    next = next.strftime('%d-%m-%Y')
    dlist = [date, next, prev]
    for d in dlist:
        list = ndtv[d]
        for tup in list:
            count = 0
            test = tup[0].translate(translationtable).lower().split(" ")
            for word in title:
                if len(word) < 4: continue
                if word in test:
                    count += 1
            if count > hi:
                hi = count
                rl = tup[1]
    # return rl
    if hi > 2:
        return rl
    else:
        return None


final_links = collections.defaultdict(list)
for date in factual:
    for tup in factual[date]:
        ndtv_link = get_match(tup[0], date)
        if ndtv_link is not None:
            final_links[date].append((tup[1], ndtv_link))

with open(f"final_links_{cat}.pickle", "wb") as handle:
    pickle.dump(final_links, handle)
print(final_links)
int
total = 0
for date in final_links:
    total += len(final_links[date])
print(total)
