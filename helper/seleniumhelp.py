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

query = "Justice Pinaki Chandra Ghose appointed first Lokpal of India \"ndtv\""
# query = "hola"
query = query.replace(" ", "+")
driver.get(f"https://www.google.com/search?q={query}")

results = driver.find_elements_by_css_selector('div.g')
link = results[0].find_element_by_tag_name("a")
href = link.get_attribute("href")
print(href)
driver.quit()
