import unittest
from time import sleep

from selenium.webdriver.common.by import By

from src.common.browser import Browser
from src.forms.phase_4.form20 import Form_20


class Form_20_Tests(unittest.TestCase):

    def setUp(self):
        self.br = Browser()
        self.f = Form_20(self.br.dr)
        self.br.load_page(self.f.url_debug)

    def test_distributor_dle_ic(self):
        """
        """
        f = self.f
        f.write_to_textbox("25635964", f.CSS_ZADATEL_IC)
        f.click_button_by_name("Načíst distributora podle IČ")
        f.log_readonly_inputs()
        f.set_checkbox_value(f.CSS_PREVZIT_ADRESU, set_checked=False)
        f.ra.randomize_radio_inputs()
        f.ra.randomize_checkbox_inputs()
        f.ra.randomize_datepicker_inputs()
        f.ra.randomize_text_inputs()
        f.ra.randomize_select_inputs()
        f.ra.randomize_file_inputs()

        f.sign_and_send_form()
        f.check_result()

    def test_distributor_dle_nazvu(self):
        """
        """
        f = self.f
        f.write_to_textbox("25635964", f.CSS_ZADATEL_NAZEV)
        f.click_button_by_name("Načíst distributora podle názvu")
        f.log_readonly_inputs()
        f.set_checkbox_value(f.CSS_PREVZIT_ADRESU, set_checked=True)
        f.ra.randomize_radio_inputs()
        f.ra.randomize_checkbox_inputs()
        f.ra.randomize_datepicker_inputs()
        f.ra.randomize_text_inputs()
        f.ra.randomize_select_inputs()
        f.ra.randomize_file_inputs()

        f.sign_and_send_form()
        f.check_result()

    def test_nacist_formular_z_json(self):
        """
        """
        f = self.f

        f.write_to_textbox("25635964", f.CSS_ZADATEL_IC)
        f.click_button_by_name("Načíst distributora podle IČ")
        sleep(0.5)
        f.log_readonly_inputs()
        f.click_button_by_name("Přidat léčivou látku", repeat_cnt=2)

        f.ra.randomize_radio_inputs()
        f.ra.randomize_checkbox_inputs()
        f.ra.randomize_datepicker_inputs()
        f.ra.randomize_text_inputs()
        f.ra.randomize_select_inputs()
        f.ra.randomize_file_inputs()

        self._save_and_load_json()
        f.clear_attached_files_log()
        f.ra.randomize_file_inputs()

        f.sign_and_send_form()
        f.check_result()

    def test_qwer(self):
        """
        """
        f = self.f
        self.br.dr.find_element(f.XPATH_NACIST_FORMULAR, By.XPATH).click()

    # ------------------------------------------------------------------------
    # pomocne funkce

    def _save_and_load_json(self):
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
