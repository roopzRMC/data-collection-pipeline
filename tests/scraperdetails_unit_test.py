import unittest
from agodascraper.AgodaDetailsScraper import AgodaDetailsScraper


class ScraperDetailsTestCase(unittest.TestCase):
    def test_hotel_facilities(self):
        test_url = 'https://www.agoda.com/en-gb/hyatt-regency-vancouver/hotel/vancouver-bc-ca.html?finalPriceView=2&isShowMobileAppPrice=false&cid=1844104&numberOfBedrooms=&familyMode=false&adults=2&children=1&rooms=1&maxRooms=0&checkIn=2023-05-9&isCalendarCallout=false&childAges=7&numberOfGuest=0&missingChildAges=false&travellerType=2&showReviewSubmissionEntry=false&currencyCode=GBP&isFreeOccSearch=false&isCityHaveAsq=false&los=7&searchrequestid=0108ffcb-730c-4120-b463-c79a9971fa73'
        testscraper = AgodaDetailsScraper(test_url)
        test_dict = testscraper.get_hotel_metadata()
        self.assertGreater(sum(len(v) for v in test_dict.values()), 2)

unittest.main(argv=[''], verbosity=2, exit=False)