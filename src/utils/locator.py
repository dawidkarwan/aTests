from typing import NamedTuple

from selenium.webdriver.common.by import By


class Locator(NamedTuple):
    by: str
    value: str


class LoCreator:
    @staticmethod
    def xpath(value: str) -> Locator:
        return Locator(by=By.XPATH, value=value)

    @staticmethod
    def id(value: str) -> Locator:
        return Locator(by=By.ID, value=value)
