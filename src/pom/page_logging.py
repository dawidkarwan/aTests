from dataclasses import dataclass

import allure

from src.pom.commons.page_base import BasePage
from src.utils.locator import LoCreator


class LoggingLocators:
    INPUT_LOGIN = LoCreator.id("email")
    INPUT_PASSWORD = LoCreator.id("password")
    BUTTON_LOGIN = LoCreator.id("login")


@dataclass
class LoggingData:
    login: str = "administrator@testarena.pl"
    password: str = "sumXQQ72$L"


class LoggingPage(BasePage):

    @allure.step("Zaloguj się do aplikacji")
    def log_in(self):
        self.driver.find_element(*LoggingLocators.INPUT_LOGIN).send_keys(LoggingData.login)
        self.driver.find_element(*LoggingLocators.INPUT_PASSWORD).send_keys(LoggingData.password)
        self.driver.find_element(*LoggingLocators.BUTTON_LOGIN).click()
