import time
import unittest
from time import sleep

from selenium.webdriver.common.by import By

from src.common.browser import Browser
from src.forms.phase_4.form20 import Form_20


class Form_20_Tests(unittest.TestCase):

    def setUp(self):
        self.br = Browser()
        self.f = Form_20(self.br.dr)
        self.br.load_page(self.f.URL_DEBUG)
        # self.br.load_page(self.f.URL)

    def test_asdf(self):
        """
        """
        f = self.f

        f.write_to_textbox("25635964", f.CSS_ZADATEL_IC)
        f.click_button_by_name("Načíst distributora podle IČ")
        # f.set_checkbox_value(f.CSS_PREVZIT_ADRESU, set_checked=False)

        # f.click_button_by_name("Přidat léčivou látku")

        f.ra.randomize_radio_inputs()
        f.ra.randomize_checkbox_inputs()
        f.ra.randomize_datepicker_inputs()
        f.ra.randomize_text_inputs()
        f.ra.randomize_select_inputs()
        f.ra.randomize_file_inputs()

        sleep(5)
        f.click_button_by_name("Elektronicky podepsat formulář")
        sleep(0.5)
        f.click_button_by_name("Odeslat podepsaný formulář")
        f.check_result()

    def test_nacteni_jsonu(self):
        """
        """
        f = self.f

        f.write_to_textbox("25635964", f.CSS_ZADATEL_IC)
        f.click_button_by_name("Načíst distributora podle IČ")
        f.log_readonly_inputs()

        f.ra.randomize_radio_inputs()
        f.ra.randomize_checkbox_inputs()
        f.ra.randomize_datepicker_inputs()
        f.ra.randomize_text_inputs()
        f.ra.randomize_select_inputs()
        f.ra.randomize_file_inputs()

        self._save_and_upload_json()
        f.clear_attached_files_log()
        f.ra.randomize_file_inputs()

        f.sign_and_send()
        f.check_result()

    def test_qwer(self):
        """
        """
        f = self.f
        self.br.dr.find_element(f.XPATH_NACIST_FORMULAR, By.XPATH).click()

    # ------------------------------------------------------------------------
    # pomocne funkce

    def _save_and_upload_json(self):
        f = self.f
        br = self.br

        sleep(2)
        f.click_button_by_name("Stáhnout formulář v PDF")
        sleep(0.5)
        f.click_button_by_name("Uložit formulář")
        sleep(0.5)
        br.dr.refresh()
        sleep(0.5)
        f.insert_file(br.last_downloaded_file_path, f.XPATH_NACIST_FORMULAR, locator_type=By.XPATH, log_value=False)
        sleep(0.5)

    def tearDown(self):
        self.br.print_console_errors()
        self.br.close_browser()


if __name__ == '__main__':
    unittest.main()
