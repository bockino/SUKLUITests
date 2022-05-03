
import unittest

from HtmlTestRunner import HTMLTestRunner

from src.common.constants import Constantsonstants
from src import Constantsfg
from src.forms.phase_1.form14 import Form_14


class Form_14_Tests(unittest.TestCase):

    def setUpClass(self):
        self.f = Form_14()

    def setUp(self):
        self.f.load_page(self.f.URL)
        cfg.element_values_log = {}

    def tet_todo_test_name(self):
        f = self.f
        
        # EXAMPLE 
        f.add_section_max("TODO")
        f.add_section_max("TODO")

        f.ra.randomize_radio_inputs()
        f.ra.randomize_checkbox_inputs()
        f.ra.randomize_text_inputs()
        f.ra.randomize_select_inputs()
        f.ra.randomize_file_inputs()
        f.submit_form("Odeslat formulář")
        
    def tearDown(self):
        self.f.dr.close()

if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output=ConstantsRESULT_FOLDER))
