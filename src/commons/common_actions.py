from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CommonLocators:
    DDL = (By.XPATH, '//div[@class="token-input-dropdown-facebook"]//li')


class CommonActions:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def wait_for_ddl(self):
        self.wait.until(EC.visibility_of_element_located(CommonLocators.DDL))
