from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time

class AgodaScraper:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Remote('http://172.17.0.2:4444/wd/hub', webdriver.DesiredCapabilities.CHROME)
        self.go_to_url()
        #self.vancouver_data = self.get_hotels_data()
        #self.quit_scraping()


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
            hotel_addresses = hotel_container.find_elements(by=By.XPATH, value='//span[@class="sc-iBPRYJ sc-fubCfw dyNXNh hZNSEN sc-pFZIQ gbgfMs"]')
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

if __name__ == '__main__':
    AgodaScraper().main()
