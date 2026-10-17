# Creates the browser named in setup.cfg (based on Tutorial 10).
# Selenium 4.6+ downloads the matching driver automatically (Selenium Manager).
from selenium import webdriver
from helper.helper_base import HelperFunc


def get_browser(browser):
    if browser == "chrome":
        return HelperFunc(webdriver.Chrome())
    if browser == "firefox":
        return HelperFunc(webdriver.Firefox())
    if browser == "edge":
        return HelperFunc(webdriver.Edge())
    raise ValueError(f"Unsupported browser in setup.cfg: {browser}")
