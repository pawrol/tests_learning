import logging
import allure
from allure_commons.types import AttachmentType


class ResultSearchHotel:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.hotels_names_xpath = "//h4[contains(@class,'list_title')]//b"
        self.prices_xpath = "//div[contains(@class,'price_tab')]//b"

    @allure.step("results")
    def list_hotels(self):
        hotels = self.driver.find_elements_by_xpath(self.hotels_names_xpath)
        names = [hotel.get_attribute('textContent') for hotel in hotels]
        self.logger.info("Available hotels are: ")
        allure.attach(self.driver.get_screenshot_as_png(), name="results", attachment_type=AttachmentType.PNG)
        for name in names:
            self.logger.info(name)
        return names

    def list_prices(self):
        prices = self.driver.find_elements_by_xpath(self.prices_xpath)
        prices_list =  [cost.get_attribute('textContent') for cost in prices]
        self.logger.info("Prices are: ")
        for price in prices_list:
            self.logger.info(price)
        return prices_list