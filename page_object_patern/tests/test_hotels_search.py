import pytest
import allure
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

from page_object_patern.pages.result_search_hotel import ResultSearchHotel
from page_object_patern.pages.search_hotel import SearchHotelPage
from page_object_patern.utils.read_excel import ExcelReader


@pytest.mark.usefixtures("setup")               # współdzielenie metody setup()
class TestHotelsSearch:

    @allure.title("This is title")
    @allure.description("Test description")
    @pytest.mark.parametrize("data", ExcelReader.get_data())           #oznaczamy metode testowa i podajemy parametr data i podajemy metode ktora zwraca liste
    def test_hotel_search(self, data):                          #data jako parametr testowy
        self.driver.get("http://www.kurs-selenium.pl/demo/")
        home_page = SearchHotelPage(self.driver)
        home_page.set_city("Dubai")
        home_page.set_date(data.checkin, data.checkout)         #przekazujemy odpowiednie wartosci z clasy searchdata
        home_page.set_travellers('2', '2')
        home_page.search_hotels()
        result_page = ResultSearchHotel(self.driver)
        hotel_names = result_page.list_hotels()
        prices_list = result_page.list_prices()

        assert hotel_names[0] == 'Jumeirah Beach Hotel'
        assert hotel_names[1] == 'Oasis Beach Tower'
        assert hotel_names[2] == 'Rose Rayhaan Rotana'
        assert hotel_names[3] == 'Hyatt Regency Perth'

        assert prices_list[0] == '$22'
        assert prices_list[1] == '$50'
        assert prices_list[2] == '$80'
        assert prices_list[3] == '$150'
