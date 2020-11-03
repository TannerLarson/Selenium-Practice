from selenium.webdriver.common.by import By


class IndexPageLocator:
    GO_BUTTON = (By.XPATH, "//button[@type='submit']")
    SEARCH_TEXT_BOX = (By.ID, "search_query_top")
    LOGO = (By.XPATH, "//img[@class='logo img-responsive']")


class SearchResultsPageLocators:
    pass
