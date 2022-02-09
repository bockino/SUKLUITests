from time import sleep
import unittest

from selenium.webdriver.common.by import By

from src.common.browser import Browser
from src.forms.phase_4.form32 import Form_32
from src.common.constants import Constants as C


class Form_32_Tests(unittest.TestCase):

    def setUp(self):
        self.br = Browser()
        self.f = Form_32(self.br.dr)
        self.br.load_page(self.f.URL_DEBUG)

    def test_drzitel_reg(self):
        f = self.f
        br = self.br

        f.find_and_click_radio(f.CSS_DRZITEL_RADIO)
        f.find_and_click_radio(f.CSS_REGISTROVANE_RADIO)
        f.find_and_click_button("Přidat léčivý přípravek", repeat_cnt=3)
        f.find_and_click_button("Přidat šarži", index=0, repeat_cnt=2)
        f.find_and_click_button("Přidat šarži", index=2, repeat_cnt=1)

        f.ra.randomize_radio_buttons()
        f.ra.randomize_checkbox_inputs()
        f.ra.randomize_datepicker_inputs()
        f.ra.randomize_text_inputs()
        f.ra.randomize_select_inputs()
        f.ra.randomize_file_inputs()

        sleep(C.SECS_SHORT)
        f.find_and_click_button("Odeslat")

        br.check_result()
        self.assertIn("lp1_test_file.csv", br.page_source)
        self.assertIn("lp2_test_file.csv", br.page_source)
        self.assertIn("lp3_test_file.csv", br.page_source)
        self.assertIn("lp4_test_file.csv", br.page_source)

    def test_provozovatel_reg(self):
        f = self.f
        br = self.br

        f.find_and_click_radio(f.CSS_PROVOZOVATEL_RADIO)
        f.find_and_click_radio(f.CSS_REGISTROVANE_RADIO)
        f.find_and_click_button("Přidat léčivý přípravek", repeat_cnt=1)
        f.find_and_click_button("Přidat šarži", repeat_cnt=2)

        f.ra.randomize_radio_buttons()
        f.ra.randomize_checkbox_inputs()
        f.ra.randomize_datepicker_inputs()
        f.ra.randomize_text_inputs()
        f.ra.randomize_select_inputs()
        f.ra.randomize_file_inputs()

        sleep(C.SECS_SHORT)
        f.find_and_click_button("Odeslat")

        br.check_result()
        self.assertIn("lp1_test_file.csv", br.page_source)
        self.assertIn("lp2_test_file.csv", br.page_source)

    def test_provozovatel_NEreg(self):
        f = self.f
        br = self.br

        f.find_and_click_radio(f.CSS_PROVOZOVATEL_RADIO)
        f.find_and_click_radio(f.CSS_NEREGISTROVANE_RADIO)
        f.find_and_click_button("Přidat léčivý přípravek", repeat_cnt=2)
        f.find_and_click_button("Přidat šarži", repeat_cnt=1)

        f.ra.randomize_radio_buttons()
        f.ra.randomize_checkbox_inputs()
        f.ra.randomize_datepicker_inputs()
        f.ra.randomize_text_inputs()
        f.ra.randomize_select_inputs()
        f.ra.randomize_file_inputs()

        sleep(0.5)
        f.find_and_click_button("Odeslat")

        br.check_result()
        self.assertIn("lp1_test_file.csv", br.page_source)
        self.assertIn("lp2_test_file.csv", br.page_source)
        self.assertIn("lp3_test_file.csv", br.page_source)

    def test_pacient_reg(self):
        f = self.f
        br = self.br

        f.find_and_click_radio(f.CSS_PACIENT_RADIO)
        f.find_and_click_button("Přidat léčivý přípravek", repeat_cnt=1)
        f.find_and_click_button("Přidat šarži", index=1, repeat_cnt=2)

        f.ra.randomize_radio_buttons()
        f.ra.randomize_checkbox_inputs()
        f.ra.randomize_datepicker_inputs()
        f.ra.randomize_text_inputs()
        f.ra.randomize_select_inputs()
        f.ra.randomize_file_inputs()

        sleep(0.5)
        f.find_and_click_button("Odeslat")

        br.check_result()
        self.assertIn("lp1_test_file.csv", br.page_source)
        self.assertIn("lp2_test_file.csv", br.page_source)

    def test_nevalidni_vyplneni(self):
        pass

    def test_hodne_opakovani(self):
        pass

    def test_captcha_nevalidni(self):
        f = self.f
        br = self.br

        br.load_page(f.URL)
        sleep(2)

        self.assertIn("Opište text z obrázku", br.page_source)
        for _ in range(0, 150):
            br.dr.find_element(By.CSS_SELECTOR, "small").click()

        for _ in range(0, 5):
            br.dr.find_element(By.XPATH, f.XPATH_CAPTCHA_INPUT).send_keys(500 * "X")
            f.find_and_click_button("Ověřit")

        self.assertIn("Více než 5 neplatných pokusů. Čekejte:", br.page_source)
        sleep(31)
        self.assertNotIn("Více než 5 neplatných pokusů. Čekejte:", br.page_source)
        self.assertIn("Opište text z obrázku", br.page_source)

    def tearDown(self):
        self.br.close_browser()


if __name__ == '__main__':
    unittest.main()



