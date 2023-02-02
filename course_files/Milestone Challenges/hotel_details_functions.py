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

os.getcwd()
# %%

url = 'https://www.agoda.com/en-gb/century-plaza-hotel-spa_3/hotel/vancouver-bc-ca.html?finalPriceView=2&isShowMobileAppPrice=false&cid=1844104&numberOfBedrooms=&familyMode=false&adults=2&children=1&rooms=1&maxRooms=0&checkIn=2023-05-9&isCalendarCallout=false&childAges=7&numberOfGuest=0&missingChildAges=false&travellerType=2&showReviewSubmissionEntry=false&currencyCode=GBP&isFreeOccSearch=false&isCityHaveAsq=false&tspTypes=7,6,3&los=7&searchrequestid=efab119f-9b4e-4c5b-a9d1-eefe2b210837'

def get_hotel_images():
    ## Get images
    driver = webdriver.Chrome()
    url='https://www.agoda.com/en-gb/century-plaza-hotel-spa_3/hotel/vancouver-bc-ca.html?finalPriceView=2&isShowMobileAppPrice=false&cid=1844104&numberOfBedrooms=&familyMode=false&adults=2&children=1&rooms=1&maxRooms=0&checkIn=2023-05-9&isCalendarCallout=false&childAges=7&numberOfGuest=0&missingChildAges=false&travellerType=2&showReviewSubmissionEntry=false&currencyCode=GBP&isFreeOccSearch=false&isCityHaveAsq=false&tspTypes=7,6,3&los=7&searchrequestid=efab119f-9b4e-4c5b-a9d1-eefe2b210837'
    driver.get(url)
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

def get_hotel_metadata(url):
    driver = webdriver.Chrome()
    url='https://www.agoda.com/en-gb/century-plaza-hotel-spa_3/hotel/vancouver-bc-ca.html?finalPriceView=2&isShowMobileAppPrice=false&cid=1844104&numberOfBedrooms=&familyMode=false&adults=2&children=1&rooms=1&maxRooms=0&checkIn=2023-05-9&isCalendarCallout=false&childAges=7&numberOfGuest=0&missingChildAges=false&travellerType=2&showReviewSubmissionEntry=false&currencyCode=GBP&isFreeOccSearch=false&isCityHaveAsq=false&tspTypes=7,6,3&los=7&searchrequestid=efab119f-9b4e-4c5b-a9d1-eefe2b210837'
    driver.get(url)

    raw_path = 'raw_data'

    try:
        os.makedirs(raw_path)
    except:
        FileExistsError
        print('raw data directory already exists')

    os.chdir(raw_path)

    ## Get current time
    scrape_time = str(datetime.now())

    ## Get hotel name
    hotel_name = driver.find_element(by=By.XPATH, value = '//h1[@class="HeaderCerebrum__Name"]')
    hotel_name.text

    ## Check and create top level file structure
    print(f'your current directory is {os.getcwd()}')


    try:
        os.makedirs(hotel_name.text)
    except:
        FileExistsError
        print('hotel directory already exists')
    os.chdir(hotel_name.text)   

    ## Get facilities
    facilities = driver.find_elements(by=By.XPATH, value = '//div[@data-element-name="facility-highlights-item"]')
    facilities_list = []
    for facility in range(len(facilities)):
        facilities_list.append(facilities[facility].text)   
    
    ## Get description
    description = driver.find_element(by=By.XPATH, value = '//p[@class="Typographystyled__TypographyStyled-sc-j18mtu-0 fHvoAu kite-js-Typography "]')

    hotel_dict = {'Scrape Time': scrape_time, 'Hotel_Name': hotel_name.text, 'Description': description.text, 'Facilities' : facilities_list}

    with open(str(hotel_name.text+'.json'), 'w') as outfile:
        json.dump(hotel_dict, outfile)
    outfile.close()

    print(f'dictionary creation complete, END OF LINE')



# %%

        


# %%
get_hotel_metadata(url)
# %%
### Next steps

"""

Get file structure working

Add images function

add name is main
"""