import unittest
from time import sleep, time

from selenium.webdriver.common.by import By

from src.common.browser import Browser
from src.forms.phase_4.form20 import Form_20


class Form_20_Tests(unittest.TestCase):

    def setUp(self):
        self.br = Browser()
        self.f = Form_20(self.br.dr)
        self.br.load_page(self.f.url_debug, self.f.form_title)
        # self.br.load_page(self.f.url)

    def test_distributor_dle_ic(self):
        """
        """
        f = self.f
        f.write_to_textbox("25635964", f.CSS_ZADATEL_IC)
        f.click_button_by_name("Načíst distributora podle IČ")

        f.write_to_textbox("Gynekologická ambulance MUDr. Karla Hrabcová s.r.o.", f.CSS_ZDRAVOTNICKE_ZARIZENI_NAZEV.format(0))
        f.click_button_by_name("Načíst zařízení podle názvu")
        sleep(2)
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
        f.write_to_textbox("JK - Trading spol. s r.o.", f.CSS_ZADATEL_NAZEV)
        f.click_button_by_name("Načíst distributora podle názvu")

        f.write_to_textbox("Gynekologická ambulance MUDr. Karla Hrabcová s.r.o.", f.CSS_ZDRAVOTNICKE_ZARIZENI_NAZEV.format(0))
        f.click_button_by_name("Načíst zařízení podle názvu")
        sleep(2)
        f.log_readonly_inputs()
        f.ra.randomize_radio_inputs()
        f.ra.randomize_checkbox_inputs()
        f.ra.randomize_datepicker_inputs()
        f.ra.randomize_text_inputs()
        f.ra.randomize_select_inputs()
        f.ra.randomize_file_inputs()

        f.sign_and_send_form()
        f.check_result()

    def test_distributor_ze_seznamu(self):
        """
        """
        f = self.f
        f.write_to_textbox("N", f.CSS_ZADATEL_NAZEV, log_value=False)
        f.click_button_by_name("Načíst distributora podle názvu")
        sleep(2)
        f.set_select_value("NELCORE s.r.o.", f.XPATH_VYBERTE_DISTRIBUTORA, locator_type=By.XPATH, log_value=False)

        f.write_to_textbox("Gynekologická ambulance MUDr. Karla Hrabcová s.r.o.", f.CSS_ZDRAVOTNICKE_ZARIZENI_NAZEV.format(0))
        f.click_button_by_name("Načíst zařízení podle názvu")
        sleep(2)

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

    def test_opakovani_a_nacteni_json(self):
        """
        """
        f = self.f

        f.click_button_by_name("Přidat léčivou látku", repeat_cnt=2)
        f.click_button_by_name("Přidat zdravotnické zařízení", repeat_cnt=2)

        f.write_to_textbox("25635964", f.CSS_ZADATEL_IC)
        f.click_button_by_name("Načíst distributora podle IČ")

        f.write_to_textbox("Gynekologická ambulance MUDr. Karla Hrabcová s.r.o.",
                           f.CSS_ZDRAVOTNICKE_ZARIZENI_NAZEV.format(0))
        f.click_button_by_name("Načíst zařízení podle názvu")

        f.write_to_textbox("AAA-dent s.r.o.",
                           f.CSS_ZDRAVOTNICKE_ZARIZENI_NAZEV.format(1))
        f.click_button_by_name("Načíst zařízení podle názvu")

        f.write_to_textbox("Nestátní zdravotnické zařízení Ordinace praktického lékaře pro dospělé MUDr. Dvořáková Iva",
                           f.CSS_ZDRAVOTNICKE_ZARIZENI_NAZEV.format(2))
        f.click_button_by_name("Načíst zařízení podle názvu")

        sleep(2)
        f.log_readonly_inputs()

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

    # ------------------------------------------------------------------------

    def _save_and_load_json(self):
        f = self.f
        br = self.br

        sleep(1)
        f.click_button_by_name("Stáhnout formulář v PDF")
        f.click_button_by_name("Uložit formulář")
        br.refresh_page("Státní ústav pro kontrolu léčiv")
        f.insert_file(br.last_downloaded_file_path, f.XPATH_NACIST_FORMULAR, locator_type=By.XPATH, log_value=False)
        sleep(0.5)

    def tearDown(self):
        # todo kdyz test neprojde udelat printscreen?
        self.br.save_screenshot(self._testMethodName)
        self.br.print_console_errors()
        self.br.close_browser()


if __name__ == '__main__':
    unittest.main()
