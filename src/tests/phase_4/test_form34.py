from time import sleep
import unittest

from selenium.webdriver.common.by import By

from src.common.browser import Browser
from src.forms.phase_4.form34 import Form_34
from src.common.constants import Constants as C
from src.common.functions import log_value_of_element


# TODO MOZNOST VOLAT REMEMBER ELEMENT VALUE NA ELEMENT, PRO PRIPADY, KDY SE INPUTY NACTOU SAMI

class Form_34_Tests(unittest.TestCase):
    # TODO refactor testcasu

    def setUp(self):
        self.br = Browser()
        self.f = Form_34(self.br.dr)
        self.br.load_page(self.f.URL_DEBUG)
        # self.br.load_page(self.f.URL)

    def test_zadatel_JE_drzitel(self):
        """
        Test s volbou Drzitel
        LP 2900 s registracni procedurou `NAR` (zobrazeni dalsich inputu)
        """
        f = self.f
        br = self.br

        f.set_checkbox_value(f.CSS_UDAJE_PRAVDIVE)
        f.set_radio_value(f.CSS_JE_DRZITEL)

        f.click_button_by_name("Přidat léčivý přípravek")
        f.load_lp("2900", 0)
        self.assertIn("Tento LP je registrován národním postupem", br.page_source)
        f.load_lp("2901", 1)

        # aby se nasledne zkontrovaly i automaticky nactene inputy
        f.log_readonly_inputs(0)
        f.log_readonly_inputs(1)

        f.ra.randomize_radio_inputs()
        f.ra.randomize_checkbox_inputs()
        f.ra.randomize_datepicker_inputs()
        f.ra.randomize_text_inputs()
        # f.ra.randomize_select_inputs() <-- nelze zde pouzit
        # CSS_JAZYK_NA_OBALU - Specialni select, nelze vycist hodnotu,
        # proto bude kontrolovana explicitne jako text na strance
        f.set_select_value("Francouzština", f.CSS_JAZYK_NA_OBALU.format(0), log_value=False)
        f.set_select_value("Němčina", f.CSS_JAZYK_NA_OBALU.format(1), log_value=False)
        f.set_select_value("Futuna", f.CSS_DRZITEL_STAT.format(0), log_value=True)
        f.set_select_value("Futuna", f.CSS_DRZITEL_STAT.format(1), log_value=True)
        f.ra.randomize_file_inputs()

        self._save_and_upload_json()
        f.clear_attached_files_log()
        f.ra.randomize_file_inputs()

        f.sign_and_send()
        f.check_result()

        # Alespon takto lze select zkontrolovat
        self.assertIn("Francouzština", br.page_source)
        self.assertIn("Němčina", br.page_source)

    def test_zadatel_NEdrzitel_pravicka(self):
        """
        Test s volbou Drzitel
        LP bez registracni procedury NAR
        """
        f = self.f
        br = self.br

        f.set_checkbox_value(f.CSS_UDAJE_PRAVDIVE)
        f.set_radio_value(f.CSS_NENI_DRZITEL)
        f.set_radio_value(f.CSS_JE_PRAVICKA)

        f.load_lp("3000", 0)
        self.assertNotIn("Tento LP je registrován národním postupem", br.page_source)

        # aby se nasledne zkontrovaly i automaticky nactene inputy
        f.log_readonly_inputs(0)

        f.ra.randomize_radio_inputs()
        f.ra.randomize_checkbox_inputs()
        f.ra.randomize_datepicker_inputs()
        f.ra.randomize_text_inputs()
        f.set_select_value("Francouzština", f.CSS_JAZYK_NA_OBALU.format(0), log_value=False)
        f.set_select_value("Futuna", f.CSS_DRZITEL_STAT.format(0))
        f.ra.randomize_file_inputs()

        self._save_and_upload_json()
        f.clear_attached_files_log()
        f.ra.randomize_file_inputs()

        f.sign_and_send()
        f.check_result()

        self.assertIn("Francouzština", br.page_source)

    def test_zadatel_NEdrzitel_fyzicka(self):
        """
        Test s volbou Drzitel
        """
        f = self.f
        br = self.br

        f.set_checkbox_value(f.CSS_UDAJE_PRAVDIVE)
        f.set_radio_value(f.CSS_NENI_DRZITEL)
        f.set_radio_value(f.CSS_JE_FYZICKA)

        f.load_lp("2500", 0)

        f.log_readonly_inputs(0)

        f.ra.randomize_radio_inputs()
        f.ra.randomize_checkbox_inputs()
        f.ra.randomize_datepicker_inputs()
        f.ra.randomize_text_inputs()
        f.set_select_value("Slovenština", f.CSS_JAZYK_NA_OBALU.format(0), log_value=False)
        f.set_select_value("Polština", f.CSS_JAZYK_NA_OBALU.format(0), log_value=False)
        f.set_select_value("Němčina", f.CSS_JAZYK_NA_OBALU.format(0), log_value=False)
        f.set_select_value("Futuna", f.CSS_DRZITEL_STAT.format(0))
        f.ra.randomize_file_inputs()

        self._save_and_upload_json()
        f.clear_attached_files_log()
        f.ra.randomize_file_inputs()

        f.sign_and_send()
        f.check_result()

        self.assertIn("Slovenština", br.page_source)
        self.assertIn("Polština", br.page_source)
        self.assertIn("Němčina", br.page_source)

    def test_LP_neexistuje(self):
        """
        Test nacteni neexistujiciho LP
        """
        f = self.f
        br = self.br

        f.load_lp(500 * "!@#")
        self.assertIn("Zadaný přípravek neexistuje", br.page_source)

    def test_max_opakovani_LP(self):
        """
        Test max. počtu opakování LP včetně odeslání
        """
        f = self.f
        br = self.br

        f.set_checkbox_value(f.CSS_UDAJE_PRAVDIVE)
        f.click_button_by_name("Přidat léčivý přípravek", repeat_cnt=9)
        self.assertNotIn("Přidat léčivý přípravek", br.page_source)

        f.load_lp("1", 0)
        f.load_lp("11", 1)
        f.load_lp("111", 2)
        f.load_lp("2", 3)
        f.load_lp("22", 4)
        f.load_lp("222", 5)
        f.load_lp("3", 6)
        f.load_lp("2900", 7)
        f.load_lp("2900", 8)
        f.load_lp("2900", 9)

        for i in range(0, 10):
            f.log_readonly_inputs(i)

        f.ra.randomize_radio_inputs()
        f.ra.randomize_checkbox_inputs()
        f.ra.randomize_datepicker_inputs()
        f.ra.randomize_text_inputs()

        for i in range(0, 10):
            f.set_select_value("Španělština", f.CSS_JAZYK_NA_OBALU.format(i), log_value=False)
            f.set_select_value("Německo", f.CSS_DRZITEL_STAT.format(i))

        self._save_and_upload_json()
        f.ra.randomize_file_inputs()
        f.clear_attached_files_log()

        f.sign_and_send()
        f.check_result()
        self.assertIn("Španělština", br.page_source)

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
        f.insert_file(br.last_downloaded_file_path, f.XPATH_LOAD_FORM_INPUT, locator_type=By.XPATH, log_value=False)
        sleep(0.5)

    def tearDown(self):
        self.br.print_console_errors()
        self.br.close_browser()


if __name__ == '__main__':
    unittest.main()
