from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait

from src.commons.common_actions import CommonActions


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def wait(self, timeout: int = 15) -> WebDriverWait:
        return WebDriverWait(self.driver, timeout)

    @property
    def common_actions(self) -> CommonActions:
        return CommonActions(self.driver)
