# %%
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time
from datetime import datetime
import urllib.request
import os
import json

## Determine which elements to scrape from individual hotel page
# %%
driver = webdriver.Chrome()
url='https://www.agoda.com/en-gb/century-plaza-hotel-spa_3/hotel/vancouver-bc-ca.html?finalPriceView=2&isShowMobileAppPrice=false&cid=1844104&numberOfBedrooms=&familyMode=false&adults=2&children=1&rooms=1&maxRooms=0&checkIn=2023-05-9&isCalendarCallout=false&childAges=7&numberOfGuest=0&missingChildAges=false&travellerType=2&showReviewSubmissionEntry=false&currencyCode=GBP&isFreeOccSearch=false&isCityHaveAsq=false&tspTypes=7,6,3&los=7&searchrequestid=efab119f-9b4e-4c5b-a9d1-eefe2b210837'
driver.get(url)
# %%
images_container = driver.find_element(by=By.XPATH, value='//div[@class="Box-sc-kv6pi1-0 kCNWwO Mosaic"]')
# %%
images = images_container.find_elements(by=By.XPATH, value='//img[@class="SquareImage"]')
# %%
image_links = []
for i in range(len(images)):
    image_links.append(images[i].get_attribute('src'))
# %%
description_container = driver.find_element(by=By.XPATH, value='//div[@class="Box-sc-kv6pi1-0 leAmQV"]')

# %%
description = description_container.find_element(by=By.XPATH, value = '//p[@class="Typographystyled__TypographyStyled-sc-j18mtu-0 fHvoAu kite-js-Typography "]')
# %%
description.text

# %%
hotel_name = driver.find_element(by=By.XPATH, value = '//h1[@class="HeaderCerebrum__Name"]')
hotel_name.text
# %%
facilities = driver.find_elements(by=By.XPATH, value = '//div[@data-element-name="facility-highlights-item"]')
# %%
len(facilities)
# %%
print(str(datetime.now()))

# %%
## Function for hotel details
def get_hotel_data(url):
    ## Initialise the drivers for selenium
    print(os.getcwd())

    driver = webdriver.Chrome()
    driver.get(url)

    time.sleep(4)

    scrape_time = str(datetime.now())

    ## Get name
    hotel_name = driver.find_element(by=By.XPATH, value = '//h1[@class="HeaderCerebrum__Name"]')
    ## Check for file structure
    raw_path = 'raw_data'

    try:
        os.makedirs(raw_path)
    except:
        FileExistsError
        print('directory already exists')

    os.chdir(raw_path)
    ## Checks whether existing hotel exists within raw data and creates directory if not already there
    try:
        os.makedirs(hotel_name.text)
    except:
        FileExistsError
        print('hotel directory already exists')
    os.chdir(hotel_name.text)

    ## Get description
    #description_container = driver.find_element(by=By.XPATH, value='//div[@class="Box-sc-kv6pi1-0 leAmQV"]')
    #description = description_container.find_element(by=By.XPATH, value = '//p[@class="Typographystyled__TypographyStyled-sc-j18mtu-0 fHvoAu kite-js-Typography "]')

    ## Get images
    images_container = driver.find_element(by=By.XPATH, value='//div[@class="Box-sc-kv6pi1-0 kCNWwO Mosaic"]')
    images = images_container.find_elements(by=By.XPATH, value='//img[@class="SquareImage"]')
    image_links = []
    for i in range(len(images)):
        image_links.append(images[i].get_attribute('src'))

    ## Download the images
    try:
        os.makedirs('images')
    except:
        FileExistsError
        print('image directory already exists')
    os.chdir('images')
    for i in range(len(image_links)):
        urllib.request.urlretrieve(image_links[i].split('?', 1)[0], str(str(datetime.now()) + '.jpg'))

    
    ## Get facilities
    facilities = driver.find_elements(by=By.XPATH, value = '//div[@data-element-name="facility-highlights-item"]')
    facilities_list = []
    for j in range(len(facilities)):
        facilities_list.append(facilities[j].text)


    #hotel_dict = {'Scrape Time': scrape_time, 'Hotel_Name': hotel_name.text, 'Images': image_links, 'Facilities' : facilities_list}

    #return hotel_dict
# %%

os.chdir('/Users/rupertcoghlan/data-collection-pipeline/')
url='https://www.agoda.com/en-gb/century-plaza-hotel-spa_3/hotel/vancouver-bc-ca.html?finalPriceView=2&isShowMobileAppPrice=false&cid=1844104&numberOfBedrooms=&familyMode=false&adults=2&children=1&rooms=1&maxRooms=0&checkIn=2023-05-9&isCalendarCallout=false&childAges=7&numberOfGuest=0&missingChildAges=false&travellerType=2&showReviewSubmissionEntry=false&currencyCode=GBP&isFreeOccSearch=false&isCityHaveAsq=false&tspTypes=7,6,3&los=7&searchrequestid=efab119f-9b4e-4c5b-a9d1-eefe2b210837'
myhotel = get_hotel_data(url)
# %%
myhotel
# %%


### 
## Creating a file structure

import os
import json
# %%
os.getcwd()
# %%
path = 'raw_data'

# %%
try:
    os.makedirs(path)
except:
    FileExistsError
    print('directory already exists')

# %%
os.chdir(path)
# %%
os.getcwd()
# %%

## CHecks whether existing hotel exists within raw data and creates directory if not already there
try:
    os.makedirs(hotel_name.text)
except:
    FileExistsError
    print('hotel directory already exists')
os.chdir(hotel_name.text)
# %%

## DUmps the results of the dictionary to the sub directory
with open(str(hotel_name.text+'.json'), 'w') as outfile:
    json.dump(myhotel, outfile)
outfile.close()

# %%
outfile.close()
# %%
str(hotel_name.text+'.json')
# %%
## 
# Get an image

import urllib.request

img_url = image_links[0].split('?', 1)[0]
print(img_url)
print(images[0].accessible_name)
# %%
os.getcwd()
# %%
## Store the image with datetime appended to the name
urllib.request.urlretrieve(img_url, str(str(datetime.now()) + '.jpg'))


# %%
# Function to create file structure


