import allure

from src.pom.commons.page_base import BasePage
from src.utils.locator import LoCreator


class ModalLocators:
    INFO_MSG = LoCreator.xpath('//div[@id="j_info_box"]//p')


class ModalPage(BasePage):

    @allure.step("Pobierz komunikat informacyjny")
    def get_info_msg(self) -> str:
        return self.driver.find_element(*ModalLocators.INFO_MSG).text
