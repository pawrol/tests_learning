import logging
import allure
from allure_commons.types import AttachmentType


class SearchHotelPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)           #definiuje loga z pyterst.ini
        self.search_hotel_span_xpath = "//span[text()='Search by Hotel or City Name']"
        self.search_hotel_input_xpath = "//div[@id='select2-drop']//input"
        self.location_match_xpath = "//span[text()='Dubai']"
        self.check_in_input_name = "checkin"
        self.check_out_input_name = "checkout"
        self.travellers_input_id = "travellersInput"
        self.adult_input_id = "adultInput"
        self.child_input_id = "childInput"
        self.search_button_xpath = "//button[text()=' Search']"

    @allure.step("Setting city name to '{1}'")                  #1 zamienia sie w parametr city
    def set_city(self, city):
        self.logger.info("Setting city {}".format(city))
        self.driver.find_element_by_xpath(self.search_hotel_span_xpath).click()
        self.driver.find_element_by_xpath(self.search_hotel_input_xpath).send_keys(city)
        self.driver.find_element_by_xpath(self.location_match_xpath).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="set_city", attachment_type=AttachmentType.PNG)            # screenshot

    @allure.step("Setting date range from '{1}' to '{2}'")
    def set_date(self, checkin, checkout):
        self.logger.info("Setting check in {checkin} and {checkout} dates".format(checkin=checkin, checkout=checkout))
        self.driver.find_element_by_name(self.check_in_input_name).send_keys(checkin)
        self.driver.find_element_by_name(self.check_out_input_name).send_keys(checkout)
        allure.attach(self.driver.get_screenshot_as_png(), name="set_date", attachment_type=AttachmentType.PNG)

    @allure.step("Setting travellers: adults: '{1}' and kids: '{2}'")
    def set_travellers(self, adult, child):
        self.logger.info("Setting tracellers {adults} and {kids}".format(adults=adult, kids=child))
        self.driver.find_element_by_id(self.travellers_input_id).click()
        self.driver.find_element_by_id(self.adult_input_id).clear()
        self.driver.find_element_by_id(self.child_input_id).clear()
        self.driver.find_element_by_id(self.adult_input_id).send_keys(adult)
        self.driver.find_element_by_id(self.child_input_id).send_keys(child)
        allure.attach(self.driver.get_screenshot_as_png(), name="set_travellers", attachment_type=AttachmentType.PNG)

    @allure.step("Click the button 'search'")
    def search_hotels(self):
        self.logger.info("Performing search".format())
        self.driver.find_element_by_xpath(self.search_button_xpath).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="search_hotels", attachment_type=AttachmentType.PNG)