# %%
from bs4 import BeautifulSoup
import requests
import os
import pandas as pd
import numpy as np
import re
from bs4 import NavigableString

def surrounded_by_strings(tag):
    return (isinstance(tag.next_element, NavigableString)
            and isinstance(tag.previous_element, NavigableString))
# %%
url = 'https://www.imdb.com/title/tt0110912/?ref_=nv_sr_srsg_0'
headers = "headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36','referer': 'https://www.google.com/'}"

response = requests.get(url, headers={'referer': 'https://www.google.com/'})
# %%

html = response.text
# %%
print(html)
# %%
## parse through beautiful soup
soup = BeautifulSoup(html, 'html.parser')
# %%
print(soup)
# %%
soup.prettify()
# %%
soup.title
# %%
soup.title.name
# %%

# %%
title_cast = soup.find('section', attrs={'data-testid': 'title-cast'})
# %%
print(title_cast)
# %%
actors = title_cast.find_all("a", attrs={"data-testid":"title-cast-item__actor"})
# %%
print(actors[0].text)
# %%
for i in range(len(actors)):
    print(actors[i].text)
# %%
actor_links = title_cast.find_all("a", attrs={"data-testid":"title-cast-item__actor"})
# %%
# %%
actor_dict = {}
for index, link in enumerate(actor_links):
    actor_dict[actor_links[index].text] = str('https://www.imdb.com/' + actor_links[index]['href'])
# %%
actor_dict
# %%
