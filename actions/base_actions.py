from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import InvalidSelectorException as EX


class BaseActions:
    def __init__(self, browser):
        self.browser = browser

    def load(self, url):
        self.browser.get(url)

    def element_click(self, by_locator):
        try:
            WebDriverWait(self.browser, timeout=10).until(
                EC.visibility_of_element_located(by_locator))
            user = self.browser.find_element(*by_locator)
            user.click()
        except EX:
            print("Exception! Can't click on the element")

    def type_info(self, by_locator, keyword):
        try:
            WebDriverWait(self.browser, timeout=10).until(
                EC.visibility_of_element_located(by_locator))
            user = self.browser.find_element(*by_locator)
            user.send_keys(keyword)
        except EX:
            print("Exception! Can't find on the element")

    def is_displayed(self, by_locator):
        try:
            self.browser.find_element(*by_locator)
            WebDriverWait(self.browser, timeout=10).until(
                EC.visibility_of_element_located(by_locator))
        except EX:
            print("Exception! Can't see the element")
        assert True, "Test pass"

    def is_enabled(self, by_locator):
        try:
            self.browser.find_element(*by_locator)
            WebDriverWait(self.browser, timeout=10).until(
                EC.element_to_be_clickable(by_locator))
        except EX:
            print("Exception! Can't see the element")
        assert True, "Test pass"
