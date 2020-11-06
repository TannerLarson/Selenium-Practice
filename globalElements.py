from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
import time


def wait_until_found(driver, xpath):
    try:
        WebDriverWait(driver, 10).until(
            lambda x: x.find_element_by_xpath(xpath))
    except TimeoutException:
        return False
    else:
        return True
