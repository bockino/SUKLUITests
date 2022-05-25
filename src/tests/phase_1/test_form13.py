import unittest
from time import sleep

from src.common.browser import Browser
from src.forms.phase_1.form13 import Form_13


class Form_13_Tests(unittest.TestCase):

    def setUp(self):
        self.br = Browser()
        self.f = Form_13(self.br.dr)
        self.br.load_page(self.f.URL_DEBUG, self.f.form_title)
        # self.br.load_page(self.f.URL)

    def test_vydej_cr(self):
        f = self.f

        f.set_checkbox_value(f.CSS_ZASILKOVY_VYDEJ_CR)
        f.set_checkbox_value(f.CSS_ZASILKOVY_VYDEJ_ZAHRANICI, set_checked=False)
        f.click_button_by_name("Přidat osobu", repeat_cnt=20)
        f.click_button_by_name("Odebrat osobu", repeat_cnt=20)

        f.ra.randomize_radio_inputs()
        f.ra.randomize_checkbox_inputs()
        f.ra.randomize_text_inputs()
        f.ra.randomize_datepicker_inputs()
        f.ra.randomize_select_inputs()
        f.ra.randomize_file_inputs()

        sleep(0.5)
        f.click_button_by_name("Odeslat")
        f.check_result()

    def test_vydej_zahranici(self):
        f = self.f

        f.set_checkbox_value(f.CSS_ZASILKOVY_VYDEJ_ZAHRANICI)
        f.set_checkbox_value(f.CSS_ZASILKOVY_VYDEJ_CR, set_checked=False)

        f.ra.randomize_radio_inputs()
        f.ra.randomize_checkbox_inputs()
        f.ra.randomize_text_inputs()
        f.ra.randomize_datepicker_inputs()
        f.ra.randomize_select_inputs()
        f.ra.randomize_file_inputs()

        sleep(0.5)
        f.click_button_by_name("Odeslat")
        f.check_result()

    def test_vydej_cr_i_zahranici(self):
        f = self.f

        f.set_checkbox_value(f.CSS_ZASILKOVY_VYDEJ_CR)
        f.set_checkbox_value(f.CSS_ZASILKOVY_VYDEJ_ZAHRANICI)

        f.ra.randomize_radio_inputs()
        f.ra.randomize_checkbox_inputs()
        f.ra.randomize_text_inputs()
        f.ra.randomize_datepicker_inputs()
        f.ra.randomize_select_inputs()
        f.ra.randomize_file_inputs()

        sleep(0.5)
        f.click_button_by_name("Odeslat")
        f.check_result()

    def test_hodne_opakovani(self):
        f = self.f

        f.set_checkbox_value(f.CSS_ZASILKOVY_VYDEJ_ZAHRANICI)
        f.click_button_by_name("Přidat osobu", repeat_cnt=20)

        f.ra.randomize_radio_inputs()
        f.ra.randomize_checkbox_inputs()
        f.ra.randomize_text_inputs()
        f.ra.randomize_datepicker_inputs()
        f.ra.randomize_select_inputs()
        f.ra.randomize_file_inputs()

        sleep(0.5)
        f.click_button_by_name("Odeslat")
        f.check_result()

    def tearDown(self):
        self.br.print_console_errors()
        self.br.close_browser()


if __name__ == '__main__':
    unittest.main()
