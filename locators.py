from selenium.webdriver.common.by import By


# locators.py is a reference page filled with HTML locators used to move the mouse around the webpage

class IndexPageLocators:
    SEARCH_BUTTON = (By.XPATH, "//button[@name='submit_search']")
    CONTACT_US_BUTTON = (By.ID, "contact-link")
    SEARCH_TEXT_BOX = (By.ID, "search_query_top")
    AD_TOP = (By.CLASS_NAME, "img-responsive")
    LOGO = (By.XPATH, "//img[@class='logo img-responsive']")


class SearchResultsPageLocators:
    pass
