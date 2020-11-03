from locator import *
from element import BasePageElement


class SearchTextElement(BasePageElement):
    locator = "q"


class BasePage:

    def __init__(self, driver):
        self.driver = driver


class IndexPage(BasePage):

    search_text_element = SearchTextElement()

    def is_title_matches(self):
        return "My Store" in self.driver.title

    def click_search_button(self):
        element = self.driver.find_element(*IndexPageLocators.SEARCH_BUTTON)
        element.click()


class SearchResultPage(BasePage):

    def is_results_found(self):
        return "No results were found" not in self.driver.page_source
