import allure
import pytest

from assertpy import assert_that


@pytest.mark.common
@allure.title("Logowanie")
def test_logging_test_arena(driver):
    with allure.step("Sprawdź dane użytkownika po zalogowaniu"):
        assert_that(driver.find_element("xpath", "//*[@class='user-info']").text).contains("Gall Anonim")
