import unittest
import sys
sys.path.append('data-collection-pipeline')
from agodascraper.AgodaScaper import AgodaScraper
from agodascraper.AgodaDetailsScraper import AgodaDetailsScraper


class ScraperTestCase(unittest.TestCase):
    def test_data_scraped(self):
        test_url = 'https://www.agoda.com/en-gb/search?city=9023&checkIn=2023-05-09&los=7&rooms=1&adults=2&children=1&childages=7&cid=1844104&locale=en-gb&ckuid=95581d02-61ef-4bd2-99e3-a16577324135&prid=0&currency=GBP&correlationId=4e535957-d2d0-468d-8f96-f6c17b4ae3e4&pageTypeId=1&realLanguageId=16&languageId=1&origin=GB&userId=95581d02-61ef-4bd2-99e3-a16577324135&whitelabelid=1&loginLvl=0&storefrontId=3&currencyId=2&currencyCode=GBP&htmlLanguage=en-gb&cultureInfoName=en-gb&machineName=am-pc-4g-acm-web-user-7cd56857bc-27dfk&trafficGroupId=1&sessionId=0rpc5l4grjcqf4nvz3snwdfc&trafficSubGroupId=84&aid=130589&useFullPageLogin=true&cttp=4&isRealUser=true&mode=production&browserFamily=Chrome&checkOut=2023-05-16&priceCur=GBP&textToSearch=Vancouver%20(BC)&travellerType=2&familyMode=off&productType=-1'
        testscraper = AgodaScraper(test_url)
        test_dict = testscraper.get_hotels_data()
        testscraper.quit_scraping()
        self.assertGreater(sum(len(v) for v in test_dict.values()), 1)
    
    def test_price_data_quality(self):
        test_url = 'https://www.agoda.com/en-gb/search?city=9023&checkIn=2023-05-09&los=7&rooms=1&adults=2&children=1&childages=7&cid=1844104&locale=en-gb&ckuid=95581d02-61ef-4bd2-99e3-a16577324135&prid=0&currency=GBP&correlationId=4e535957-d2d0-468d-8f96-f6c17b4ae3e4&pageTypeId=1&realLanguageId=16&languageId=1&origin=GB&userId=95581d02-61ef-4bd2-99e3-a16577324135&whitelabelid=1&loginLvl=0&storefrontId=3&currencyId=2&currencyCode=GBP&htmlLanguage=en-gb&cultureInfoName=en-gb&machineName=am-pc-4g-acm-web-user-7cd56857bc-27dfk&trafficGroupId=1&sessionId=0rpc5l4grjcqf4nvz3snwdfc&trafficSubGroupId=84&aid=130589&useFullPageLogin=true&cttp=4&isRealUser=true&mode=production&browserFamily=Chrome&checkOut=2023-05-16&priceCur=GBP&textToSearch=Vancouver%20(BC)&travellerType=2&familyMode=off&productType=-1'
        testscraper = AgodaScraper(test_url)
        test_dict = testscraper.get_hotels_data()
        testscraper.quit_scraping()
        self.assertEqual((test_dict['Price'][0]).isnumeric(), True)
        
unittest.main(argv=[''], verbosity=2, exit=False)