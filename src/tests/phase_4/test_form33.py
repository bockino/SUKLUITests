import time
import unittest

from src.common import globals as G
from src.forms.phase_4.form33 import Form_33


class Form_33_Tests(unittest.TestCase):

    def setUp(self):
        self.f = Form_33()
        self.f.load_page(self.f.URL)
        G.entered_values = {}

    def test_drzitel(self):
        f = self.f
        f.find_and_click_radio(f.CSS_DRZITEL_RADIO)
        f.find_and_click_button("Přidat léčivý přípravek")
        f.find_and_click_button("Přidat léčivý přípravek")
        f.find_and_click_button("Přidat šarži", index=0, repeat_cnt=2)
        f.find_and_click_button("Přidat šarži", index=1, repeat_cnt=2)
        f.find_and_click_button("Přidat šarži", index=2)
        f.find_and_click_button("Odebrat šarži", index=0)

        f.find_and_write_textbox("444", f.CSS_KOD_SUKL_GENERAL.format("0"), explicit_assert_value="0000444")
        f.find_and_click_button("Načíst přípravek", index=0)
        time.sleep(1)

        f.find_and_write_textbox("555", f.CSS_KOD_SUKL_GENERAL.format("1"), explicit_assert_value="0000555")
        f.find_and_click_button("Načíst přípravek", index=1)
        time.sleep(1)

        f.find_and_write_textbox("666", f.CSS_KOD_SUKL_GENERAL.format("2"), explicit_assert_value="0000666")
        f.find_and_click_button("Načíst přípravek", index=2)
        time.sleep(1)

        f.ra.randomize_radio_buttons()
        f.ra.randomize_checkbox_inputs()
        f.ra.randomize_datepicker_inputs()
        f.ra.randomize_text_inputs()
        f.ra.randomize_select_inputs()
        f.ra.randomize_file_inputs()

        f.submit_form("Odeslat")

    def test_provozovatel_reg(self):
        f = self.f

        f.find_and_click_radio(f.CSS_PROVOZOVATEL_RADIO)
        f.find_and_click_radio(f.CSS_REGISTROVANE)
        f.find_and_write_textbox("111", f.CSS_KOD_SUKL_GENERAL.format("0"), explicit_assert_value="0000111")
        f.find_and_click_button("Načíst přípravek")
        time.sleep(1)

        f.ra.randomize_radio_buttons()
        f.ra.randomize_checkbox_inputs()
        f.ra.randomize_datepicker_inputs()
        f.ra.randomize_text_inputs()
        f.ra.randomize_select_inputs()
        f.ra.randomize_file_inputs()

        f.submit_form("Odeslat")

    def test_provozovatel_NEreg(self):
        f = self.f

        f.find_and_click_radio(f.CSS_PROVOZOVATEL_RADIO)
        f.find_and_click_radio(f.CSS_NEREGISTROVANE)

        f.ra.randomize_radio_buttons()
        f.ra.randomize_checkbox_inputs()
        f.ra.randomize_datepicker_inputs()
        f.ra.randomize_text_inputs()
        f.ra.randomize_select_inputs()
        f.ra.randomize_file_inputs()

        f.submit_form("Odeslat")

    def test_pacient_reg(self):
        f = self.f

        f.find_and_click_radio(f.CSS_PACIENT_RADIO)

        f.ra.randomize_radio_buttons()
        f.ra.randomize_checkbox_inputs()
        f.ra.randomize_datepicker_inputs()
        f.ra.randomize_text_inputs()
        f.ra.randomize_select_inputs()
        f.ra.randomize_file_inputs()

        f.submit_form("Odeslat")

    def tearDown(self):
        self.f.dr.close()


if __name__ == '__main__':
    unittest.main()


