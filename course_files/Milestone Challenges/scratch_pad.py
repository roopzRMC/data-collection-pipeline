# %%
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
driver = webdriver.Chrome() 

# %%
buttons = driver.find_elements(by=By.XPATH, value='//button')
# %%
buttons
# %%
type(buttons)
# %%
len(buttons)
# %%
driver = webdriver.Chrome() 
URL = "https://www.zoopla.co.uk/new-homes/property/london/?q=London&results_sort=newest_listings&search_source=new-homes&page_size=25&pn=1&view_type=list"
driver.get(URL)
time.sleep(2) # Wait a couple of seconds, so the website doesn't suspect you are a bot
try:
    driver.switch_to_frame('gdpr-consent-notice') # This is the id of the frame
    accept_cookies_button = driver.find_element(by=By.XPATH, value='//*[@id="save"]')
    accept_cookies_button.click()

except AttributeError: # If you have the latest version of Selenium, the code above won't run because the "switch_to_frame" is deprecated
    driver.switch_to.frame('gdpr-consent-notice') # This is the id of the frame
    accept_cookies_button = driver.find_element(by=By.XPATH, value='//*[@id="save"]')
    accept_cookies_button.click()

except:
    pass # If there is no cookies button, we won't find it, so we can pass
house_property = driver.find_element(by=By.XPATH, value='//*[@id="listing_63357506"]') # Change this xpath with the xpath the current page has in their properties
a_tag = house_property.find_element(by=By.TAG_NAME, value='a')
link = a_tag.get_attribute('href')
print(link)
driver.get(link)
# %%
## get listing listing_63349097


# %%
price = driver.find_element(by=By.XPATH, value='//p[@data-testid="price"]').text
print(price)
# %%
price = driver.find_element(by=By.XPATH, value='//p[@data-testid="price"]').text
print(price)
address = driver.find_element(by=By.XPATH, value='//address[@data-testid="address-label"]').text
print(address)
bedrooms = driver.find_element(by=By.XPATH, value='//div[@class="c-PJLV c-PJLV-iiNveLf-css"]').text
print(bedrooms)
div_tag = driver.find_element(by=By.XPATH, value='//div[@data-testid="truncated_text_container"]')
span_tag = div_tag.find_element(by=By.XPATH, value='.//span')
description = span_tag.text
print(description)
# %%
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

    prop_container = driver.find_element(by=By.XPATH, value='//div[@class="css-1itfubx e5pbze00"]')
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
print(next_button)

# %%

for i in range(5): # The first 5 pages only
    big_list.extend(get_links(driver)) # Call the function we just created and extend the big list with the returned list
    ## TODO: Click the next button. Don't forget to use sleeps, so the website doesn't suspect
    driver.get(next_button)


for link in big_list:
    ## TODO: Visit all the links, and extract the data. Don't forget to use sleeps, so the website doesn't suspect
    pass # This pass should be removed once the code is complete

driver.quit() # Close the browser when you finish


# %%
driver.quit()
# %%
#### Advanced selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get("http://www.python.org")
# %%
## Scroll to the bottom of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# %%
### Navigate to the search bar, enter method and then intiate search
search_bar = driver.find_element(by=By.XPATH, value='//*[@id="id-search-field"]')
search_bar.click()
# %%
search_bar.send_keys("method")
# %%
search_bar.send_keys(Keys.RETURN)
# %%
driver.quit()
# %%
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time

# %%
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
    delay = 10
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="gdpr-consent-notice"]')))
        print("Frame Ready!")
        driver.switch_to.frame('gdpr-consent-notice')
        accept_cookies_button = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="save"]')))
        print("Accept Cookies Button Ready!")
        accept_cookies_button.click()
        time.sleep(1)
    except TimeoutException:
        print("Loading took too much time!")

    return driver 
# %%
driver = load_and_accept_cookies()
# %%
driver.quit()
# %%
## adapting the code for agoda

agoda_url = 'https://www.agoda.com/en-gb/search?guid=47f34383-24c1-46ad-9021-0af74c576c77&asq=NQVGXW6jsE3tbdY9S%2BqUCpufa9Vwpz6XltTHq4n%2B9gPt6Sc9VYM%2BOtJvOdzFsuZ%2Fv0r02lkXGpWI%2BQOUTXHgW7KhS5oHpuGAHeLVos2dFZGi0q4kwKxmwzESZxdDAHGnYELE%2BI5n28g5rhlErwqNnHfmG1btJ4rXIGquB6HLlWNDUKJAPdRsuRqj1LTkzEh5gq1iGWzMVL9MJKP5Etw9U0A9ZvKqYuIH382Z5Xz4lVY%3D&city=9023&tick=638054630322&locale=en-gb&ckuid=95581d02-61ef-4bd2-99e3-a16577324135&prid=0&currency=GBP&correlationId=f3d934ca-3b17-4cc6-857c-e51bc5b88740&pageTypeId=1&realLanguageId=16&languageId=1&origin=GB&cid=1844104&userId=95581d02-61ef-4bd2-99e3-a16577324135&whitelabelid=1&loginLvl=0&storefrontId=3&currencyId=2&currencyCode=GBP&htmlLanguage=en-gb&cultureInfoName=en-gb&machineName=am-pc-4g-acm-web-user-7cd56857bc-9r5x2&trafficGroupId=1&sessionId=0rpc5l4grjcqf4nvz3snwdfc&trafficSubGroupId=84&aid=130589&useFullPageLogin=true&cttp=4&isRealUser=true&mode=production&browserFamily=Chrome&checkIn=2023-05-09&checkOut=2023-05-16&rooms=1&adults=2&children=1&childages=7&priceCur=GBP&los=7&textToSearch=Vancouver%20(BC)&occCheckboxType=1&travellerType=2&familyMode=off&productType=-1'
# %%
driver = webdriver.Chrome() 
driver.get(agoda_url)
# %%
### Navigate to hamburger
# hamburger - div class=HiddenMenu__HideLargeShow-sc-2fn5tp-0 rkmhM
# click on the div
# div data-selenium="user-menu-signin-button-container"
hamburger = driver.find_element(by=By.XPATH, value='//div[@class="HiddenMenu__HideLargeShow-sc-2fn5tp-0 rkmhM"]')
hamburger.click()

time.sleep(2)
sign_in = driver.find_element(by=By.XPATH, value='//div[@data-selenium="user-menu-signin-button-container"]')

# %%
si_button = driver.find_element(by=By.XPATH, value='//button[@class="Buttonstyled__ButtonStyled-sc-5gjk6l-0 brUBl"]')
# %%
si_button.click()

# %%
# %%
## enter user name
delay=2
WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@title="Universal login"]')))
print("Frame Ready!")
driver.switch_to.frame(driver.find_element(by=By.XPATH, value='//*[@title="Universal login"]'))
email_input = driver.find_element(by=By.XPATH, value='//input[@id="email"]')


#login_panel.find_elements(by=By.XPATH, value='//*[@id="email"]')
# %%

email_input.click()
# %%
email_input.send_keys("rupert.m.coghlan@gmail.com")
# %%
password_input = driver.find_element(by=By.XPATH, value='//input[@id="password"]')
password_input.click()
password_input.send_keys("newzeafra83!")
# %%

sign_in_button = driver.find_element(by=By.XPATH, value='//button[@class="sc-fzoiQi hsJTpM"]')
sign_in_button.click()

# %%
### Get hotels data

hotel_dict = {'Hotel': [], 'Address': [], 'Price': [], 'AvgRating': [], 'url' :[]}

# %%
hotel_container = driver.find_element(by=By.XPATH, value='//div[@id="contentContainer"]')
url_container = driver.find_element(by=By.XPATH, value='//div[@class="Box-sc-kv6pi1-0 hRUYUu JacketContent JacketContent--UnifiedJacket"]')
urls = url_container.find_elements(by=By.XPATH, value='//a[@class="PropertyCard__Link"]')
# %%
urls[1].get_attribute('href')
# %%
hotel_container
# %%
hotel_container = driver.find_element(by=By.XPATH, value='//div[@id="contentContainer"]')
hotel_list = hotel_container.find_elements(by=By.XPATH, value='//h3[@data-selenium="hotel-name"]')
hotel_prices = hotel_container.find_elements(by=By.XPATH, value='//span[@class="PropertyCardPrice__Value"]')
hotel_addresses = hotel_container.find_elements(by=By.XPATH, value='//span[@class="sc-dlfnbm sc-hKgILt eBEczI fdmzSj sc-pFZIQ gbgfMs"]')
rating_container = driver.find_element(by=By.XPATH, value='//div[@class="Box-sc-kv6pi1-0 ggePrW"]')
ratings = rating_container.find_elements(by=By.XPATH, value='//p[@class="Typographystyled__TypographyStyled-sc-j18mtu-0 Hkrzy kite-js-Typography "]')
urls = driver.find_elements(by=By.XPATH, value='//a[@class="PropertyCard__Link"]')

for i in range(len(hotel_list)):
    hotel_dict['Hotel'].append(hotel_list[i].text)
    hotel_dict['Address'].append(hotel_addresses[i].text)
    hotel_dict['Price'].append(hotel_prices[i].text)
    hotel_dict['AvgRating'].append(ratings[i].text)
    hotel_dict['url'].append(urls[i].get_attribute('href'))
# %%
print(hotel_list[1].text)
print(hotel_addresses[1].text)
print(ratings[1].text)
print(hotel_prices[1].text)
print(urls[1].get_attribute('href'))

# %%
hotel_dict
# %%
## Captcha frame switch
WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@title="reCAPTCHA"]')))
print("Frame Ready!")
driver.switch_to.frame(driver.find_element(by=By.XPATH, value='//*[@title="reCAPTCHA"]'))

# %%
driver.find_element(by=By.XPATH, value='//div[@class="rc-anchor rc-anchor-normal rc-anchor-light"]')
# %%
check_box = driver.find_element(by=By.XPATH, value='//span[@id="recaptcha-anchor"]')

check_box.click()
# %%
## agoda pages have infinite scroll

## get initial scroll height

last_height = driver.execute_script("return document.body.scrollHeight")

## 
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

## calculate new scroll height and compare to old
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# %%
## get next button
next_button = driver.find_element(by=By.XPATH, value='//button[@class="btn pagination2__next"]')
# %%
next_button.click()
# %%
cookie_banner = driver.find_element(by=By.XPATH, value='//div[@class="ConsentBanner"]')

cookie_decline = cookie_banner.find_element(by=By.XPATH, value='//*[@class="BtnPair__RejectBtn"]')
# %%
print(cookie_decline)
# %%
cookie_decline.click()
# %%
driver.quit()
# %%
## testing with trip advisor
driver = webdriver.Chrome() 

# %%
driver.get('https://www.tripadvisor.co.uk/')
# %%
driver.quit()
# %%

import re

replacements = {" ": "", "-": ""}

# %%
replacements = dict((re.escape(k), v) for k, v in replacements.items()) 

# %%
pattern = re.compile("|".join(replacements.keys()))
# %%
pattern
# %%
test = 'RC-black shoes'

text = pattern.sub(lambda m: replacements[re.escape(m.group(0))], test)

# %%
text
# %%
from collections import defaultdict
s = defaultdict()
# %%
s
# %%
s.items()
# %%
s.keys == None
# %%
len(s.keys())
# %%
from example.product import Product
from example.cart import ShoppingCart

# %%
test_cart = ShoppingCart()
small_blue_shoes = Product('shoes', 'S', 'blue')

# %%
product = Product(small_blue_shoes.generate_sku())
# %%

#tests that, after adding a product to the cart, cart.products will be equal to a dictionary like this: {'SHOES-S-BLUE': {'quantity': 1}}
test_cart = ShoppingCart()
small_blue_shoes = Product('shoes', 'S', 'blue')
test_cart.add_product(small_blue_shoes)
test_dict = {'Shoes-S-Blue': {'quantity': 1}}
# %%
test_cart.products
# %%
small_blue_shoes.generate_sku()
# %%
