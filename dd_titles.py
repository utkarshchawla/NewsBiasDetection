from bs4 import BeautifulSoup
from urllib.request import urlopen


def get_titles():
    # page = ['', '&page=1', '&page=2', '&page=3']
    page = ['']
    link = []
    title = []
    date = []
    for pageno in page:
        url = f"http://ddnews.gov.in/about/news-archive?title=&news_type=6&changed_1=&changed_2={pageno}";
        page = urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
        headline = soup.find_all('span', attrs={'class': 'field-content'})

        for item in headline:
            link.append(f"http://ddnews.gov.in{item.find('a').get('href')}")
            title.append(item.find('p', attrs={'class': 'archive-title'}).get_text())
            date.append(item.find('p', attrs={'class': 'archive-date'}).get_text())

    return title, date, link
