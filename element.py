from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *


class BasePageElement:

    def __init__(self):
        # Ensure self.locator is implemented
        assert self.locator, "Locator not implemented"
        assert isinstance(self.locator, str), "Locator {} is not a string".format(self.locator)
        assert len(self.locator) > 0, "Locator {} is empty".format(self.locator)

    def __set__(self, instance, value):
        driver = instance.driver
        try:
            WebDriverWait(driver, 5).until(
                lambda driver: driver.find_element_by_name(self.locator))
        except TimeoutException:
            assert False, "Locator {} not found".format(self.locator)
        driver.find_element_by_name(self.locator).clear()
        driver.find_element_by_name(self.locator).send_keys(value)

    def __get__(self, instance, owner):
        driver = instance.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        element = driver.find_element_by_name(self.locator)
        return element.get_attribute("value")
