from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from src.common.constants import Settings as S
from src.common.constants import Constants as C


def driver_inicialize():
    # make chrome log requests
    # TODO nepredavam to driveru, presto funguje.. kdzy to predam jako desired_capabilities, je to deprecated
    capabilities = DesiredCapabilities.CHROME
    capabilities["goog:loggingPrefs"] = {"performance": "ALL"}

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    prefs = {"download.default_directory": C.DOWNLOADS_FOLDER_PATH}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    if S.RUN_HEADLESS:
        chrome_options.add_argument('-headless')

    service = Service(executable_path="chromedriver.exe")

    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(S.DRIVER_WAIT)
    return driver
