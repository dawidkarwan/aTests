import pytest

from src.page_left_nav import LeftNavPage, LeftNavData
from src.page_tasks import TasksLocators, PageTasksDataClass
from src.utils.get_test_data import get_test_data


class TestTasks:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.left_nav = LeftNavPage(driver)

    @pytest.mark.parametrize('params', get_test_data('tasks', PageTasksDataClass))
    def test_add_task(self, driver, params: PageTasksDataClass):
        self.left_nav.go_to_tab(LeftNavData.TASK.value)
        driver.find_element(*TasksLocators.BUTTON_ADD_TASK).click()
        driver.find_element(*TasksLocators.INPUT_TITLE).send_keys(params.title)
        driver.find_element(*TasksLocators.INPUT_DESCRIPTION).send_keys(params.description)
        driver.find_element(*TasksLocators.INPUT_ENV).send_keys(params.env)
        driver.find_element(*TasksLocators.INPUT_VERSION).send_keys(params.version)
        driver.find_element(*TasksLocators.DDL_PRIORITY).click()
        driver.find_element(*TasksLocators.priority_option(params.priority)).click()
        driver.find_element(*TasksLocators.INPUT_DUE_DATE).send_keys(params.due_date)
        driver.find_element(*TasksLocators.INPUT_ASSIGNEE_TO).send_keys(params.assignee_to)
        driver.find_element(*TasksLocators.INPUT_TAG).send_keys(params.tag)
        driver.find_element(*TasksLocators.BUTTON_SAVE).click()
