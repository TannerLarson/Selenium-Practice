from locators import *
from globalElements import *
from element import BasePageElement


#  --------- Decorators ------------------------------------------
def confirm_correct_page(func):
    def func_wrapper(self):
        xpath = ''
        print(type(self))
        if isinstance(self, HomePage):
            xpath = "//body[@id='index']"
        elif isinstance(self, SearchResultPage):
            xpath = "//body[@id='search']"
        elif isinstance(self, ContactPage):
            xpath = "//body[@id='contact']"
        elif isinstance(self, AccountPage):
            xpath = "//body[@id='my-account']"
        if not wait_until_found(self.driver, xpath):
            assert False, "Page not found"
        else:
            return func(self)

    return func_wrapper


#  --------- Classes ------------------------------------------
class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def is_title_matches(self):
        return "My Store" in self.driver.title

    @confirm_correct_page
    def is_page_correct(self):
        return True


class HomePage(BasePage):
    # --------- ELEMENTS -----------------------------------------------
    class SearchTextElement(BasePageElement):
        locator = "search_query"

    search_text_element = SearchTextElement()

    # --------- ACTIONS --------------------------------------------------
    @confirm_correct_page
    def click_search_button(self):
        element = self.driver.find_element(*IndexPageLocators.SEARCH_BUTTON)
        element.click()

    @confirm_correct_page
    def click_ad_top(self):
        element = self.driver.find_element(*IndexPageLocators.AD_TOP)
        element.click()

    @confirm_correct_page
    def click_contact_us_button(self):
        element = self.driver.find_element(*IndexPageLocators.CONTACT_US_BUTTON)
        element.click()

    @confirm_correct_page
    def click_logo_button(self):
        element = self.driver.find_element(*IndexPageLocators.LOGO)
        element.click()


class SearchResultPage(BasePage):
    # --------- ELEMENTS -----------------------------------------------

    # --------- ACTIONS --------------------------------------------------
    @confirm_correct_page
    def is_results_found(self):
        return "No results were found" not in self.driver.page_source


class ContactPage(BasePage):
    # --------- ELEMENTS -----------------------------------------------

    # --------- ACTIONS --------------------------------------------------
    pass


class AccountPage(BasePage):
    # --------- ELEMENTS -----------------------------------------------

    # --------- ACTIONS --------------------------------------------------
    pass
