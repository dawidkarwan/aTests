from dataclasses import dataclass

import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from src.pom.commons.page_base import BasePage


class TasksLocators:
    BUTTON_ADD_TASK = (By.XPATH, '//a[@class="button_link"][text()="Dodaj zadanie"]')
    INPUT_TITLE = (By.ID, 'title')
    INPUT_DESCRIPTION = (By.ID, 'description')
    INPUT_ENV = (By.ID, 'token-input-environments')
    INPUT_VERSION = (By.ID, 'token-input-versions')
    INPUT_DUE_DATE = (By.ID, 'dueDate')
    INPUT_ASSIGNEE_TO = (By.ID, 'assigneeName')
    DDL_ASSIGNEE_TO = (By.XPATH, '//a[@class="ui-corner-all"][contains(text(),"Gall Anonim")]')
    INPUT_TAG = (By.ID, 'token-input-tags')
    BUTTON_SAVE = (By.ID, 'save')
    DDL_PRIORITY = (By.ID, 'priority')
    BUTTON_CANCEL = (By.XPATH, '//span[@class="j_cancel_button"]//a[text()="Anuluj"]')

    @staticmethod
    def priority_option(priority: str) -> tuple[str, str]:
        return By.XPATH, f'//select[@id="priority"]/option[.="{priority}"]'

    @staticmethod
    def dynamic_ddl(value: str) -> tuple[str, str]:
        return By.XPATH, f'//div[@class="token-input-dropdown-facebook"]//li[.="{value}"]'


@dataclass
class TasksDataClass:
    title: str
    description: str
    env: str
    version: str
    due_date: str
    assignee_to: str
    tag: str
    priority: str


class TasksPage(BasePage):

    @allure.step("Dodaj nowe zadanie")
    def add_new_task(self, params: TasksDataClass):
        self._click_add_task()
        self._fill_new_task_fields(params)
        self._click_save_task()

    @allure.step("Anuluj zadanie")
    def cancel_task(self):
        self._click_add_task()
        self._click_cancel_app()

    @allure.step("Uzupełnij pola w nowym zadaniu")
    def _fill_new_task_fields(self, params: TasksDataClass):
        self.driver.find_element(*TasksLocators.INPUT_TITLE).send_keys(params.title)
        self.driver.find_element(*TasksLocators.INPUT_DESCRIPTION).send_keys(params.description)
        self.driver.find_element(*TasksLocators.INPUT_ENV).send_keys(params.env)
        self.common_actions.wait_for_ddl()
        self.driver.find_element(*TasksLocators.dynamic_ddl(params.env)).click()
        self.driver.find_element(*TasksLocators.INPUT_VERSION).send_keys(params.version)
        self.common_actions.wait_for_ddl()
        self.driver.find_element(*TasksLocators.dynamic_ddl(params.version)).click()
        self.driver.find_element(*TasksLocators.DDL_PRIORITY).click()
        self.driver.find_element(*TasksLocators.priority_option(params.priority)).click()
        self.driver.find_element(*TasksLocators.INPUT_DUE_DATE).send_keys(params.due_date + Keys.TAB)
        self.driver.find_element(*TasksLocators.INPUT_ASSIGNEE_TO).send_keys(params.assignee_to)
        self.wait().until(EC.visibility_of_element_located(TasksLocators.DDL_ASSIGNEE_TO))
        self.driver.find_element(*TasksLocators.DDL_ASSIGNEE_TO).click()
        self.driver.find_element(*TasksLocators.INPUT_TAG).send_keys(params.tag)
        self.common_actions.wait_for_ddl()
        self.driver.find_element(*TasksLocators.dynamic_ddl(params.tag)).click()

    @allure.step("Kliknij dodaj zadanie")
    def _click_add_task(self):
        self.driver.find_element(*TasksLocators.BUTTON_ADD_TASK).click()

    @allure.step("Kliknij zapisz")
    def _click_save_task(self):
        self.driver.find_element(*TasksLocators.BUTTON_SAVE).click()

    @allure.step("Kliknij anuluj")
    def _click_cancel_app(self):
        self.driver.find_element(*TasksLocators.BUTTON_CANCEL).click()
