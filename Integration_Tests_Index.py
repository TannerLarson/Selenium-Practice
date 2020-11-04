import unittest
from selenium import webdriver
import page


class IndexPageTests(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("http://automationpractice.com/index.php")

    def tearDown(self) -> None:
        self.driver.close()

    # --------- TESTS -----------------------------------------------

    def _test_search_skirt(self):
        # test_title
        homePage = page.HomePage(self.driver)
        assert homePage.is_title_matches()

        homePage.search_text_element = "skirt"
        homePage.click_search_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()
        self.driver.implicitly_wait(5)