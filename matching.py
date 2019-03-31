import pickle
from tqdm import tqdm
from helper_functions import get_match
import collections

cat = "Sports"
with open(f"pickle_files/factual-{cat}.pickle", "rb") as handle:
    factual = pickle.load(handle)
with open(f"pickle_files/tn_{cat}.pickle", "rb") as handle:
    tn = pickle.load(handle)
with open("pickle_files/NDTV.pickle", "rb") as handle:
    ndtv = pickle.load(handle)

ndtv_nf = 0
tn_nf = 0
final_links = collections.defaultdict(list)
for date in tqdm(factual):
    for tup in factual[date]:
        ndtv_link = get_match(tup[0], date, ndtv)
        tn_link = get_match(tup[0], date, tn)
        if ndtv_link is not None and tn_link is not None:
            final_links[date].append((tup[1], ndtv_link, tn_link))
        elif ndtv_link is not None:
            tn_nf += 1
        elif tn_link is not None:
            ndtv_nf += 1

with open(f"pickle_files/final_links_{cat}.pickle", "wb") as handle:
    pickle.dump(final_links, handle)
print(final_links)

total = 0
for date in final_links:
    total += len(final_links[date])
print(total)

print(ndtv_nf)
print(tn_nf)
