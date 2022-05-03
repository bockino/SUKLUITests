import unittest

from HtmlTestRunner import HTMLTestRunner
from selenium.webdriver.common.by import By

from src import Constantsfg
from src.forms.phase_3.form27_13 import Form_27_13
from src.common.constants import Constantsonstants


class Form_27_13_Tests(unittest.TestCase):

    def setUp(self):
        self.f = Form_27_13()
        self.f.load_page(self.f.URL)
        cfg.element_values_log = {}

    def test_all_random(self):
        f = self.f

        # IBAN nema atribut name - nelze zkontrolovat, proto remember_value=False
        f.write_to_textbox("BR15 0000 0000 0000 1093 2840", f.XPATH_IBAN_TEXT, By.XPATH, remember_value=False)

        f.ra.randomize_radio_inputs()
        f.ra.randomize_checkbox_inputs()
        f.ra.randomize_datepicker_inputs()
        f.ra.randomize_text_inputs()
        f.ra.randomize_select_inputs()
        f.ra.randomize_file_inputs()
        f.submit_form("Odeslat formulář")

    def tearDown(self):
        self.f.dr.close()


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output=ConstantsRESULT_FOLDER))
    
