from dataclasses import dataclass

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class LoggingLocators:
    INPUT_LOGIN = (By.ID, "email")
    INPUT_PASSWORD = (By.ID, "password")
    BUTTON_LOGIN = (By.ID, "login")


@dataclass
class LoggingData:
    login: str = "administrator@testarena.pl"
    password: str = "sumXQQ72$L"


class LoggingPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def log_in(self):
        self.driver.find_element(*LoggingLocators.INPUT_LOGIN).send_keys(LoggingData.login)
        self.driver.find_element(*LoggingLocators.INPUT_PASSWORD).send_keys(LoggingData.password)
        self.driver.find_element(*LoggingLocators.BUTTON_LOGIN).click()
