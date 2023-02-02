'''
This is a class to scrape hotel metadata from the agoda website

Details retrieved are;
    Hotel Name
    Hotel description
    Hotel facilities
    Hotel thumbnail images

The class creates a folder structure to store the metadata in a JSON dict and the images in an image folder

'''
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


class AgodaDetailsScraper:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome()

    def get_hotel_metadata(self):
        """
        Retrieves key individual hotel metadata

        Takes the url supplied in the class instantiation.
        It scrapes the hotel name, description, facilities.
        These elements are output to a dictionary.
        The dictionary is dumped to a json in a folder named after the hotel
        """


        os.getcwd()
        self.driver.get(self.url)

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
        hotel_name = self.driver.find_element(by=By.XPATH, value = '//h1[@class="HeaderCerebrum__Name"]')
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
        facilities = self.driver.find_elements(by=By.XPATH, value = '//div[@data-element-name="facility-highlights-item"]')
        facilities_list = []
        for facility in range(len(facilities)):
            facilities_list.append(facilities[facility].text)   
        
        ## Get description
        description = self.driver.find_element(by=By.XPATH, value = '//p[@class="Typographystyled__TypographyStyled-sc-j18mtu-0 fHvoAu kite-js-Typography "]')

        hotel_dict = {'Scrape Time': scrape_time, 'Hotel_Name': hotel_name.text, 'Description': description.text, 'Facilities' : facilities_list}

        with open(str(hotel_name.text+'.json'), 'w') as outfile:
            json.dump(hotel_dict, outfile)
        outfile.close()

        print(f'dictionary creation complete, END OF LINE')

    def get_hotel_images(self):
        """
        Retrieves hotel images from details pages as specified by class url.

        Images are saves as jpgs, with scraped timestamp in images folder
        """
        ## Get images
        images_container = self.driver.find_element(by=By.XPATH, value='//div[@class="Box-sc-kv6pi1-0 kCNWwO Mosaic"]')
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

if __name__ == '__main__':
    AgodaDetailsScraper().main()

