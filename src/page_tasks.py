from dataclasses import dataclass

from selenium.webdriver.common.by import By

from src.commons.page_base import BasePage


class TasksLocators:
    TITLE = (By.XPATH, '//h1[@class="content_title"]')
    BUTTON_ADD_TASK = (By.XPATH, '//a[@class="button_link"][text()="Dodaj zadanie"]')
    INPUT_TITLE = (By.ID, 'title')
    INPUT_DESCRIPTION = (By.ID, 'description')
    INPUT_ENV = (By.ID, 'token-input-environments')
    INPUT_VERSION = (By.ID, 'token-input-versions')
    INPUT_DUE_DATE = (By.ID, 'dueDate')
    INPUT_ASSIGNEE_TO = (By.ID, 'assigneeName')
    INPUT_TAG = (By.ID, 'token-input-tags')
    BUTTON_SAVE = (By.ID, 'save')
    DDL_PRIORITY = (By.ID, 'priority')

    @staticmethod
    def priority_option(priority: str) -> tuple:
        return By.XPATH, f'//select[@id="priority"]/option[.="{priority}"]'


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

    def fill_new_task_fields(self, params: TasksDataClass):
        self.driver.find_element(*TasksLocators.BUTTON_ADD_TASK).click()
        self.driver.find_element(*TasksLocators.INPUT_TITLE).send_keys(params.title)
        self.driver.find_element(*TasksLocators.INPUT_DESCRIPTION).send_keys(params.description)
        self.driver.find_element(*TasksLocators.INPUT_ENV).send_keys(params.env)
        self.driver.find_element(*TasksLocators.INPUT_VERSION).send_keys(params.version)
        self.driver.find_element(*TasksLocators.DDL_PRIORITY).click()
        self.driver.find_element(*TasksLocators.priority_option(params.priority)).click()
        self.driver.find_element(*TasksLocators.INPUT_DUE_DATE).send_keys(params.due_date)
        self.driver.find_element(*TasksLocators.INPUT_ASSIGNEE_TO).send_keys(params.assignee_to)
        self.driver.find_element(*TasksLocators.INPUT_TAG).send_keys(params.tag)
        self.driver.find_element(*TasksLocators.BUTTON_SAVE).click()
