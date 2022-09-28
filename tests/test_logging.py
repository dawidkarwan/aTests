import allure

from src.page_logging import LoggingPage
from assertpy import assert_that


def test_logging_test_arena(driver, url_test_arena):
    driver.get(url_test_arena)
    LoggingPage(driver).log_in()
    with allure.step("Sprawdź dane użytkownika po zalogowaniu"):
        assert_that(driver.find_element("xpath", "//*[@class='user-info']").text).contains("Gall Anonim")
