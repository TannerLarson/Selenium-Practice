import unittest
from selenium import webdriver
import page


class AutomationPractice(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("http://automationpractice.com/index.php")

    def test_title(self):
        indexPage = page.IndexPage(self.driver)
        assert indexPage.is_title_matches()

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
