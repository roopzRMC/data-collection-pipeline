# %%
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time


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
    print(i)
    image_links.append()
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

## Function for hotel details
def get_hotel_data(url):
    driver = webdriver.Chrome()
    driver.get(url)

    time.sleep(4)

    ## Get name
    hotel_name = driver.find_element(by=By.XPATH, value = '//h1[@class="HeaderCerebrum__Name"]')


    ## Get description
    #description_container = driver.find_element(by=By.XPATH, value='//div[@class="Box-sc-kv6pi1-0 leAmQV"]')
    #description = description_container.find_element(by=By.XPATH, value = '//p[@class="Typographystyled__TypographyStyled-sc-j18mtu-0 fHvoAu kite-js-Typography "]')

    ## Get images
    images_container = driver.find_element(by=By.XPATH, value='//div[@class="Box-sc-kv6pi1-0 kCNWwO Mosaic"]')
    images = images_container.find_elements(by=By.XPATH, value='//img[@class="SquareImage"]')
    image_links = []
    for i in range(len(images)):
        image_links.append(images[i].get_attribute('src'))

    
    ## Get facilities
    facilities = driver.find_elements(by=By.XPATH, value = '//div[@data-element-name="facility-highlights-item"]')
    facilities_list = []
    for j in range(len(facilities)):
        facilities_list.append(facilities[j].text)


    hotel_dict = {'Hotel_Name': hotel_name.text, 'Images': image_links, 'Facilities' : facilities_list}

    return hotel_dict
# %%

myhotel = get_hotel_data(url)
# %%
myhotel
# %%
