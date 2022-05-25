from time import sleep
import unittest

from selenium.webdriver import Keys

from src.common.browser import Browser
from src.forms.phase_4.form32 import Form_32
from src.common.constants import Constants


class Form_32_Tests(unittest.TestCase):

    def setUp(self):
        self.br = Browser()
        self.f = Form_32(self.br.dr)
        self.br.load_page(self.f.url_debug, self.f.form_title)

    def test_drzitel_reg(self):
        """
        Klasické odeslání s volbou Držitel, registrovaný přípravek
        """
        f = self.f

        f.set_radio_value(f.CSS_JE_DRZITEL_RADIO)
        f.set_radio_value(f.CSS_REGISTROVANE_RADIO)
        f.click_button_by_name("Přidat léčivý přípravek")
        f.click_button_by_name("Přidat šarži", index=0)

        f.ra.randomize_radio_inputs()
        f.ra.randomize_checkbox_inputs()
        f.ra.randomize_datepicker_inputs()
        f.ra.randomize_text_inputs()
        f.ra.randomize_select_inputs()
        f.ra.randomize_file_inputs()

        sleep(ConstantsTIME_SHORT)
        f.click_button_by_name("Odeslat")

        f.check_result()

    def test_provozovatel_reg(self):
        """
        Klasické odeslání s volbou Provozovatel, registrovaný přípravek
        """
        f = self.f

        f.set_radio_value(f.CSS_JE_PROVOZOVATEL_RADIO)
        f.set_radio_value(f.CSS_REGISTROVANE_RADIO)
        f.click_button_by_name("Přidat léčivý přípravek")
        f.click_button_by_name("Přidat šarži", index=1)

        f.ra.randomize_radio_inputs()
        f.ra.randomize_checkbox_inputs()
        f.ra.randomize_datepicker_inputs()
        f.ra.randomize_text_inputs()
        f.ra.randomize_select_inputs()
        f.ra.randomize_file_inputs()

        sleep(ConstantsTIME_SHORT)
        f.click_button_by_name("Odeslat")

        f.check_result()

    def test_provozovatel_NEreg(self):
        """
        Klasické odeslání s volbou Provozovatel, neregistrovaný přípravek
        """
        f = self.f

        f.set_radio_value(f.CSS_JE_PROVOZOVATEL_RADIO)
        f.set_radio_value(f.CSS_NEREGISTROVANE_RADIO)
        f.click_button_by_name("Přidat léčivý přípravek")
        f.click_button_by_name("Přidat šarži", index=1)

        f.ra.randomize_radio_inputs()
        f.ra.randomize_checkbox_inputs()
        f.ra.randomize_datepicker_inputs()
        f.ra.randomize_text_inputs()
        f.ra.randomize_select_inputs()
        f.ra.randomize_file_inputs()

        sleep(0.5)
        f.click_button_by_name("Odeslat")
        f.check_result()

    def test_pacient_reg(self):
        """
        Klasické odeslání s volbou Pacient, registrovaný přípravek
        """
        f = self.f

        f.set_radio_value(f.CSS_JE_PACIENT_RADIO)
        f.click_button_by_name("Přidat léčivý přípravek")
        f.click_button_by_name("Přidat šarži")

        f.ra.randomize_radio_inputs()
        f.ra.randomize_checkbox_inputs()
        f.ra.randomize_datepicker_inputs()
        f.ra.randomize_text_inputs()
        f.ra.randomize_select_inputs()
        f.ra.randomize_file_inputs()

        sleep(0.5)
        f.click_button_by_name("Odeslat")
        f.check_result()

    def test_nevalidni_email(self):
        """
        Pokus o odeslani formulare se spatne vypnenym emailem, nasledne opraveno a odeslano
        """
        f = self.f
        br = self.br

        f.set_radio_value(f.CSS_JE_DRZITEL_RADIO)

        f.write_to_textbox("invalid@mailcz", f.CSS_DRZITEL_KONTAKT_OSOBA_EMAIL)
        f.ra.randomize_radio_inputs()
        f.ra.randomize_checkbox_inputs()
        f.ra.randomize_datepicker_inputs()
        f.ra.randomize_text_inputs()
        f.ra.randomize_select_inputs()
        f.ra.randomize_file_inputs()

        sleep(1)
        f.click_button_by_name("Odeslat")
        self.assertIn("Email není ve správném formátu.", br.page_source)
        f.write_to_textbox(20 * Keys.BACKSPACE, f.CSS_DRZITEL_KONTAKT_OSOBA_EMAIL, remember_value=False)
        f.write_to_textbox("valid@mail.cz", f.CSS_DRZITEL_KONTAKT_OSOBA_EMAIL)

        sleep(0.5)
        f.click_button_by_name("Odeslat")
        f.check_result()

    def test_max_opakovani_LP(self):
        """
        Test maximálního počtu Léčivých připravků
        """
        f = self.f
        br = self.br

        f.set_radio_value(f.CSS_JE_DRZITEL_RADIO)
        f.click_button_by_name("Přidat léčivý přípravek", repeat_cnt=9)
        self.assertNotIn("Přidat léčivý přípravek", br.page_source)

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
        Test maximálního počtu šarží
        """
        f = self.f
        br = self.br

        f.set_radio_value(f.CSS_JE_PROVOZOVATEL_RADIO)
        f.click_button_by_name("Přidat šarži", repeat_cnt=99)
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



