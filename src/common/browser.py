import glob
import os
import time

from selenium.common.exceptions import InvalidArgumentException

from src.common.constants import Constants as C
from src.common.driver_init import driver_inicialize


class Browser:

    def __init__(self):
        self.dr = driver_inicialize()
        # self.page_source = self.dr.page_source
        # todo mozna pridat objekt tridy FormXZ
        # todo mozna pridat objekt tridy Result

    def load_page(self, url):
        self.dr.get(url)
        time.sleep(C.TIME_MIDDLE)

    @property
    def page_source(self):
        return self.dr.page_source

    def close_browser(self):
        self.dr.close()
        self.dr.quit()

    @property
    def last_downloaded_file_path(self):
        # TODO co kdyz je slozka prazdna?
        newest_json = sorted(glob.glob(f"{C.DOWNLOADS_FOLDER_PATH}\\*.json"), key=os.path.getctime)[-1]
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
