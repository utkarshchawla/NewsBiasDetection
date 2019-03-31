from bs4 import BeautifulSoup
from urllib.request import urlopen
from helper_functions import get_match
import collections
import pickle
import datetime
import os
from tqdm import tqdm

cat = "National"  # select category.

ndtv = collections.defaultdict(list)  # dict to store NDTV data.

# load the saved factual dict from hard disk using pickle
with open(f"pickle_files/factual-{cat}.pickle", "rb") as handle:
    factual = pickle.load(handle)

# change the date format such that it can be used in NDTV urls.
dates = []
for date in factual:
    date = date.split("-")
    date = date[2] + "-" + date[1]
    dates.append(date)

print("getting ndtv titles")
for date in tqdm(set(dates)):
    url = f"http://archives.ndtv.com/articles/{date}.html"
    date = ""
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    headlines = soup.find("div", class_="related").find_all("a")
    # For each item(link) on the page, find it's date, link and title.
    for headline in headlines:
        title = headline.get_text()
        link = headline.get('href')
        if link == 'javascript:void(0);':
            date = title
        else:
            # append the title and the link of the article to the dict corresponding to it's date(key of the dict).
            ndtv[date].append((title, link))

# change the NDTV date format such that it matches with the DD date format
for date in list(ndtv.keys()):
    new_date = datetime.datetime.strptime(date, '%d %B %Y').strftime('%d-%m-%Y')
    ndtv[new_date] = ndtv.pop(date)

with open(f"pickle_files/ndtv.pickle", "wb") as handle:
    pickle.dump(ndtv, handle)
