# Wrapper around Selenium WebDriver (based on Tutorial 10).
# Every find_* method uses an explicit wait instead of time.sleep(),
# so tests wait only until the element is ready.
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://ecommerce-playground.lambdatest.io/index.php?route="


def unique_email(prefix="tester"):
    # public site shared by many students, so every new account needs a unique email
    return f"{prefix}_{int(time.time() * 1000)}@example.com"


class HelperFunc(object):
    __TIMEOUT = 10  # seconds to wait for an element before failing

    def __init__(self, driver):
        super(HelperFunc, self).__init__()
        self._driver_wait = WebDriverWait(driver, HelperFunc.__TIMEOUT)
        self._driver = driver

    # ---- browser actions ----
    def open(self, url):
        self._driver.get(url)

    def open_route(self, route):
        # e.g. open_route("account/login")
        self._driver.get(BASE_URL + route)

    def maximize(self):
        self._driver.maximize_window()

    def delete_cookies(self):
        # clears the session so each scenario starts logged out with an empty cart
        self._driver.delete_all_cookies()

    def screenshot(self, path):
        self._driver.save_screenshot(path)

    def close(self):
        self._driver.quit()

    @property
    def page_source(self):
        return self._driver.page_source

    # ---- element locators (wait until visible) ----
    def find_by_id(self, id):
        return self._driver_wait.until(EC.visibility_of_element_located((By.ID, id)))

    def find_by_name(self, name):
        return self._driver_wait.until(EC.visibility_of_element_located((By.NAME, name)))

    def find_by_xpath(self, xpath):
        return self._driver_wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

    def find_by_css(self, css):
        return self._driver_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css)))

    def click_by_css(self, css):
        # waits until the element is clickable, then clicks it
        self._driver_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, css))).click()

    def wait_for_text(self, text):
        # waits until the given text appears anywhere on the page
        return self._driver_wait.until(
            EC.visibility_of_element_located((By.XPATH, f"//*[contains(normalize-space(.), \"{text}\")]"))
        )
