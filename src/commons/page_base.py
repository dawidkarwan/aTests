from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait

from src.commons.common_actions import CommonActions


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @property
    def wait(self) -> WebDriverWait:
        return WebDriverWait(self.driver, 15)

    @property
    def common_actions(self) -> CommonActions:
        return CommonActions(self.driver)
