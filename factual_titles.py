from bs4 import BeautifulSoup
from urllib.request import urlopen
import collections
import pickle

cat = "Sports"
cats = {"National": 6, "Entertainment": 14, "Sports": 13}


def get_titles():
    d = collections.defaultdict(list)
    page = ['']
    for i in range(30):
        page.append(f'&page={i + 1}')
    for pageno in page:
        url = f"http://ddnews.gov.in/about/news-archive?title=&news_type={cats[cat]}&changed_1=&changed_2={pageno}";
        page = urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
        headline = soup.find_all('span', attrs={'class': 'field-content'})

        for item in headline:
            date = item.find('p', attrs={'class': 'archive-date'}).get_text().split("|")[0]
            date = date[1:len(date) - 1]
            link = f"http://ddnews.gov.in{item.find('a').get('href')}"
            title = item.find('p', attrs={'class': 'archive-title'}).get_text()
            d[date].append((title, link))

    return d


factual = get_titles()

with open(f"factual-{cat}.pickle", "wb") as handle:
    pickle.dump(factual, handle)

total = 0
for date in factual:
    total += len(factual[date])
print(total)
print(factual)