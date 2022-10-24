from selenium.webdriver.common.by import By

from src.commons.page_base import BasePage


class ModalLocators:
    INFO_MSG = (By.XPATH, '//div[@id="j_info_box"]//p')


class ModalPage(BasePage):

    def get_info_msg(self) -> str:
        return self.driver.find_element(*ModalLocators.INFO_MSG).text
