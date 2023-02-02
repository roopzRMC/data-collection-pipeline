
# %%
from bs4 import BeautifulSoup
import requests
import os
import pandas as pd
import numpy as np
import re
from bs4 import NavigableString
import time
# %%
url = 'https://www.zoopla.co.uk/new-homes/property/london/?q=London&results_sort=newest_listings&search_source=new-homes&page_size=25&pn=1&view_type=list'
response = requests.get(url, headers={'referer': 'https://www.google.com/'})
html = response.text
soup = BeautifulSoup(html, 'html.parser')
# %%
soup
# %%
prop_address = soup.find_all("h3", class_ = 'c-eFZDwI')
# %%
prop_type = soup.find_all("h2", class_ = 'c-hNUmYp')
# %%
prices = soup.find_all('p', class_ = 'c-bTssUX')
# %%
prices
# %%
prop_dict = {}

# %%
master_div = soup.find_all("div", class_ = 'c-PJLV c-PJLV-igALLAE-css')
# %%
master_div
# %%
len(master_div)

# %%

property_1 = soup.find("div", class_ = 'c-PJLV c-PJLV-igALLAE-css')
# %%
print(property_1.next_sibling)
# %%

prop_table = soup.find('div', class_ = 'css-1kk52wv epbptbk6')
# %%
addresses = prop_table.find_all("h3", class_ = 'c-eFZDwI')
prop_type = prop_table.find_all("h2", class_ = 'c-hNUmYp')
bedrooms = prop_table.find_all('span', class_ ="c-PJLV")

# %%
bedrooms[3].text
# %%
len(bedrooms)
# %%
prop_dict = {}
for index, property in enumerate(addresses):
    prop_dict[index] =   {prop_type[index].text : addresses[index].text}
# %%
prop_dict

# %%
len(prop_dict)
# %%
for i in range(10):
    globals()[f'x{i}']=i
# %%
## scrape pages 2 - 5
### create the urls to scrape
for i in range(2, 6):
    globals()[f'url{i}']= str('https://www.zoopla.co.uk/new-homes/property/london/?q=London&results_sort=newest_listings&search_source=new-homes&page_size=25&pn=' + str(i))
    response = requests.get(globals()[f'url{i}'], headers={'referer': 'https://www.google.com/'})
    html = response.text
    globals()[f'soup{i}'] = BeautifulSoup(html, 'html.parser')
    prop_table = globals()[f'soup{i}'].find('div', class_ = 'css-1kk52wv epbptbk6')
    addresses = prop_table.find_all("h3", class_ = 'c-eFZDwI')
    prop_type = prop_table.find_all("h2", class_ = 'c-hNUmYp')
    for index, property in enumerate(addresses):
        prop_dict[list(prop_dict.keys())[-1]+1] =   {prop_type[index].text : addresses[index].text}

    time.sleep(1)
# %%
prop_dict
# %%
list(prop_dict.keys())[-1]
# %%
url5
# %%
