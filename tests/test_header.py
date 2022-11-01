import pytest
from assertpy import assert_that

from src.page_header import HeaderPage


@pytest.mark.common
def test_chose_project(driver):
    project = "Testy bazy danych"
    header = HeaderPage(driver)
    header.change_project(project)
    assert_that(header.get_active_project_name()).is_equal_to(project)
