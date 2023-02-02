import allure
import pytest

from assertpy import assert_that

from src.pom.page_header import HeaderLocators


@pytest.mark.common
@allure.title("Logowanie")
def test_logging_test_arena(driver):
    with allure.step("Sprawdź dane użytkownika po zalogowaniu"):
        assert_that(driver.find_element(*HeaderLocators.LABEL_USER).text).contains("Gall Anonim")
