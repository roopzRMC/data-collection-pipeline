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