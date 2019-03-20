from dd_titles import get_titles
import pickle
from selenium import webdriver
from fake_useragent import UserAgent

options = webdriver.ChromeOptions()
prefs = {'profile.managed_default_content_settings.images': 2, 'disk-cache-size': 4096}
options.add_experimental_option("prefs", prefs)
options.add_argument('headless')
ua = UserAgent()
userAgent = ua.random
options.add_argument(f'user-agent={userAgent}')
driver = webdriver.Chrome(options=options)

dd_titles, dd_date, dd_links = get_titles()


def helper(news_site):
    rlinks = []
    for title in dd_titles:
        extra = "&aqs=chrome..69i57j69i58.24088j0j4&sourceid=chrome&ie=UTF-8"
        query = f'site%3A{news_site}+' + title.replace(" ", "+") + extra
        driver.get(f"https://www.google.com/search?q={query}")
        results = driver.find_elements_by_css_selector('div.g')
        if len(results) > 0:
            link = results[0].find_element_by_tag_name("a")
            href = link.get_attribute("href")
            rlinks.append(href)
        else:
            rlinks.append("not_found")
    return rlinks


ndtv_links = helper("www.ndtv.com")
tn_links = helper("www.timesnownews.com")
print(dd_links)
print(ndtv_links)
print(tn_links)

with open('dd.pickle', 'wb') as f:
    pickle.dump(dd_links, f)
with open('dd_date.pickle', 'wb') as f:
    pickle.dump(dd_date, f)
with open('ndtv.pickle', 'wb') as f:
    pickle.dump(ndtv_links, f)
with open('tn.pickle', 'wb') as f:
    pickle.dump(tn_links, f)
