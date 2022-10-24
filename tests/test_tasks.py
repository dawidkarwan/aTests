import pytest
from assertpy import assert_that
from selenium.webdriver.support import expected_conditions as EC

from src.page_left_nav import LeftNavPage, LeftNavData
from src.page_modal import ModalPage, ModalLocators
from src.page_tasks import TasksDataClass, TasksPage
from src.utils.get_test_data import get_test_data


@pytest.mark.e2e
class TestTasks:

    @pytest.fixture(autouse=True)
    def setup(self, driver, waiter):
        self.driver = driver
        self.waiter = waiter
        self.left_nav = LeftNavPage(driver)
        self.tasks = TasksPage(driver)
        self.modal = ModalPage(driver)

    @pytest.mark.parametrize('params', get_test_data('tasks', TasksDataClass))
    def test_add_task(self, params: TasksDataClass):
        self.left_nav.go_to_tab(LeftNavData.TASK)
        self.tasks.fill_new_task_fields(params)
        self.waiter.until(EC.visibility_of_element_located(ModalLocators.INFO_MSG))
        assert_that(self.modal.get_info_msg()).is_equal_to('Zadanie zostało dodane.')
