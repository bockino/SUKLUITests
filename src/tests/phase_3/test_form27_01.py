import time
import unittest

from HtmlTestRunner import HTMLTestRunner
from selenium.webdriver.common.by import By

from src.forms.phase_3.form27_01 import Form_27_01
from src.common.constants import Constants


class Form_27_01_Tests(unittest.TestCase):

    def setUp(self):
        self.f = Form_27_01()
        self.f.load_page(self.f.URL)

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

        f.write_to_textbox(r"c:\Users\bocek\OneDrive - QCM, s.r.o\codes\python_projects\SUKL_UI_Tests\src\resources\downloads\platby-nahrady-vydaju-zdravotnicke-prostredky_1_2_2022_13_16_57.json", "/html/body/div[1]/div/div[1]/div/form/div[3]/fieldset/div/div/div/div[2]/div[2]/input", By.XPATH, remember_value=False)
        time.sleep(500)
        #f.submit_form("Odeslat formulář")

    def tearDown(self):
        self.f.dr.close()


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner(output=ConstantsRESULT_FOLDER))