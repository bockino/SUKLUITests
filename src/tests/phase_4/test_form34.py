import time
from time import sleep
import unittest

from selenium.webdriver.common.by import By

from src.common.browser import Browser
from src.forms.phase_4.form34 import Form_34
from src.common.constants import Constants as C


class Form_34_Tests(unittest.TestCase):

    def setUp(self):
        self.br = Browser()
        self.f = Form_34(self.br.dr)
        self.br.load_page(self.f.URL_DEBUG)

    def test_zadatel_JE_drzitel(self):
        f = self.f
        br = self.br
        br.load_page(f.URL)

        # time.sleep(500)
        f.find_and_check_checkbox(f.CSS_UDAJE_PRAVDIVE)
        f.find_and_click_radio(f.CSS_ZADATEL_JE_DRZITEL)
        # f.find_and_click_button("Přidat léčivý přípravek")
        f.find_and_write_textbox("150", f.CSS_KOD_PRIPRAVKU_DEFAULT.format("0"), explicit_assert_value="0000150")
        f.find_and_click_button("Načíst přípravek", index=0)
        sleep(C.SECS_SHORT)
        # f.find_and_write_textbox("2900", f.CSS_KOD_PRIPRAVKU_DEFAULT.format("1"), explicit_assert_value="0002900")
        # f.find_and_click_button("Načíst přípravek", index=1)
        # sleep(C.SECS_SHORT)

        f.ra.randomize_radio_buttons()
        f.ra.randomize_checkbox_inputs()
        f.ra.randomize_datepicker_inputs()
        f.ra.randomize_text_inputs()
        f.ra.randomize_select_inputs()
        f.ra.randomize_file_inputs()

        sleep(5000)

        # f.find_and_click_button("Elektronicky podepsat formulář")
        # sleep(C.SECS_SHORT)
        # f.find_and_click_button("Odeslat podepsaný formulář")

        # sleep(C.SECS_SHORT)
        # f.find_and_click_button("Odeslat")

        br.check_result()

    def test_stahnout_json(self):
        f = self.f

        f.find_and_check_checkbox(f.CSS_UDAJE_PRAVDIVE)
        f.find_and_click_radio(f.CSS_ZADATEL_JE_DRZITEL)
        f.find_and_write_textbox("150", f.CSS_KOD_PRIPRAVKU_DEFAULT.format("0"), explicit_assert_value="0000150")
        f.find_and_click_button("Načíst přípravek", index=0)
        sleep(C.SECS_SHORT)

        f.ra.randomize_radio_buttons()
        f.ra.randomize_checkbox_inputs()
        f.ra.randomize_datepicker_inputs()
        f.ra.randomize_text_inputs()
        f.ra.randomize_select_inputs()
        f.ra.randomize_file_inputs()
        sleep(C.SECS_SHORT)
        f.find_and_click_button("Uložit formulář")
        sleep(C.SECS_SHORT)
        f.find_and_write_textbox(f.last_downloaded_file_path, f.SEKLECTOR_LOAD_FORM_INPUT, By.CSS_SELECTOR, remember_value=False)
        sleep(500)

    def tearDown(self):
        self.f.dr.close()


if __name__ == '__main__':
    unittest.main()
