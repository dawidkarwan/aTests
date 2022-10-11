from dataclasses import dataclass

from selenium.webdriver.common.by import By


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
class PageTasksDataClass:
    title: str
    description: str
    env: str
    version: str
    due_date: str
    assignee_to: str
    tag: str
    priority: str
