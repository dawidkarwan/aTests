import pytest
from assertpy import assert_that

from src.commons.common_actions import CommonActions
from src.page_left_nav import LeftNavPage
from src.page_left_nav import LeftNavData as tabs


@pytest.mark.common
def test_left_nav_switch_tabs(driver):
    left_nav = LeftNavPage(driver)
    left_nav.go_to_tab(tabs.TASK)
    assert_that(CommonActions(driver).get_page_title()).is_equal_to("Zadania")
