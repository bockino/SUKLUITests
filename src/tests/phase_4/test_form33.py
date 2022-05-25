import unittest
from time import sleep

from src.common.browser import Browser
from src.forms.phase_4.form33 import Form_33


class Form_33_Tests(unittest.TestCase):

    def setUp(self):
        self.br = Browser()
        self.f = Form_33(self.br.dr)
        self.br.load_page(self.f.url_debug, self.f.form_title)

    def test_drzitel(self):
        """
        Klasické odeslání s volbou Držitel
        """
        f = self.f

        f.set_radio_value(f.CSS_DRZITEL_RADIO)
        f.click_button_by_name("Přidat léčivý přípravek")
        f.click_button_by_name("Přidat šarži")
        f.click_button_by_name("Přidat šarži")
        f.click_button_by_name("Odebrat šarži")

        f.load_lp("444", 0)
        f.load_lp("555", 1)

        f.ra.randomize_radio_inputs()
        f.ra.randomize_checkbox_inputs()
        f.ra.randomize_datepicker_inputs()
        f.ra.randomize_text_inputs()
        f.ra.randomize_select_inputs()
        f.ra.randomize_file_inputs()

        sleep(2)
        f.click_button_by_name("Odeslat")

        f.check_result()

    def test_provozovatel_reg(self):
        f = self.f

        f.set_radio_value(f.CSS_PROVOZOVATEL_RADIO)
        f.set_radio_value(f.CSS_REGISTROVANE)
        f.load_lp("111", 0)

        f.ra.randomize_radio_inputs()
        f.ra.randomize_checkbox_inputs()
        f.ra.randomize_datepicker_inputs()
        f.ra.randomize_text_inputs()
        f.ra.randomize_select_inputs()
        f.ra.randomize_file_inputs()

        sleep(2)
        f.click_button_by_name("Odeslat")

        f.check_result()

    def test_provozovatel_NEreg(self):
        f = self.f

        f.set_radio_value(f.CSS_PROVOZOVATEL_RADIO)
        f.set_radio_value(f.CSS_NEREGISTROVANE)

        f.ra.randomize_radio_inputs()
        f.ra.randomize_checkbox_inputs()
        f.ra.randomize_datepicker_inputs()
        f.ra.randomize_text_inputs()
        f.ra.randomize_select_inputs()
        f.ra.randomize_file_inputs()

        sleep(2)
        f.click_button_by_name("Odeslat")

        f.check_result()

    def test_pacient_reg(self):
        f = self.f

        f.set_radio_value(f.CSS_PACIENT_RADIO)

        f.ra.randomize_radio_inputs()
        f.ra.randomize_checkbox_inputs()
        f.ra.randomize_datepicker_inputs()
        f.ra.randomize_text_inputs()
        f.ra.randomize_select_inputs()
        f.ra.randomize_file_inputs()

        sleep(2)
        f.click_button_by_name("Odeslat")
        f.check_result()

    # TODO ultimate test decorator
    def test_max_opakovani_LP(self):
        """
        Test maximálního počtu Léčivých přípravků
        """
        f = self.f
        br = self.br

        f.set_radio_value(f.CSS_DRZITEL_RADIO)
        f.click_button_by_name("Přidat léčivý přípravek", repeat_cnt=9)
        self.assertNotIn("Přidat léčivý přípravek", br.page_source)

        f.load_lp("111", 0)
        f.load_lp("222", 1)
        f.load_lp("333", 2)
        f.load_lp("444", 3)
        f.load_lp("555", 4)
        f.load_lp("666", 5)
        f.load_lp("777", 6)
        f.load_lp("888", 7)
        f.load_lp("999", 8)
        f.load_lp("0001234", 9)

        f.ra.randomize_radio_inputs()
        f.ra.randomize_checkbox_inputs()
        f.ra.randomize_datepicker_inputs()
        f.ra.randomize_text_inputs()
        f.ra.randomize_select_inputs()
        f.ra.randomize_file_inputs()

        sleep(0.5)
        f.click_button_by_name("Odeslat")

        f.check_result()

    def test_max_opakovani_sarzi(self):
        """
        Test maximálního počtu Šarží
        """
        f = self.f
        br = self.br

        f.set_radio_value(f.CSS_DRZITEL_RADIO)
        f.load_lp("111", 0)
        f.click_button_by_name("Přidat šarži", repeat_cnt=19)
        self.assertNotIn("Přidat šarži", br.page_source)

        f.ra.randomize_radio_inputs()
        f.ra.randomize_checkbox_inputs()
        f.ra.randomize_datepicker_inputs()
        f.ra.randomize_text_inputs()
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
