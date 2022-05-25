import glob
import os
from telnetlib import EC
from time import sleep, time

from selenium.common.exceptions import InvalidArgumentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from src.common.constants import Constants
from src.common.driver_init import driver_inicialize


class Browser:

    def __init__(self):
        self.dr = driver_inicialize()
        # self.page_source = self.dr.page_source
        # todo mozna pridat objekt tridy FormXZ
        # todo mozna pridat objekt tridy Result

    def load_page(self, url, wait_text):
        self.dr.get(url)
        self.wait_till_text_visible(wait_text)

    @property
    def page_source(self):
        return self.dr.page_source

    def close_browser(self):
        self.dr.close()
        self.dr.quit()

    def refresh_page(self, wait_text):
        self.dr.refresh()
        self.wait_till_text_visible(wait_text)

    def wait_till_element_visible(self, element_locator, locator_type=By.XPATH):
        # self.dr.wait.until(EC.visibility_of_element_located((locator_type, element_locator)))
        WebDriverWait(self.dr, 10).until(EC.visibility_of_element_located((locator_type, element_locator)))

    def wait_till_text_visible(self, text):
        while not (text in self.dr.page_source):
            sleep(0.1)

    def save_screenshot(self, test_name):
        self.dr.save_screenshot("{} : {}".format(test_name, time()))

    @property
    def last_downloaded_file_path(self):
        # TODO co kdyz je slozka prazdna?
        newest_json = sorted(glob.glob(f"{Constants.DOWNLOADS_FOLDER_PATH}\\*.json"), key=os.path.getctime)[-1]
        if not newest_json:
            exit("nenalezen zadny stazenny soubor")
        print(newest_json)
        return newest_json

    def print_console_errors(self):
        # TODO assert na errory
        print("\nBrowser log: ", end='')
        for e in self.dr.get_log('browser'):
            print(e)
        print("\nDriver log:", end='')
        for e in self.dr.get_log('driver'):
            print(e)
        try:
            print("\nServer log:", end='')
            for e in self.dr.get_log('server'):
                print(e)
        except InvalidArgumentException:
            print('nepodaril se vycist server log', end='')
        try:
            print("\nClient log:", end='')
            for e in self.dr.get_log('client'):
                print(e)
        except InvalidArgumentException:
            print("nepodaril se vycist client log", end='')
