import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from src.commons.page_base import BasePage


class HeaderLocators:
    ACTIVE_PROJECT = (By.XPATH, '//div[@id="activeProject_chosen"]//span')
    INPUT_PROJECT = (By.XPATH, '//div[@id="activeProject_chosen"]//input')

    @staticmethod
    def chose_project(project: str) -> tuple[str, str]:
        return By.XPATH, f'//div[@id="activeProject_chosen"]//li[text()="{project}"]'


class HeaderPage(BasePage):

    def get_active_project_name(self) -> str:
        return self.driver.find_element(*HeaderLocators.ACTIVE_PROJECT).text

    @allure.step("Zmień projekt")
    def change_project(self, project: str):
        self.driver.find_element(*HeaderLocators.ACTIVE_PROJECT).click()
        self.wait(5).until(EC.visibility_of_element_located(HeaderLocators.chose_project(project)))
        self.driver.find_element(*HeaderLocators.chose_project(project)).click()
        self.wait().until(EC.visibility_of_element_located(HeaderLocators.ACTIVE_PROJECT))
