import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from page_object_patern.utils.driver_factory import DriverFactory


@pytest.fixture()
def setup(request):
        driver = DriverFactory.get_driver("chrome")
        driver.implicitly_wait(10)
        #driver.maximize_window()               w driver_factory mamy opcje maksymalizacji
        request.cls.driver = driver
        before_failed = request.session.testsfailed                             #zmienna ile błedów
        yield
        if request.session.testsfailed != before_failed:                       #po yield porównuje if != to screeshot
            allure.attach(driver.get_screenshot_as_png(), name="before failed", attachment_type=AttachmentType.PNG)
        driver.quit()