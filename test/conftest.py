import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.fixture
def driver() -> WebDriver:
    driver = Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def url_test_arena() -> str:
    return "http://demo.testarena.pl/"
