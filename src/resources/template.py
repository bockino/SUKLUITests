default_form = '''
import time

from source_code.common.constants import Constants as Constants as C
from source_code.common.form import Form

class Form_{}(Form):
    URL = "TODO"

    EXAMPLE1 = "[id^='TODO']"
    EXAMPLE2 = "[id^='TODO']"
    EXAMPLE3 = "[id^='TODO']"

    def __init__(self):
        super().__init__()
'''

default_test = '''
import unittest

from HtmlTestRunner import HTMLTestRunner

from source_code.common.constants import Constants as Constants as C
from source_code import Constants as Cfg
from source_code.forms.phase_TODO.form{} import Form_{}


class Form_{}_Tests(unittest.TestCase):

    def setUpClass(self):
        self.f = Form_{}()

    def setUp(self):
        self.f.load_page(self.f.URL)
        cfg.submitted_items = TODO

    def test_todo_test_name(self):
        f = self.f
        
        # EXAMPLE 
        f.cea.click_on("TODO")
        f.cea.click_on("TODO")
        f.add_section_max("TODO")
        f.add_section_max("TODO")

        f.ra.randomize_radio_buttons()
        f.ra.randomize_checkbox_inputs()
        f.ra.randomize_text_inputs()
        f.ra.randomize_select_inputs()
        f.ra.randomize_file_inputs()
        f.submit_form("Odeslat formulář")
        
    def test_todo_test_name2(self):
        f = self.f
        # TODO
        
    def tearDown(self):
        self.f.dr.close()

if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output=C.RESULT_FOLDER))
'''


# for i in range(2, 31):
#     form_x = default_test.format(f"Form_{i}")
#     with open(f"form{i}.py", "w") as file:
#         file.write(form_x)

for i in range(1, 31):
    form_x = default_test.format(i, i, i, i)
    with open(f"test_form{i}.py", "w") as file:
        file.write(form_x)
