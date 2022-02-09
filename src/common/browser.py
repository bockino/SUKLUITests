import glob
import json
import os
import time
from unittest import TestCase

from selenium.common.exceptions import InvalidArgumentException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from src.common import globals as G
from src.common.constants import Constants as C
from src.common.driver_init import driver_inicialize


class Browser:
    def __init__(self):
        self.dr = driver_inicialize()

    def load_page(self, url):
        self.dr.get(url)
        time.sleep(C.SECS_MIDDLE)

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

    def check_result(self):
        time.sleep(C.SECS_MIDDLE)
        self._assert_entered_values()
        self._check_console_errors()

    def _assert_entered_values(self):
        """
        Po odeslani formulare vycte z response odkaz na vyplneny formular
        Prejde na vyplneny formualar
        Porovna hodnoty ve formulari s predchozimi vyplnenymi hodnotami // overit
        """

        ac = ActionChains(self.dr)
        tc = TestCase()

        def _log_filter(log_):
            return (
                    log_["method"] == "Network.responseReceived" and
                    "json" in log_["params"]["response"]["mimeType"] and
                    log_["params"]["response"]["url"] == "https://server.dev.eforms.qcm.cz/api/submissions"
            )

        public_id = ''
        logs_raw = self.dr.get_log("performance")
        logs = [json.loads(lr["message"])["message"] for lr in logs_raw]
        for log in filter(_log_filter, logs):
            request_id = log["params"]["requestId"]
            body_str = self.dr.execute_cdp_cmd("Network.getResponseBody", {"requestId": request_id})
            public_id = (json.loads(body_str["body"]))["publicId"]

        if not public_id:
            tc.fail("nepodarilo se vycist public_id z response, mozna formular nebyl odeslan")

        self.dr.get(C.SAVED_FORM_URL_BASE + public_id)
        time.sleep(C.SECS_MIDDLE)

        for _ in G.entered_values:
            item = G.entered_values[_]
            print(f"\nassert hodnoty inputu {item['id']}", end='')
            element = self.dr.find_element(By.CSS_SELECTOR, f'[id^="{item["id"]}"]')

            ac.move_to_element(element)
            ac.perform()
            ac.reset_actions()

            real_value = element.get_attribute("value")
            submitted_value = item["value"]

            print(f"; zadana hodnota: '{submitted_value}' VS. ulozena hodnota: '{real_value}'", end='')
            tc.assertEqual(real_value, submitted_value, item["id"])

            if item["is_checkable"]:
                print("; assert stavu checked/unchecked", end='')
                tc.assertEqual(bool(element.get_attribute("checked")), item["is_checked"],
                               f"nesouhlasi stav checked/unchecked elementu {item['id']}")

    def _check_console_errors(self):
        # TODO assert na errory

        print()
        print("Browser log: ", end="")
        for e in self.dr.get_log('browser'):
            print(e)
        print("Driver log:", end="")
        for e in self.dr.get_log('driver'):
            print(e)

        try:
            print("Server log:", end="")
            for e in self.dr.get_log('server'):
                print(e)
        except InvalidArgumentException:
            print('nepodaril se vycist server log')

        try:
            print("Client log:", end="")
            for e in self.dr.get_log('client'):
                print(e)
        except InvalidArgumentException:
            print('nepodaril se vycist client log')
