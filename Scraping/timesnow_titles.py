import requests
import json
import pickle
import datetime
import collections
from tqdm import tqdm

timesnow = collections.defaultdict(list)

cat = "Sports"
cats = {
    "National": ["https://www.timesnownews.com/load-more/166/1/all/latest/",
                 "/391480,391477,391462,391446,391430,391422,391404,391391,391382,391379/0",
                 "https://www.timesnownews.com/india"],
    "Entertainment": ["https://www.timesnownews.com/load-more/167/1/all/latest/",
                      "/391496,391469,391453,391483,391306,391450,389859,389798/0",
                      "https://www.timesnownews.com/entertainment"],
    "Sports": ["https://www.timesnownews.com/load-more/168/1/all/latest/",
               "/391412,391415,391423,391396,391319,391341,391390,391340/0",
               "https://www.timesnownews.com/sports"]}

with open(f"pickle_files/factual-{cat}.pickle", "rb") as handle:
    factual = pickle.load(handle)

last_date = list(factual.keys())[len(factual) - 1]
last_date = datetime.datetime.strptime(last_date, '%d-%m-%Y')
# print(last_date.strftime('%d-%m-%Y'))

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Authority': 'www.timesnownews.com',
    'Referer': cats[cat][2]}
flag = True
for pg in tqdm(range(1388)):
    url = cats[cat][0] + str(pg) + cats[cat][1]
    r = requests.get(url, params={}, headers=headers)
    article = []
    try:
        articles = json.loads(r.content)['result_items']
    except:
        print(pg)
    for article in articles:
        date = article['date'].split("|")[0].strip()
        date = datetime.datetime.strptime(date, '%b %d, %Y').strftime('%d-%m-%Y')
        if datetime.datetime.strptime(date, '%d-%m-%Y') < last_date:
            flag = False
            break
        title = article['title']
        link = article["story_url"]
        timesnow[date].append((title, link))
    if flag is False:
        break

total = 0
for date in timesnow:
    total += len(timesnow[date])
print(total)
print(timesnow)

with open(f"pickle_files/tn_{cat}.pickle", "wb") as handle:
    pickle.dump(timesnow, handle)
