import unittest
import page
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
import Base_Tests as base


# TODO: Create tests for mobile website

class IndexPageUnitTests(base.BaseUnitTests):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")

    def setUp(self) -> None:
        self.driver.get("http://automationpractice.com/index.php")
        self.mainPage = page.HomePage(self.driver)

    def _test_homeslider_left_button(self):
        pass

    def _test_homeslider_right_button(self):
        pass

    def _test_homeslider_two_women_shop_now_button(self):
        pass

    def _test_homeslider_two_women_picture_link(self):
        pass

    def _test_homeslider_one_woman_shop_now_button(self):
        pass

    def _test_homeslider_one_woman_picture_link(self):
        pass

    def _test_homeslider_man_and_woman_shop_now_button(self):
        pass

    def _test_homeslider_man_and_woman_picture_link(self):
        pass

    def _test_3days_sale_link(self):
        pass

    def _test_only_online_link(self):
        pass

    def _test_popular_button(self):
        pass

    def _test_best_sellers_button(self):
        pass

    def _test_printed_chiffon_dress_picture_link(self):
        pass

    def _test_printed_chiffon_dress_quick_view_button(self):
        pass

    def _test_printed_chiffon_dress_add_to_cart_button(self):
        pass

    def _test_printed_chiffon_dress_more_button(self):
        pass

    def _test_blouse_picture_link(self):
        pass

    def _test_blouse_quick_view_button(self):
        pass

    def _test_blouse_add_to_cart_button(self):
        pass

    def _test_blouse_more_button(self):
        pass

    def _test_printed_dress_1_picture_link(self):
        pass

    def _test_printed_dress_1_quick_view_button(self):
        pass

    def _test_printed_dress_1_add_to_cart_button(self):
        pass

    def _test_printed_dress_1_more_button(self):
        pass

    def _test_printed_dress_2_picture_link(self):
        pass

    def _test_printed_dress_2_quick_view_button(self):
        pass

    def _test_printed_dress_2_add_to_cart_button(self):
        pass

    def _test_printed_dress_2_more_button(self):
        pass

    def _test_printed_summer_dress_1_picture_link(self):
        pass

    def _test_printed_summer_dress_1_quick_view_button(self):
        pass

    def _test_printed_summer_dress_1_add_to_cart_button(self):
        pass

    def _test_printed_summer_dress_1_more_button(self):
        pass

    def _test_printed_summer_dress_2_picture_link(self):
        pass

    def _test_printed_summer_dress_2_quick_view_button(self):
        pass

    def _test_printed_summer_dress_2_add_to_cart_button(self):
        pass

    def _test_printed_summer_dress_2_more_button(self):
        pass

    def _test_t_shirt_picture_link(self):
        pass

    def _test_t_shirt_quick_view_button(self):
        pass

    def _test_t_shirt_add_to_cart_button(self):
        pass

    def _test_t_shirt_more_button(self):
        pass

    def _test_top_trends_picture_link(self):
        pass

    def _test_men_coats_picture_link(self):
        pass

    def _test_women_coats_picture_link(self):
        pass

    def _test_sunglasses_picture_link(self):
        pass

    def _test_handbags_picture_link(self):
        pass

    def _test_selenium_framework_button(self):
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()


if __name__ == "__main__":
    unittest.main()
