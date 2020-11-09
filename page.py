from locators import *
from globalElements import *
from element import BasePageElement


#  --------- Decorators ------------------------------------------
def confirm_correct_page(func):
    def func_wrapper(self):
        xpath = ''
        if isinstance(self, HomePage):
            xpath = "//body[@id='index']"
        elif isinstance(self, SearchResultPage):
            xpath = "//body[@id='search']"
        elif isinstance(self, ContactPage):
            xpath = "//body[@id='contact']"
        elif isinstance(self, AccountPage):
            xpath = "//body[@id='my-account']"
        elif isinstance(self, SignInPage):
            xpath = "//body[@id='authentication']"
        else:
            assert False, "You need to add an elif statement"
        if not wait_until_found(self.driver, xpath):
            assert False, "Page not found"
        else:
            return func(self)

    return func_wrapper


#  --------- Classes ------------------------------------------
class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # --------- ELEMENTS -----------------------------------------------
    class SearchTextElement(BasePageElement):
        locator = "search_query"

    search_text_element = SearchTextElement()

    # --------- ACTIONS --------------------------------------------------

    def is_title_matches(self):
        return "My Store" in self.driver.title

    @confirm_correct_page
    def is_page_correct(self):
        return True

    def is_signed_in(self):
        try:
            self.driver.find_element(*Locators.ACCOUNT_BUTTON)
        except NoSuchElementException:
            return False
        else:
            return True

    def sign_in(self):
        if self.is_signed_in():
            return
        element = self.driver.find_element(*IndexPageLocators.SIGN_IN_BUTTON)
        element.click()
        signInPage = SignInPage(self.driver)
        assert signInPage.is_page_correct()

        signInPage.email_text_element = "tanner.b.larson@gmail.com"
        signInPage.password_text_element = "inksplot"
        signInPage.click_submit_login_button()

        accountPage = AccountPage(self.driver)
        accountPage.is_page_correct()

    def sign_out(self):
        if not self.is_signed_in():
            return
        element = self.driver.find_element(*Locators.SIGN_OUT_BUTTON)
        element.click()


class HomePage(BasePage):
    # --------- ELEMENTS -------------------------------------------------

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

    @confirm_correct_page
    def click_account_button(self):
        if not self.is_signed_in():
            assert False, "Must be signed in for button to exist"
        element = self.driver.find_element(*IndexPageLocators.ACCOUNT_BUTTON)
        element.click()

    @confirm_correct_page
    def click_sign_in_button(self):
        if self.is_signed_in():
            assert False, "Must be signed out for button to exist"
        element = self.driver.find_element(*IndexPageLocators.SIGN_IN_BUTTON)
        element.click()

    @confirm_correct_page
    def click_sign_out_button(self):
        if not self.is_signed_in():
            assert False, "Must be signed in for button to exist"
        element = self.driver.find_element(*IndexPageLocators.SIGN_OUT_BUTTON)
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


class SignInPage(BasePage):
    # --------- ELEMENTS -----------------------------------------------
    class EmailTextElement(BasePageElement):
        locator = "email"

    email_text_element = EmailTextElement()

    class PasswordTextElement(BasePageElement):
        locator = "passwd"

    password_text_element = PasswordTextElement()

    # --------- ACTIONS --------------------------------------------------
    def click_submit_login_button(self):
        # TODO: ERROR: test_account_button NoSuchElementException
        element = self.driver.find_element(*SignInPageLocators.SUBMIT_LOGIN_BUTTON)
        element.click()
