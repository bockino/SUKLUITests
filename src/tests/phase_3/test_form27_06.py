import unittest

from HtmlTestRunner import HTMLTestRunner
from selenium.webdriver.common.by import By

from src import Constants as Cfg
from src.forms.phase_3.form27_06 import Form_27_06
from src.common.constants import Constants as Constants as C


class Form_27_06_Tests(unittest.TestCase):

    def setUp(self):
        self.f = Form_27_06()
        self.f.load_page(self.f.URL)
        cfg.element_values_log = {}

    def test_all_random(self):
        f = self.f

        # IBAN nema atribut name - nelze zkontrolovat, proto remember_value=False
        f.write_to_textbox("BR15 0000 0000 0000 1093 2840", f.XPATH_IBAN_TEXT, By.XPATH, remember_value=False)

        f.ra.randomize_category_selection()
        # f.ra.randomize_radio_buttons()
        # f.ra.randomize_checkbox_inputs()
        # f.ra.randomize_datepicker_inputs()
        # f.ra.randomize_text_inputs()
        # f.ra.randomize_select_inputs()
        # f.ra.randomize_file_inputs()
        # f.submit_form("Odeslat formulář")

    def tearDown(self):
        self.f.dr.close()


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output=C.RESULT_FOLDER))