import time
import unittest

import HtmlTestRunner

from src.common.constants import Constantsonstants
from src import Constantsfg
from src.forms.phase_1.form2 import Form_2


class Form_2_Tests(unittest.TestCase):

    def setUp(self):
        self.f = Form_2()
        self.f.load_page(self.f.URL)
        cfg.element_values_log = {}

    def test_S_kodem_sukl(self):
        f = self.f

        f.set_radio_value(f.CSS_CESTNE_PROHLASENI_CHECK)
        f.set_radio_value(f.CSS_S_KODEM_RADIO)
        f.set_radio_value(f.CSS_PLNA_MOC_PREDKLADA_RADIO)
        f.write_to_textbox("1559", f.CSS_KOD_SUKL_TXT)
        f.click_button_by_name("Načíst přípravek")

        f.ra.randomize_radio_inputs()
        f.ra.randomize_checkbox_inputs()
        f.ra.randomize_datepicker_inputs()

        f.ra.randomize_select_inputs()
        time.sleep(60)
        f.click_button_by_name("Přidat stát")
        f.ra.randomize_text_inputs()
        f.ra.randomize_file_inputs()

        f.click_button_by_name("Uložit formulář")
        time.sleep(50000)
        # f.submit_form("Odeslat formulář")

    def test_BEZ_kodu_sukl(self):
        f = self.f

        f.find_and_check_switch(f.CSS_CESTNE_PROHLASENI_CHECK)

        f.ra.randomize_radio_inputs()
        f.ra.randomize_checkbox_inputs()
        f.ra.randomize_text_inputs()
        f.ra.randomize_select_inputs()
        f.ra.randomize_file_inputs()
        f.submit_form("Odeslat formulář")

    def test_experimental(self):
        f = self.f
        f.ra.randomize_radio_inputs()
        f.click_button_by_name("Uložit formulář")
        f.click_button_by_name("Načíst formulář")
        time.sleep(50)

    def tearDown(self):
        self.f.dr.close()


if __name__ == '__main__':
    unittest.main()
