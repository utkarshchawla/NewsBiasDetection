from bs4 import BeautifulSoup
from urllib.request import urlopen
import collections


def get_titles():
    d = collections.defaultdict(list)
    page = ['']
    for i in range(20):
        page.append(f'&page={i + 1}')
    for pageno in page:
        url = f"http://ddnews.gov.in/about/news-archive?title=&news_type=6&changed_1=&changed_2={pageno}";
        page = urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
        headline = soup.find_all('span', attrs={'class': 'field-content'})

        for item in headline:
            date = item.find('p', attrs={'class': 'archive-date'}).get_text()
            key = date.split("-")
            key = key[2][:4] + "-" + key[1]
            link = f"http://ddnews.gov.in{item.find('a').get('href')}"
            title = item.find('p', attrs={'class': 'archive-title'}).get_text()
            d[key].append((title, link, date))

    return d
