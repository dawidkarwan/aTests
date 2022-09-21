from selenium import webdriver

from src.page_logging import LoggingPage

driver = webdriver.Chrome()


def test_logging_test_arena():
    driver.get("http://demo.testarena.pl/")
    LoggingPage(driver).log_in()
    assert driver.find_element("xpath", "//*[@class='user-info']").text.split()[0] == "Gall"
    driver.quit()
