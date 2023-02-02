# Data Collection Pipeline
> Using Selenium

The web driver must be downloaded and then moved to one of the appropriate paths found here 

```
echo $PATH
```
The art to selenium is ensuring that you have determined
* The container for the element you are looking to scrape
OR
* the iframe that contains some element you need to click on eg - deny cookies or a sign in page

## Finding a container of elements

First, initialise the driver and specify the url, this will start the browser in an automated mode

```
driver = webdriver.Chrome() 
URL = "https://www.zoopla.co.uk"
driver.get(URL)

```

Using the developer tools try to isolate the container (generally a div tag) that is likely to contain all the elements or that is repeated

### Finding a container

```
driver.find_element(by=By.XPATH, value='//*[@id="save"]')
## leveraging the value argument can either do a wild card search based on an id or class name OR

driver.find_element(by=By.XPATH, value='//li[@class="css-qhg1xn-PaginationItemPreviousAndNext-PaginationItemNext eaoxhri2"]')
## this specifies both a tag and a class id
```

Within the parent container you can find an element or an attribute

```
next_tag = next_property.find_element(by=By.TAG_NAME, value='a')
next_button = next_tag.get_attribute('href')

```

## Switching to an iFrame

You need to use a ```.switch_to.frame()``` method on driver to switch to an iframe. It is highly recommend to then sleep for 2 seconds before eg inputting information

## Inputting data
Locate the element which contains the field, use the click method and send keys to input a series of values

```
        email_input = self.driver.find_element(by=By.XPATH, value='//input[@id="email"]')
        email_input.click()
        email_input.send_keys(username)

```

## Scrolling
If a page does not have infinite scroll the following code will scroll to the bottom of the page

```
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

```
Dealing with infinite scrolling requires a while loop as you do not as yet know how far down the page will reach

```
## get initial scroll height after first scroll

last_height = driver.execute_script("return document.body.scrollHeight")   

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    ## add scraping code here
    ## get the current height as new_height:
    new_height = driver.execute_script("return document.body.scrollHeight")

    ## if after scrolling its the same as before - break
    if new_height == last_height:
    
        ## this is where you can insert a try except to see if there is a next button to press
        try:
            self.driver.find_element(by=By.XPATH, value='//button[@class="btn pagination2__next"]').click()
        except NoSuchElementException:
            
            break
    ## otherwise set the last height as the last new_height and loop again
    last_height = new_height
```

Note, you must make sure you import even the errors you wish to raise

```
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time
```

> Getting Detailed Hotels data

Leveraging the ``` import os ``` library and combining it with the hotel name allowed for a dynamic creation of a folder name

Using ``` os.makedirs('raw_data') ``` created a folder to contain raw data. Within this ``` os.chdir('raw_data') ``` then ``` os.makedirs('hotel_name.text') ``` having already extracted the hotel name from the h1 class scraped via selenium

### Getting Images

Retrieving images requires importing the ``` urllib.request ``` module

```
## Find the images container
   images_container = driver.find_element(by=By.XPATH, value='//div[@class="Box-sc-kv6pi1-0 kCNWwO Mosaic"]')
## FIne the image elements 
    images = images_container.find_elements(by=By.XPATH, value='//img[@class="SquareImage"]')

## Instantiate an empty list object to extract the images too
    image_links = []
    for i in range(len(images)):
        image_links.append(images[i].get_attribute('src'))

```

Using the OS library, a new directory (images) is created

Using the ``` try except ``` approach allows us to detect whether this dir exists already, if not it does not try to overwrite and instead we change directories to enter this new dir 

A new for loop is initiated to extract the urls via the urls in the image list

```
 for i in range(len(image_links)):
        urllib.request.urlretrieve(image_links[i].split('?', 1)[0], str(str(datetime.now()) + '.jpg'))

```
Each image is saved with the current timestamp of extraction with the jpg file ext. It was necessary to split the url link before the ? to ensure the image was sourced correctly

> Dumping the hotel details contents to a JSON

Collecting the data from an individual hotel in a dictionary format means it can be easily resturctured to a JSON

Use a context manager and the JSON library, we can dump the contents of the dictionary with the structure intact 

```
with open(str(hotel_name.text+'.json'), 'w') as outfile:
    json.dump(myhotel, outfile)
outfile.close()


```
> Unit Testing The Scraper

### AgodaScraper (multiple hotels)

There are 2 unit tests of this class

```
test_data_scraped()
test_price_data_quality()
```

```test_data_scraped()``` tests that the dictionary that is eventually parsed as a JSON file is not empty by checking that the of sum of the dictionary's value lengths is greater than 1

```test_price_quality_data()``` tests that the string values of the price values within the dictionary are actually numeric

### AgodaDetailsScraper (hotel deepdive)

There is 1 unit test of this class

```
test_hotel_facilities()
```

This tests that the facilities dictionary has a series of values greater than 2 to ensure that the relevant hotels have been scraped

### Leveraging Docker Selenium Image

port forwarding via ssh to a virtual machine should be in the form below

```
gcloud compute ssh --ssh-flag="-L 4444:localhost:4444" --zone "europe-west2-c" "docker-test"  --project "aicore-study"

```

### Issues with ARM based macs and selenium docker images

It was necessary for a VM to be spun up using x486 architecture as the selenium image does not cater for arm archiecture

### Preparing Docker on an ubuntu Virtual Machine

Docker Engine needs to be installed via these instructions https://docs.docker.com/engine/install/ubuntu/

Once installed, ensure docker has the correct sudo permissions ``` sudo usermod -a -G docker $USER```

### Pulling Selenium from Docker and Running

To pull the chromedriver version of selenium type

```
docker pull selenium/standalone-chrome 

```

To ensure you are portforwarding correctly run the image as per 

```

docker run -d -p 4444:4444 --shm-size=2g selenium/standalone-chrome:latest
```

Assuming that you have ssh'd in to the virtual machine port forwarding to 4444 you can log in to the selenium server on the browser by going to localhost:4444. Ensure that you note down the ip address that the selenium server running on.

This ip address with correct port must be hardcoded to the webdriver.remote method in the class in the scraper

```
class AgodaScraper:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Remote('http://172.17.0.2:4444/wd/hub', webdriver.DesiredCapabilities.CHROME)
        self.go_to_url()
        #self.vancouver_data = self.get_hotels_data()
        #self.quit_scraping()


```

### Creating the scraper dockerfile

The dockerfile leverage python 3.10 and install the chrome driver on an ubuntu imaged machine

The dockerfile references a requirements txt file which specifies the need for 

* selenium
* requests
* webdriver-manager

to be installed using pip

The CMD statement runs the run_scrapers.py which trigger the scraper python files


## CI/CD Pipeline

The CI/CD pipelines consists of a github action located in ```.github/workflows``` directory and is found in the ```push_to_docker.yaml``` file

The github action is configured to run on a push to the main branch only

On pushing to main, the following actions are automated;

* repo is checked out
* docker is logged in to via the username and password secrets stored as github secrets
* the docker image is republished to the private repository



