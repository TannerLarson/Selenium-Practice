from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *


def wait_until_found(driver, xpath):
    try:
        WebDriverWait(driver, 5).until(
            lambda x: x.find_element_by_xpath(xpath))
    except TimeoutException:
        return False
    else:
        return True