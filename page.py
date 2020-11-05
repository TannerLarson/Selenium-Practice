from locators import *
from globalElements import *
from element import BasePageElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *


class BasePage:

    def __init__(self, driver):
        self.driver = driver


class HomePage(BasePage):
    # --------- ELEMENTS -----------------------------------------------
    class SearchTextElement(BasePageElement):
        locator = "search_query"

    search_text_element = SearchTextElement()

    # --------- ACTIONS --------------------------------------------------
    def is_page_index(self):
        return self.driver.find_elements_by_xpath("//body[@id='index']")

    def is_title_matches(self):
        return "My Store" in self.driver.title

    def click_search_button(self):
        element = self.driver.find_element(*IndexPageLocators.SEARCH_BUTTON)
        element.click()

    def click_ad_top(self):
        element = self.driver.find_element(*IndexPageLocators.AD_TOP)
        element.click()

    def click_contact_us_button(self):
        element = self.driver.find_element(*IndexPageLocators.CONTACT_US_BUTTON)
        element.click()


class SearchResultPage(BasePage):
    # --------- ELEMENTS -----------------------------------------------

    # --------- TESTS --------------------------------------------------
    def is_page_search(self):
        return bool(self.driver.find_elements_by_xpath("//body[@id='search']"))

    def is_results_found(self):
        return "No results were found" not in self.driver.page_source


class ContactPage(BasePage):
    # --------- ELEMENTS -----------------------------------------------

    # --------- TESTS --------------------------------------------------
    def is_page_contact(self):
        wait_until_found(self.driver, "//body[@id='contact']")  # TODO: For some reason this refuses to work
        #return bool(self.driver.find_elements_by_id("contact"))

