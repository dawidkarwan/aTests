from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from src.utils.locator import LoCreator


class CommonLocators:
    DDL = LoCreator.xpath('//div[@class="token-input-dropdown-facebook"]//li')
    TITLE = LoCreator.xpath('//h1[@class="content_title"]')


class CommonActions:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def wait_for_ddl(self):
        self.wait.until(EC.visibility_of_element_located(CommonLocators.DDL))

    def get_page_title(self) -> str:
        return self.driver.find_element(*CommonLocators.TITLE).text
