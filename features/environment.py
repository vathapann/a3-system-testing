# Behave hooks (based on Tutorial 10).
import os
from configparser import ConfigParser
from helper.helper_web import get_browser


def before_all(context):
    # read the browser type from setup.cfg and open it once for the whole run
    config = ConfigParser()
    config.read(os.path.join(os.getcwd(), "setup.cfg"))
    context.helperfunc = get_browser(config.get("Environment", "Browser"))
    context.helperfunc.maximize()


def before_scenario(context, scenario):
    # start every scenario with a clean session (logged out, empty cart)
    context.helperfunc.open_route("common/home")
    context.helperfunc.delete_cookies()


def after_scenario(context, scenario):
    # save a screenshot of every scenario result for the report
    os.makedirs("screenshots", exist_ok=True)
    safe_name = "".join(c if c.isalnum() else "_" for c in scenario.name)[:80]
    context.helperfunc.screenshot(f"screenshots/{scenario.status.name}_{safe_name}.png")


def after_all(context):
    context.helperfunc.close()