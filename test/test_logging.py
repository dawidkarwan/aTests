

from src.page_logging import LoggingPage


def test_logging_test_arena(driver, url_test_arena):
    driver.get(url_test_arena)
    LoggingPage(driver).log_in()
    assert driver.find_element("xpath", "//*[@class='user-info']").text.split()[0] == "Gall"

