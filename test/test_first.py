from selenium import webdriver

driver = webdriver.Chrome()


def test_open_test_arena_login_page():
    driver.get("http://demo.testarena.pl/")
    assert driver.find_element(value="login").get_attribute("value") == "Zaloguj"
    driver.quit()
