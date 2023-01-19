# %%
from tests.scraper_unit_test import ScraperTestCase
from tests.scraperdetails_unit_test import ScraperDetailsTestCase

# %%

scraper_test = ScraperTestCase()

scraper_test.test_data_scraped()

scraper_test.test_price_data_quality()

scraper_details_test = ScraperDetailsTestCase()

scraper_details_test.test_hotel_facilities()
# %%
