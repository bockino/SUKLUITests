import unittest

from HtmlTestRunner import HTMLTestRunner

from src import Constants as Cfg
from src.common.constants import Constants as Constants as C
from src.forms.phase_3.form27_16 import Form_27_16


class Form_27_16_Tests(unittest.TestCase):

    def setUp(self):
        self.f = Form_27_16()
        self.f.load_page(self.f.URL)
        cfg.element_values_log = {}

    def test_all_random(self):
        f = self.f

        f.ra.randomize_category_selection()
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
    unittest.main(testRunner=HTMLTestRunner(output=C.RESULT_FOLDER))
    
