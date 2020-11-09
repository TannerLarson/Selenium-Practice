import unittest
from selenium import webdriver
import Base_Tests as base
import page


class IndexPageTests(base.BaseIntegrationTests):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")

    def setUp(self) -> None:
        self.driver.get("http://automationpractice.com/index.php")
        self.mainPage = page.HomePage(self.driver)

    @classmethod
    def tearDownClass(self) -> None:
        self.driver.close()

    # --------- TESTS -----------------------------------------------


if __name__ == "__main__":
    unittest.main()
