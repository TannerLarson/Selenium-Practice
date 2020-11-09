import unittest
import page
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *


def wait_until(driver, func):
    """
    :param driver: Driver to put on pause
    :param func: Function that returns a boolean
    :return: True if found, False if timed out
    """
    try:
        WebDriverWait(driver, 5).until(lambda x: func)
    except TimeoutException:
        return False
    return True


class BaseUnitTests(unittest.TestCase):
    driver = None

    mainPage = None

    # --------- TOP OF PAGE ---------------------------------------------

    def _test_is_page_correct(self):
        assert self.mainPage.is_page_correct()

    def _test_title(self):
        print("Testing webpage title...")
        assert self.mainPage.is_title_matches()

    def _test_search_button(self):
        print("Testing search button...")
        self.mainPage.click_search_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert wait_until(self.driver, search_result_page.is_page_correct())

    def _test_top_ad(self):
        print("Testing advertisement at top of website")
        self.mainPage.click_ad_top()
        time.sleep(0.5)  # Give driver time to navigate
        assert self.mainPage.is_page_correct()

    def _test_contact_us_button(self):
        print("Testing Contact us button")
        self.mainPage.click_contact_us_button()
        contactPage = page.ContactPage(self.driver)
        assert contactPage.is_page_correct()

    def _test_sign_in_button(self):
        print("Testing Sign in button")
        self.mainPage.sign_out()
        self.mainPage.click_sign_in_button()
        signInPage = page.SignInPage(self.driver)
        assert signInPage.is_page_correct()

    def _test_account_button(self):
        print("Testing Account button")
        self.mainPage.sign_in()
        self.driver.get("http://automationpractice.com/index.php")
        assert self.mainPage.is_page_correct()

        self.mainPage.click_account_button()
        accountPage = page.AccountPage(self.driver)
        assert accountPage.is_page_correct()

    def _test_sign_out_button(self):
        print("Testing Sign out button")
        self.mainPage.sign_in()
        self.driver.get("http://automationpractice.com/index.php")
        assert self.mainPage.is_page_correct()

        self.mainPage.click_sign_out_button()
        assert self.mainPage.is_page_correct()

    def _test_logo_button(self):
        print("Testing logo button")
        self.mainPage.click_logo_button()
        assert self.mainPage.is_page_correct()

    def _test_cart_button_empty(self):
        pass

    def _test_cart_button_full(self):
        pass

    def _test_cart_dropdown_empty(self):
        pass

    def _test_cart_dropdown_full(self):
        pass

    def _test_women_button(self):
        pass

    def _test_dresses_button(self):
        pass

    def _test_t_shirts_button(self):
        pass

    def _test_women_dropdown(self):
        pass

    def _test_dresses_dropdown(self):
        pass

    # --------- BOTTOM OF PAGE --------------------------------------------
    def _test_submit_newsletter_button(self):
        pass

    def _test_facebook_button(self):
        pass

    def _test_twitter_button(self):
        pass

    def _test_youtube_button(self):
        pass

    def _test_google_plus_button(self):
        pass

    def _test_categories_women(self):
        pass

    def _test_information_specials_button(self):
        pass

    def _test_information_new_products_Button(self):
        pass

    def _test_information_best_sellers(self):
        pass

    def _test_information_our_stores(self):
        pass

    def _test_information_contact_us(self):
        pass

    def _test_information_terms_conditions(self):
        pass

    def _test_information_about_us(self):
        pass

    def _test_information_sitemap(self):
        pass

    def _test_my_account_my_orders(self):
        pass

    def _test_my_account_my_credit_slips(self):
        pass

    def _test_my_account_my_addresses(self):
        pass

    def _test_my_account_my_personal_info(self):
        pass

    def _test_my_account_sign_out(self):
        pass

    def _test_email_support_link(self):
        pass

    def _test_ecommerce_link(self):
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()


class BaseIntegrationTests(unittest.TestCase):
    driver = None

    mainPage = None

    # --------- TOP OF PAGE ---------------------------------------------
    def _test_search_skirt(self):
        # test_title
        homePage = page.HomePage(self.driver)
        assert homePage.is_title_matches()

        homePage.search_text_element = "skirt"
        homePage.click_search_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()

    # --------- BOTTOM OF PAGE ---------------------------------------------
    def _test_newsletter_invalid_email(self):
        pass

    def _test_newsletter_valid_email(self):
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()


def execute():
    unittest.main()
