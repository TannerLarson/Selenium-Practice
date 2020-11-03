class BasePage:

    def __init__(self, driver):
        self.driver = driver


class IndexPage(BasePage):

    def is_title_matches(self):
        return "My Store" in self.driver.title

    def click_search_button(self):
        element = self.driver.find_element()
        element.click()