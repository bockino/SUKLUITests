from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from src.common.constants import Constants


def driver_inicialize():
    # TODO nepredavam to driveru, presto funguje.. kdzy to predam jako desired_capabilities, je to deprecated
    # make chrome log requests
    capabilities = DesiredCapabilities.CHROME
    capabilities["goog:loggingPrefs"] = {"performance": "ALL"}

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    prefs = {"download.default_directory": Constants.DOWNLOADS_FOLDER_PATH}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    if Constants.RUN_HEADLESS:
        chrome_options.add_argument('-headless')

    service = Service(executable_path="chromedriver.exe")

    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(Constants.TIME_TINY)
    return driver
