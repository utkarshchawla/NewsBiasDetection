from bs4 import BeautifulSoup
from urllib.request import urlopen
import collections
import pickle

cat = "Sports"  # select category
cats = {"National": 6, "Entertainment": 14, "Sports": 13}  # codes for each category. Used in DD news URL.


def get_titles():
    d = collections.defaultdict(list)  # dictionary to store factual data
    page = ['']
    # select the number of pages you want to scrape
    num_pages = 30
    for i in range(num_pages):
        page.append(f'&page={i + 1}')
    for pageno in page:
        url = f"http://ddnews.gov.in/about/news-archive?title=&news_type={cats[cat]}&changed_1=&changed_2={pageno}";
        page = urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
        headline = soup.find_all('span', attrs={'class': 'field-content'})
        # For each item on the page, get it's date, link and title.
        for item in headline:
            date = item.find('p', attrs={'class': 'archive-date'}).get_text().split("|")[0]
            date = date[1:len(date) - 1]
            link = f"http://ddnews.gov.in{item.find('a').get('href')}"
            title = item.find('p', attrs={'class': 'archive-title'}).get_text()
            # append the title and the link of the article to the dict corresponding to it's date(key of the dict)
            d[date].append((title, link))

    return d


factual = get_titles()

# save the dict to hard disk using pickle.
with open(f"factual-{cat}.pickle", "wb") as handle:
    pickle.dump(factual, handle)

# calculate the total number of articles scrapped
total = 0
for date in factual:
    total += len(factual[date])
print(total)
print(factual)
