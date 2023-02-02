import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait

from src.pom.page_logging import LoggingPage
from src.pom.page_header import HeaderPage


@pytest.fixture
def driver() -> WebDriver:
    driver = Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def waiter(driver) -> WebDriverWait:
    return WebDriverWait(driver, 15)


@pytest.fixture(scope="session")
def url_test_arena() -> str:
    return "http://demo.testarena.pl/"


@pytest.fixture(autouse=True)
def log_in_to_test_arena(driver, url_test_arena):
    driver.get(url_test_arena)
    LoggingPage(driver).log_in()


@pytest.fixture
def set_project(driver):
    project = 'PROJEKT_DK'
    header = HeaderPage(driver)
    if header.get_active_project_name() != project:
        header.change_project(project)
