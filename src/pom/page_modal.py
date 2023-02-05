import allure
from selenium.webdriver.common.by import By

from src.pom.commons.page_base import BasePage


class ModalLocators:
    INFO_MSG = (By.XPATH, '//div[@id="j_info_box"]//p')


class ModalPage(BasePage):

    @allure.step("Pobierz komunikat informacyjny")
    def get_info_msg(self) -> str:
        return self.driver.find_element(*ModalLocators.INFO_MSG).text
