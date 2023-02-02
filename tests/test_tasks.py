import allure
import pytest
from assertpy import assert_that
from selenium.webdriver.support import expected_conditions as EC

from src.pom.commons.common_actions import CommonActions
from src.pom.page_left_nav import LeftNavPage, LeftNavData
from src.pom.page_modal import ModalPage, ModalLocators
from src.pom.page_tasks import TasksDataClass, TasksPage
from src.utils.get_test_data import get_test_data


@pytest.mark.e2e
class TestTasks:

    @pytest.fixture(autouse=True)
    def setup(self, driver, waiter, set_project):
        self.driver = driver
        self.waiter = waiter
        self.left_nav = LeftNavPage(driver)
        self.tasks = TasksPage(driver)
        self.modal = ModalPage(driver)
        self.left_nav.go_to_tab(LeftNavData.TASK)

    @allure.title("Dodanie zadania")
    @allure.testcase("https://github.com/dawidkarwan/aTests/wiki/1.-Dodanie-nowego-zadania")
    @pytest.mark.parametrize('params', get_test_data('tasks', TasksDataClass))
    def test_add_task(self, params: TasksDataClass):
        self.tasks.add_new_task(params)
        self.waiter.until(EC.visibility_of_element_located(ModalLocators.INFO_MSG))
        with allure.step("Sprawdź komunikat informacyjny"):
            assert_that(self.modal.get_info_msg()).is_equal_to('Zadanie zostało dodane.')

    @allure.title("Anulowanie zadania")
    def test_cancel_task(self):
        self.tasks.cancel_task()
        with allure.step("Sprawdź tytuł strony"):
            assert_that(CommonActions(self.driver).get_page_title()).is_equal_to("Zadania")
