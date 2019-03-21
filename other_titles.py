from bs4 import BeautifulSoup
from urllib.request import urlopen
import collections
from factual_titles import get_titles

ndtv = collections.defaultdict(list)
factual = get_titles()


def freq_map(s):
    translationtable = str.maketrans("", "", "!@#$%^&*()-_+=|/<>.`~,:\"")
    s = s.translate(translationtable)
    s = s.lower()
    my_list = s.split(" ")
    freq = {}
    for item in my_list:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq


# for ndtv
for date in factual:
    url = f"http://archives.ndtv.com/articles/{date}.html"
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    headlines = soup.find("div", class_="related").find_all("a")
    for headline in headlines:
        text = headline.get_text()
        ndtv[date].append((text, headline.get('href'), freq_map(text)))

links = []


def get_match(title, dic_list):
    hi = 0
    rl = ""
    translationtable = str.maketrans("", "", "!@#$%^&*()-_+=|/<>.`~,:\"")
    title = title.translate(translationtable)
    title = title.lower()
    my_list = title.split(" ")
    for tocomp in dic_list:
        count = 0
        dic = tocomp[2]
        for word in my_list:
            if word in dic:
                count += 1
        if count > hi:
            hi = count
            rl = tocomp[1]
    if hi > (len(my_list) + 1) / 2:
        return rl
    else:
        return None


for date in factual:
    dd_list = factual[date]
    ndtv_list = ndtv[date]
    print(len(dd_list))
    for f in dd_list:
        ndtvLink = get_match(f[0], ndtv_list)
        if ndtvLink is not None:
            links.append((f[1], get_match(f[0], ndtv_list)))

print(links)
print(len(links))
