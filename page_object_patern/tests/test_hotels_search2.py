import pytest
import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from page_object_patern.pages.result_search_hotel import ResultSearchHotel
from page_object_patern.pages.search_hotel import SearchHotelPage


@pytest.mark.usefixtures("setup")  # współdzielenie metody setup() plik conftest
class TestHotelsSearch:

    @allure.title("This is title")
    @allure.description("Test description")
    def test_hotel_search(self, setup):
        self.driver.get("http://www.kurs-selenium.pl/demo/")
        home_page = SearchHotelPage(self.driver)
        home_page.set_city("Dubai")
        home_page.set_date('18/10/2019', '22/10/2019')
        home_page.set_travellers('2', '2')
        home_page.search_hotels()
        result_page = ResultSearchHotel(self.driver)
        hotel_names = result_page.list_hotels()
        prices_list = result_page.list_prices()

        assert hotel_names[0] == 'Jumerah Beach Hotel'
        assert hotel_names[1] == 'Oasis Beach Tower'
        assert hotel_names[2] == 'Rose Rayhaan Rotana'
        assert hotel_names[3] == 'Hyatt Regency Perth'

        assert prices_list[0] == '$2'
        assert prices_list[1] == '$50'
        assert prices_list[2] == '$80'
        assert prices_list[3] == '$150'
