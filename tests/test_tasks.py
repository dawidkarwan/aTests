import pytest

from src.page_left_nav import LeftNavPage, LeftNavData
from src.page_tasks import TasksDataClass, TasksPage
from src.utils.get_test_data import get_test_data


class TestTasks:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.left_nav = LeftNavPage(driver)
        self.tasks = TasksPage(driver)

    @pytest.mark.parametrize('params', get_test_data('tasks', TasksDataClass))
    def test_add_task(self, params: TasksDataClass):
        self.left_nav.go_to_tab(LeftNavData.TASK.value)
        self.tasks.fill_new_task_fields(params)
