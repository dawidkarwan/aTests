import allure

from src.pom.commons.page_base import BasePage
from src.utils.locator import LoCreator, Locator
from src.utils.str_enum import StrEnum


class LeftNavLocators:
    MAIN_PAGE = LoCreator.id("header_logo")

    @staticmethod
    def get_tab_locator(name: str) -> Locator:
        return LoCreator.xpath(f'//ul[@class="menu"]//a[text()="{name}"]')


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

    @allure.step("Przejdź do zakładki")
    def go_to_tab(self, tab_name: LeftNavData):
        self.driver.find_element(*LeftNavLocators.get_tab_locator(tab_name)).click()

    @allure.step("Przejdź do strony głównej")
    def go_to_main_page(self):
        self.driver.find_element(*LeftNavLocators.MAIN_PAGE).click()
