import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webdriver import WebDriver

from src.page_logging import LoggingPage


@pytest.fixture
def driver() -> WebDriver:
    driver = Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def url_test_arena() -> str:
    return "http://demo.testarena.pl/"


@pytest.fixture()
def log_in_to_test_arena(driver, url_test_arena):
    driver.get(url_test_arena)
    LoggingPage(driver).log_in()
