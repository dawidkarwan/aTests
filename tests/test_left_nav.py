from assertpy import assert_that

from src.page_left_nav import LeftNavPage
from src.page_left_nav import LeftNavData as tabs
from src.page_tasks import TasksLocators


def test_left_nav_switch_tabs(driver):
    left_nav = LeftNavPage(driver)
    left_nav.go_to_tab(tabs.TASK)
    assert_that(driver.find_element(*TasksLocators.TITLE).text).is_equal_to("Zadania")
