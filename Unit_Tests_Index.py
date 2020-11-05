import unittest
from selenium import webdriver
import page
import time


class IndexPageTests(unittest.TestCase):

    @classmethod
    def setUpClass(self) -> None:
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")

    def setUp(self) -> None:
        self.driver.get("http://automationpractice.com/index.php")
        self.homePage = page.HomePage(self.driver)

    def _test_is_index(self):
        assert self.homePage.is_page_index()

    def test_title(self):
        print("Testing webpage title...")
        assert self.homePage.is_title_matches()

    def _test_search_button(self):
        print("Testing search button...")
        # test_title
        self.homePage.click_search_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_page_search()

    def _test_top_ad(self):
        print("Testing advertisement at top of website")
        self.homePage.click_ad_top()
        assert self.homePage.is_page_index()

    def test_contact_us_button(self):
        print("Testing Contact us button")
        self.homePage.click_contact_us_button()
        contact_page = page.ContactPage(self.driver)
        assert contact_page.is_page_contact()

    @classmethod
    def tearDownClass(self) -> None:
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
