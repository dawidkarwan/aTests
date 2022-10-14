from selenium.webdriver.common.by import By

from src.commons.page_base import BasePage
from src.utils.str_enum import StrEnum


class LeftNavLocators:
    MAIN_PAGE = (By.ID, "header_logo")

    @staticmethod
    def get_tab_locator(name: str) -> tuple:
        return By.XPATH, f'//ul[@class="menu"]//a[text()="{name}"]'


class LeftNavData(StrEnum):
    PROJECT = "Projekt"
    RELEASES = "Wydania"
    ENV = "Środowiska"
    VERSION = "Wersje"
    TAGS = "Tagi"
    TASK = "Zadania"
    DEFECTS = "Defekty"
    TESTS = " Baza testów"
    FILES = "Pliki"


class LeftNavPage(BasePage):

    def go_to_tab(self, tab_name: str):
        if [name for name in LeftNavData if name == tab_name]:
            self.driver.find_element(*LeftNavLocators.get_tab_locator(tab_name)).click()
        else:
            raise NotImplementedError(f"{tab_name} not added")

    def go_to_main_page(self):
        self.driver.find_element(*LeftNavLocators.MAIN_PAGE).click()
