
import unittest

from HtmlTestRunner import HTMLTestRunner

from src.common.constants import Constants as Constants as C
from src import Constants as Cfg
from src.forms.phase_1.form10 import Form_10


class Form_10_Tests(unittest.TestCase):

    def setUpClass(self):
        self.f = Form_10()

    def setUp(self):
        self.f.load_page(self.f.URL)
        cfg.element_values_log = {}

    def tet_todo_test_name(self):
        f = self.f
        
        # EXAMPLE 
        f._cea.check_element("TODO")
        f._cea.check_element("TODO")
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
    unittest.main(testRunner=HTMLTestRunner(output=C.RESULT_FOLDER))
