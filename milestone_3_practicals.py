# %%
from bs4 import BeautifulSoup
import requests
import os
import pandas as pd
import numpy as np
import re
from bs4 import NavigableString
import lxml

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
# isloate the section where the actors information is found via the developer tab
title_cast = soup.find('section', attrs={'data-testid': 'title-cast'})
# %%
print(title_cast)
# %%
## within the section above find the tags containsing the actors names
actors = title_cast.find_all("a", attrs={"data-testid":"title-cast-item__actor"})

actors_test = soup.find_all("a", attrs={"class":"sc-bfec09a1-1 gfeYgX"})

# %%
print(actors_test)
print(actors)
# %%
print(actors[0].text)
# %%
for i in range(len(actors)):
    print(actors[i].text)
# %%

# isolate the section where the li
actor_links = title_cast.find_all("a", attrs={"data-testid":"title-cast-item__actor"})
# %%
# %%
## load the names and links in to a dict - have to use enumerate as you need to specify an int when slicing
actor_dict = {}
for index, link in enumerate(actor_links):
    actor_dict[actor_links[index].text] = str('https://www.imdb.com/' + actor_links[index]['href'])
# %%
actor_dict
# %%

## For each actor - navigate to the actors page and get the list of films they have satrred in

## isolate the section where the film list is found
travolta_url = 'https://www.imdb.com/name/nm0000237/'
travolta_response = requests.get(travolta_url, headers={'referer': 'https://www.google.com/'})
travolta_html = travolta_response.text
travolta_soup = BeautifulSoup(travolta_html, 'lxml')

# %%
travolta_soup

# %%
travolta_soup.title
# %%
travolta_films = travolta_soup.find('div', class_ = 'ipc-metadata-list-summary-item__tc')
print(travolta_films)
# %%
trav_films = travolta_soup.find_all(text="ipc-metadata-list-summary-item__t") 
# %%
print(trav_films)
# %%
######### SELENIUM ###########

# %%
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time

# %%
driver = webdriver.Chrome()
def load_and_accept_cookies() -> webdriver.Chrome:
    '''
    Open Zoopla and accept the cookies
    
    Returns
    -------
    driver: webdriver.Chrome
        This driver is already in the Zoopla webpage
    '''
    driver = webdriver.Chrome() 
    URL = "https://www.zoopla.co.uk/new-homes/property/london/?q=London&results_sort=newest_listings&search_source=new-homes&page_size=25&pn=1&view_type=list"
    driver.get(URL)
    time.sleep(3) 
    try:
        driver.switch_to_frame('gdpr-consent-notice') # This is the id of the frame
        accept_cookies_button = driver.find_element(by=By.XPATH, value='//*[@id="save"]')
        accept_cookies_button.click()
        time.sleep(1)
    except AttributeError: # If you have the latest version of Selenium, the code above won't run because the "switch_to_frame" is deprecated
        driver.switch_to.frame('gdpr-consent-notice') # This is the id of the frame
        accept_cookies_button = driver.find_element(by=By.XPATH, value='//*[@id="save"]')
        accept_cookies_button.click()
        time.sleep(1)

    except:
        pass

    return driver 

# %%
def get_links(driver: webdriver.Chrome) -> list:
    '''
    Returns a list with all the links in the current page
    Parameters
    ----------
    driver: webdriver.Chrome
        The driver that contains information about the current page
    
    Returns
    -------
    link_list: list
        A list with all the links in the page
    '''

    prop_container = driver.find_element(by=By.XPATH, value='//div[@class="css-1itfubx e1uxczc30"]')
    prop_list = prop_container.find_elements(by=By.XPATH, value='./div')
    link_list = []

    for house_property in prop_list:
        a_tag = house_property.find_element(by=By.TAG_NAME, value='a')
        link = a_tag.get_attribute('href')
        link_list.append(link)

    return link_list

# %%
big_list = []
driver = load_and_accept_cookies()

## Get the next button
next_property= driver.find_element(by=By.XPATH, value='//li[@class="css-qhg1xn-PaginationItemPreviousAndNext-PaginationItemNext eaoxhri2"]')
next_tag = next_property.find_element(by=By.TAG_NAME, value='a')
next_button = next_tag.get_attribute('href')


"""
With the new acquired knowledge, extract the data from all the properties in 5 different Zoopla pages. 
This means that, once you finish scraping a page, you have to click the 'Next Page' button (you can also change the URL if you know how to tweak it). 
So, once you extract the 25 links, you can go to the next page by clicking 'Next':

"""
# %%

for i in range(5): # The first 5 pages only
    big_list.extend(get_links(driver)) # Call the function we just created and extend the big list with the returned list
    ## TODO: Click the next button. Don't forget to use sleeps, so the website doesn't suspect
    time.sleep(3)
    driver.get(next_button)

# %%
len(big_list)

# %%
dict_properties = {'Price': [], 'Address': [], 'Bedrooms': [], 'Description': []}
for link in big_list:
    driver.get(link)
    price = driver.find_element(by=By.XPATH, value='//p[@data-testid="price"]').text
    dict_properties['Price'].append(price)
    address = driver.find_element(by=By.XPATH, value='//address[@data-testid="address-label"]').text
    dict_properties['Address'].append(address)
    bedrooms = driver.find_element(by=By.XPATH, value='//div[@class="c-PJLV c-PJLV-iiNveLf-css"]').text
    dict_properties['Bedrooms'].append(bedrooms)
    div_tag = driver.find_element(by=By.XPATH, value='//div[@data-testid="truncated_text_container"]')
    span_tag = div_tag.find_element(by=By.XPATH, value='.//span')
    description = span_tag.text
    dict_properties['Description'] = description
    time.sleep(3)

# %%
driver.quit() # Close the browser when you finish
# %%
driver.get(next_button)
# %%
big_list
# %%
dict_properties
# %%
#### Build a selenium class

class lescraper:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome()

    def go_to_url(self):
        self.driver.get(self.url)

    def deny_the_cookies(self):
        cookie_banner = self.driver.find_element(by=By.XPATH, value='//div[@class="ConsentBanner"]')

        cookie_decline = cookie_banner.find_element(by=By.XPATH, value='//*[@class="BtnPair__RejectBtn"]')

        cookie_decline.click()

    def sign_in(self, username, password):

        ## select the signin option from the hamburger menu / hidden menu
        hamburger = self.driver.find_element(by=By.XPATH, value='//div[@class="HiddenMenu__HideLargeShow-sc-2fn5tp-0 rkmhM"]')
        hamburger.click()

        time.sleep(2)
        sign_in = self.driver.find_element(by=By.XPATH, value='//div[@data-selenium="user-menu-signin-button-container"]')
        si_button = self.driver.find_element(by=By.XPATH, value='//button[@class="Buttonstyled__ButtonStyled-sc-5gjk6l-0 brUBl"]')
        si_button.click()

        ## enter a username
        delay = 2
        WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@title="Universal login"]')))
        print("Frame Ready!")
        self.driver.switch_to.frame(self.driver.find_element(by=By.XPATH, value='//*[@title="Universal login"]'))
        time.sleep(2)
        email_input = self.driver.find_element(by=By.XPATH, value='//input[@id="email"]')
        email_input.click()
        email_input.send_keys(username)

        ## enter a password
        password_input = self.driver.find_element(by=By.XPATH, value='//input[@id="password"]')
        password_input.click()
        password_input.send_keys(password)

        time.sleep(2)    
        ## sign in with creds
        sign_in_button = self.driver.find_element(by=By.XPATH, value='//button[@class="sc-fzoiQi hsJTpM"]')
        sign_in_button.click()


    def get_hotels_data(self):
        hotel_dict = {'Hotel': [], 'Address': [], 'Price': [], 'url' :[]}

        ## agoda pages have infinite scroll

        ## get initial scroll height

        last_height = self.driver.execute_script("return document.body.scrollHeight")   

        ## 
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            hotel_container = self.driver.find_element(by=By.XPATH, value='//div[@id="contentContainer"]')
            hotel_list = hotel_container.find_elements(by=By.XPATH, value='//h3[@data-selenium="hotel-name"]')
            hotel_prices = hotel_container.find_elements(by=By.XPATH, value='//span[@class="PropertyCardPrice__Value"]')
            hotel_addresses = hotel_container.find_elements(by=By.XPATH, value='//span[@class="sc-dlfnbm sc-hKgILt eBEczI fdmzSj sc-pFZIQ gbgfMs"]')
            #rating_container = self.driver.find_element(by=By.XPATH, value='//div[@class="Box-sc-kv6pi1-0 ggePrW"]')
            #ratings = rating_container.find_elements(by=By.XPATH, value='//p[@class="Typographystyled__TypographyStyled-sc-j18mtu-0 Hkrzy kite-js-Typography "]')
            urls = self.driver.find_elements(by=By.XPATH, value='//a[@class="PropertyCard__Link"]')
            for i in range(len(hotel_list)):
                hotel_dict['Hotel'].append(hotel_list[i].text)
                hotel_dict['Address'].append(hotel_addresses[i].text)
                hotel_dict['Price'].append(hotel_prices[i].text)
                #hotel_dict['AvgRating'].append(ratings[i].text)
                hotel_dict['url'].append(urls[i].get_attribute('href'))


            time.sleep(2)

        ## calculate new scroll height and compare to old
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                try:
                    self.driver.find_element(by=By.XPATH, value='//button[@class="btn pagination2__next"]').click()
                except NoSuchElementException:
                    break
            last_height = new_height
            

        return hotel_dict

    def quit_scraping(self):
        self.driver.quit()


    
# %%
agoda = lescraper(url='https://www.agoda.com/en-gb/search?city=9023&checkIn=2023-05-09&los=7&rooms=1&adults=2&children=1&childages=7&cid=1844104&locale=en-gb&ckuid=95581d02-61ef-4bd2-99e3-a16577324135&prid=0&currency=GBP&correlationId=4e535957-d2d0-468d-8f96-f6c17b4ae3e4&pageTypeId=1&realLanguageId=16&languageId=1&origin=GB&userId=95581d02-61ef-4bd2-99e3-a16577324135&whitelabelid=1&loginLvl=0&storefrontId=3&currencyId=2&currencyCode=GBP&htmlLanguage=en-gb&cultureInfoName=en-gb&machineName=am-pc-4g-acm-web-user-7cd56857bc-27dfk&trafficGroupId=1&sessionId=0rpc5l4grjcqf4nvz3snwdfc&trafficSubGroupId=84&aid=130589&useFullPageLogin=true&cttp=4&isRealUser=true&mode=production&browserFamily=Chrome&checkOut=2023-05-16&priceCur=GBP&textToSearch=Vancouver%20(BC)&travellerType=2&familyMode=off&productType=-1')
# %%
agoda.go_to_url()

# %%
agoda.deny_the_cookies()
# %%
agoda.sign_in(username="rupert.m.coghlan@gmail.com", password="newzeafra83!")

# %%
dict3 = agoda.get_hotels_data()