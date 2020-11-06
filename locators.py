from selenium.webdriver.common.by import By


# locators.py is a reference page filled with HTML locators used to move the mouse around the webpage

class Locators:
    """
    Contains all the locators found on every page
    """
    SEARCH_BUTTON = (By.XPATH, "//button[@name='submit_search']")
    CONTACT_US_BUTTON = (By.ID, "contact-link")
    SEARCH_TEXT_BOX = (By.ID, "search_query_top")
    AD_TOP = (By.CLASS_NAME, "img-responsive")
    LOGO = (By.XPATH, "//img[@class='logo img-responsive']")
    ACCOUNT_BUTTON = (By.XPATH, "//a[@class='account']")
    SIGN_OUT_BUTTON = (By.XPATH, "//a[@title='Log me out']")
    SIGN_IN_BUTTON = (By.XPATH, "//a[@class='login']")


class IndexPageLocators(Locators):
    pass


class SearchResultsPageLocators(Locators):
    pass


class SignInPageLocators(Locators):
    SUBMIT_LOGIN_BUTTON = (By.ID, "SubmitLogin")
