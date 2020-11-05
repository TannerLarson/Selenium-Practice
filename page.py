from locators import *
from globalElements import *
from element import BasePageElement


#  --------- Decorators ------------------------------------------
def confirm_page_index(func):
    def func_wrapper(self):
        if not wait_until_found(self.driver, "//body[@id='index']"):
            assert False, "Page not found"
        else:
            return func(self)

    return func_wrapper


def confirm_page_search(func):
    def func_wrapper(self):
        if not wait_until_found(self.driver, "//body[@id='search']"):
            assert False, "Page not found"
        else:
            return func(self)

    return func_wrapper


def confirm_page_contact(func):
    def func_wrapper(self):
        if not wait_until_found(self.driver, "//body[@id='contact']"):
            assert False, "Page not found"
        else:
            return func(self)

    return func_wrapper


#  --------- Classes ------------------------------------------
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

    @confirm_page_index
    def click_search_button(self):
        element = self.driver.find_element(*IndexPageLocators.SEARCH_BUTTON)
        element.click()

    @confirm_page_index
    def click_ad_top(self):
        element = self.driver.find_element(*IndexPageLocators.AD_TOP)
        element.click()

    @confirm_page_index
    def click_contact_us_button(self):
        element = self.driver.find_element(*IndexPageLocators.CONTACT_US_BUTTON)
        element.click()


class SearchResultPage(BasePage):
    # --------- ELEMENTS -----------------------------------------------

    # --------- TESTS --------------------------------------------------

    def is_page_search(self):
        return wait_until_found(self.driver, "//body[@id='search']")

    @confirm_page_search
    def is_results_found(self):
        return "No results were found" not in self.driver.page_source


class ContactPage(BasePage):
    # --------- ELEMENTS -----------------------------------------------

    # --------- TESTS --------------------------------------------------
    def is_page_contact(self):
        return wait_until_found(self.driver, "//body[@id='contact']")
