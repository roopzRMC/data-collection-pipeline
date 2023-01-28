# %%
from selenium import webdriver 
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
import time

# %%
driver.get("https://www.zoopla.co.uk/")

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
house_property = driver.find_element(by=By.XPATH, value='//*[@id="listing_63357276"]') # Change this xpath with the xpath the current page has in their properties
a_tag = house_property.find_element(by=By.TAG_NAME, value='a')
link = a_tag.get_attribute('href')
print(link)
driver.get(link)
# %%
## get listing listing_63349097


# %%
price_element = driver.find_element(by=By.XPATH, value='//p[@data-testid="price"').text

# %%
driver
# %%
