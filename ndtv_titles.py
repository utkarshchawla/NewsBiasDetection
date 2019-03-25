from bs4 import BeautifulSoup
from urllib.request import urlopen
import collections
import pickle
import datetime
import os

cat = "Sports"  # select category.

ndtv = collections.defaultdict(list)  # dict to store NDTV data.

# load the saved factual dict from hard disk using pickle
with open(f"factual-{cat}.pickle", "rb") as handle:
    factual = pickle.load(handle)

# change the date format such that it can be used in NDTV urls.
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


# logic to match every DD news article with a corresponding NDTV article.
def get_match(dd_title, dd_date):
    hi = 0  # variable to keep track of the maximum number of matches.
    rl = None  # variable used to return the link.

    # remove all non alphanumeric characters from the title.
    translationtable = str.maketrans("", "", "!@#$%^&*()-_+=|/<>.`~,:\"")
    # change the title to lowercase and convert it to a list by splittin across " ".
    dd_title = dd_title.translate(translationtable).lower().split(" ")

    # calculate the prev and the next dates.
    prev = datetime.datetime.strptime(dd_date, '%d-%m-%Y') - datetime.timedelta(1)
    prev = prev.strftime('%d-%m-%Y')
    next = datetime.datetime.strptime(dd_date, '%d-%m-%Y') + datetime.timedelta(1)
    next = next.strftime('%d-%m-%Y')

    dlist = [dd_date, next, prev]
    for d in dlist:
        article_list = ndtv[d]  # get the list of NDTV articles for the corresponding date "d".
        for tup in article_list:
            count = 0
            ndtv_title = tup[0].translate(translationtable).lower().split(" ")
            # do a keyword matching between title of the DD article and that of the NDTV article.
            for word in dd_title:
                if len(word) < 4: continue  # ignore words of len < 4
                if word in ndtv_title:
                    count += 1
            if count > hi:
                hi = count
                rl = tup[1]
    # Return link if the number of keywords matched is greater than two, else return None.
    if hi > 2:
        return rl
    else:
        return None


final_links = collections.defaultdict(list)  # dict to store both DD and the corresponding NDTV link.
for date in factual:
    for tup in factual[date]:
        ndtv_link = get_match(tup[0], date)
        if ndtv_link is not None:
            final_links[date].append((tup[1], ndtv_link))

# save the final dict to hard disk using pickle
with open(f"final_links_{cat}.pickle", "wb") as handle:
    pickle.dump(final_links, handle)
print(final_links)

# calculate the total number of final links.
total = 0
for date in final_links:
    total += len(final_links[date])
print(total)
