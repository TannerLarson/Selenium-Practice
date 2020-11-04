from locator import *
from element import BasePageElement


class BasePage:

    def __init__(self, driver):
        self.driver = driver


class HomePage(BasePage):
    # --------- ELEMENTS -----------------------------------------------
    class SearchTextElement(BasePageElement):
        locator = "search_query"

    search_text_element = SearchTextElement()

    # --------- TESTS --------------------------------------------------

    def is_page_index(self):
        return self.driver.find_element_by_xpath("//body[@id='index']")

    def is_title_matches(self):
        return "My Store" in self.driver.title

    def click_search_button(self):
        element = self.driver.find_element(*IndexPageLocators.SEARCH_BUTTON)
        element.click()


class SearchResultPage(BasePage):
    # --------- ELEMENTS -----------------------------------------------

    # --------- TESTS --------------------------------------------------

    def is_page_search(self):
        return self.driver.find_element_by_xpath("//body[@id='search']")

    def is_results_found(self):
        return "No results were found" not in self.driver.page_source
