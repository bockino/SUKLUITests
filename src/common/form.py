import json
import re
import sys
import time
from unittest import TestCase

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from src.common import globals as G
from src.common.constants import Constants
from src.common.functions import CommonElementActions
from src.common.functions import log_value_of_element
from src.common.randomize import Randomize


class Form:
    # Elementy spolecne pro vsechny formulare
    XPATH_BERU_NA_VEDOMI = "/html/body/div[2]/div[3]/div/div/button"

    def __init__(self, driver, naming_rules):
        self.dr = driver
        self.ra = Randomize(self.dr)
        self._ac = ActionChains(self.dr)
        self._naming_rules = naming_rules
        self._cea = CommonElementActions(self.dr)
        self._tc = TestCase()
        self.const = Constants()

        self.clear_element_values_log()
        self.clear_attached_files_log()

    @staticmethod
    def clear_element_values_log():
        G.element_values_log = {}

    @staticmethod
    def clear_attached_files_log():
        G.attached_files_log = {}

    def click_button_by_name(self, button_text, index=0, repeat_cnt=1):
        for _ in range(0, repeat_cnt):
            buttons = self.dr.find_elements(By.XPATH, f"//button[text()='{button_text}']")
            # todo naslo to?
            buttons[index].click()

    def write_to_textbox(self, value, locator_string, locator_type=By.CSS_SELECTOR,
                         index=0, log_value=True, explicit_assert_value=None):
        textboxes = self.dr.find_elements(locator_type, locator_string)
        textboxes[index].send_keys(value)
        if log_value:
            log_value_of_element(textboxes[index], explicit_assert_value=explicit_assert_value)

    def set_radio_value(self, locator_string, locator_type=By.CSS_SELECTOR, index=0,
                        log_value=True):
        switches = self.dr.find_elements(locator_type, locator_string)
        self._cea.precise_click(switches[index])
        if log_value:
            log_value_of_element(switches[index])

    def set_checkbox_value(self, locator_string, set_checked=True, locator_type=By.CSS_SELECTOR, index=0,
                           log_value=True):
        # TODO predelato statni funkce po vzoru teto?
        # todo a jeste pridat kontrolu poctu nalezenych vuci indexu pozadovaneho
        switches = self.dr.find_elements(locator_type, locator_string)
        switch = switches[index]
        is_checked = bool(switch.get_attribute("checked"))
        if is_checked != set_checked:
            self._cea.precise_click(switch)
        if log_value:
            log_value_of_element(switch)

    def insert_file(self, file_path, locator_string=By.CSS_SELECTOR, locator_type=By.CSS_SELECTOR,
                    index=0, log_value=True, explicit_assert_value=None):
        file_inputs = self.dr.find_elements(locator_type, locator_string)
        file_input = file_inputs[index]
        file_input.send_keys(file_path)
        if log_value:
            log_value_of_element(file_input, explicit_assert_value=explicit_assert_value)

    def set_select_value(self, text_option, locator_string, locator_type=By.CSS_SELECTOR, index=0,
                         log_value=True):
        selects = self.dr.find_elements(locator_type, locator_string)
        select = selects[index]
        Select(select).select_by_visible_text(text_option)
        if log_value:
            log_value_of_element(select)

    def check_result(self):
        self._wait_form_sent()
        self._load_filled_form()
        self._assert_entered_values()
        self._assert_attached_files()

    def _wait_form_sent(self):
        self._tc.assertNotIn("Políčko nemůže být prázdné.", self.dr.page_source)
        self._tc.assertNotIn("Email není ve správném formátu.", self.dr.page_source)
        self._tc.assertNotIn("Telefonní číslo není ve správném formátu.", self.dr.page_source)
        self.dr.implicitly_wait(30)
        self.dr.find_element(By.XPATH, self.XPATH_BERU_NA_VEDOMI)
        self._tc.assertIn("Formulář byl úspěšně odeslán.", self.dr.page_source)

    def _assert_attached_files(self):
        new_expected_names = []
        for input_name in G.attached_files_log:
            original_file_names = G.attached_files_log[input_name]
            for original_file_name in original_file_names:
                found_match = False
                for pattern in self._naming_rules:
                    if re.search(pattern, input_name):
                        found_match = True
                        expected_file_name = self._naming_rules[pattern] + original_file_name
                        if re.search(r"\{\}", expected_file_name):
                            # je potreba dohledat index v name inputu - ten se projevi v nazvu souboru
                            match = re.search(r"(?<=\/)\d*(?=\/)", input_name)
                            if match:
                                index = int(match.group()) + 1
                                expected_file_name = expected_file_name.format(index)
                            else:
                                sys.exit("nepodarilo se vycist index z attributu name")
                        new_expected_names.append(expected_file_name)
                        continue
                if not found_match:
                    # neni zadan prefix souboru - bude ocekavana a kontrolovan originalni nazev
                    new_expected_names.append(original_file_name)

        print(f"\nassert ocekavanych nazvu souboru: {new_expected_names}")
        for expected_file_name in new_expected_names:
            self._tc.assertIn(expected_file_name, self.dr.page_source)

    def _load_filled_form(self):
        def _log_filter(log_):
            return (
                    log_["method"] == "Network.responseReceived" and
                    "json" in log_["params"]["response"]["mimeType"] and
                    log_["params"]["response"]["url"] == self.const.instance_url + "api/submissions"
            )
        public_id = ''
        logs_raw = self.dr.get_log("performance")
        logs = [json.loads(lr["message"])["message"] for lr in logs_raw]
        for log in filter(_log_filter, logs):
            request_id = log["params"]["requestId"]
            body_str = self.dr.execute_cdp_cmd("Network.getResponseBody", {"requestId": request_id})
            public_id = (json.loads(body_str["body"]))["publicId"]

        if public_id:
            self.dr.get(self.const.SAVED_FORM_URL_BASE + public_id)
        else:
            exit("asdfasdfasdfasdfasdfasdfasfddasf")

    def _assert_entered_values(self):
        """
        Porovna hodnoty v nactenem vyplnenem formulari s predchozimi vyplnenymi hodnotami
        """
        for element_id in G.element_values_log.keys():
            element_entered_value = G.element_values_log[element_id]['entered_value']
            element_is_checkable = G.element_values_log[element_id]['is_checkable']
            element_is_checked = G.element_values_log[element_id]['is_checked']

            print(f"\nassert hodnoty inputu {element_id}", end='; ')
            selector = f'[id^="{element_id}"]'

            # Muze se stat, ze je prvni nalezen nespravny element, pokud napr.
            # - hledam /lecivePripravky/0/sarzeInformace/zduvodneni, ale je nalezen
            # - /lecivePripravky/0/sarzeInformace/zduvodneniZadosti
            # - protoze pouzivam id^= kvuli odfiltrovani nahodnych cisel na konci name/id
            elements = self.dr.find_elements(By.CSS_SELECTOR, selector)
            if len(elements) > 1:
                print("\nwarning: nalezeno vice elementu, kontrola preskocena")
                continue
            element = elements[0]

            real_value = element.get_attribute("value")

            print(f"zadana hodnota: '{element_entered_value}' VS. ulozena hodnota: '{real_value}'", end='')
            self._tc.assertEqual(real_value, element_entered_value, element_id)

            if element_is_checkable:
                print("; assert stavu checked/unchecked", end='')
                self._tc.assertEqual(bool(element.get_attribute("checked")), element_is_checked,
                                     f"nesouhlasi {element_id}")



