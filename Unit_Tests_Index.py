import unittest
import page
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *


def wait_until(driver, func):
    """
    :param driver: Driver to put on pause
    :param func: Function that returns a boolean
    :return: True if found, False if timed out
    """
    try:
        WebDriverWait(driver, 5).until(lambda x: func)
    except TimeoutException:
        return False
    return True


class IndexPageTests(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")

    def setUp(self) -> None:
        self.driver.get("http://automationpractice.com/index.php")
        self.homePage = page.HomePage(self.driver)

    def _test_is_index(self):
        assert self.homePage.is_page_correct()

    def _test_title(self):
        print("Testing webpage title...")
        assert self.homePage.is_title_matches()

    def _test_search_button(self):
        print("Testing search button...")
        self.homePage.click_search_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert wait_until(self.driver, search_result_page.is_page_correct())

    def _test_top_ad(self):
        print("Testing advertisement at top of website")
        self.homePage.click_ad_top()
        time.sleep(0.5)  # Give driver time to navigate
        assert self.homePage.is_page_correct()

    def test_contact_us_button(self):
        print("Testing Contact us button")
        self.homePage.click_contact_us_button()
        contact_page = page.ContactPage(self.driver)
        assert contact_page.is_page_correct(), "is_page_contact failed"

    def _test_logo_button(self):
        print("Testing logo button")
        self.homePage.click_logo_button()
        assert self.homePage.is_page_correct(), "is_page_contact failed"

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()


if __name__ == "__main__":
    unittest.main()
