"""This module has the base actions from this project"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BaseActions:

    def __init__(self, browser):
        self.browser = browser

    def load(self, url):
        """Load the specified URL in the browser."""
        self.browser.get(url)

    def _wait_for_element(self, by_locator, timeout=10):
        """Wait for the element to be present and return it."""
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located(by_locator)
            )
            return self.browser.find_element(*by_locator)
        except TimeoutException:
            print(f"Timeout! The element {by_locator} was not found.")
            return None

    def element_click(self, by_locator):
        """Click on the element specified by the locator."""
        user = self._wait_for_element(by_locator)
        if user:
            user.click()
        else:
            raise Exception(f"Can't click on the element: {by_locator}")

    def type_info(self, by_locator, keyword):
        """Type information into the element specified by the locator."""
        user = self._wait_for_element(by_locator)
        if user:
            user.send_keys(keyword)
        else:
            raise Exception(f"Can't find the element to type on: {by_locator}")

    def is_displayed(self, by_locator) -> bool:
        """Check if the element specified by the locator is displayed."""
        user = self._wait_for_element(by_locator)
        if user:
            return user.is_displayed()
        return False

    def is_enabled(self, by_locator) -> bool:
        """Check if the element specified by the locator is enabled."""
        user = self._wait_for_element(by_locator)
        if user:
            return user.is_enabled()
        return False
