
from selenium_agodascraper_container.AgodaDetailsScraper import AgodaDetailsScraper
from selenium_agodascraper_container.AgodaScaper import AgodaScraper

print(f'This is testing the hotel scraper for vancouver hotels')


myurl='https://www.agoda.com/en-gb/search?city=9023&checkIn=2023-05-09&los=7&rooms=1&adults=2&children=1&childages=7&cid=1844104&locale=en-gb&ckuid=95581d02-61ef-4bd2-99e3-a16577324135&prid=0&currency=GBP&correlationId=4e535957-d2d0-468d-8f96-f6c17b4ae3e4&pageTypeId=1&realLanguageId=16&languageId=1&origin=GB&userId=95581d02-61ef-4bd2-99e3-a16577324135&whitelabelid=1&loginLvl=0&storefrontId=3&currencyId=2&currencyCode=GBP&htmlLanguage=en-gb&cultureInfoName=en-gb&machineName=am-pc-4g-acm-web-user-7cd56857bc-27dfk&trafficGroupId=1&sessionId=0rpc5l4grjcqf4nvz3snwdfc&trafficSubGroupId=84&aid=130589&useFullPageLogin=true&cttp=4&isRealUser=true&mode=production&browserFamily=Chrome&checkOut=2023-05-16&priceCur=GBP&textToSearch=Vancouver%20(BC)&travellerType=2&familyMode=off&productType=-1'

agoda_scraper = AgodaScraper(myurl)

hotels = agoda_scraper.get_hotels_data()

print(f'scraped.... now displaying hotels scraped in dictionary form')

print(hotels)

print(f'Hotel list scraping complete')

print(f'Now testing hotel details scraper')

hotel_url = 'https://www.agoda.com/en-gb/hyatt-regency-vancouver/hotel/vancouver-bc-ca.html?finalPriceView=2&isShowMobileAppPrice=false&cid=1844104&numberOfBedrooms=&familyMode=false&adults=2&children=1&rooms=1&maxRooms=0&checkIn=2023-05-9&isCalendarCallout=false&childAges=7&numberOfGuest=0&missingChildAges=false&travellerType=2&showReviewSubmissionEntry=false&currencyCode=GBP&isFreeOccSearch=false&isCityHaveAsq=false&los=7&searchrequestid=0108ffcb-730c-4120-b463-c79a9971fa73'

details_scraper = AgodaDetailsScraper(hotel_url)

hotel_details = details_scraper.get_hotel_metadata()

print(f'showing hotel details scraped')

print(hotel_details)