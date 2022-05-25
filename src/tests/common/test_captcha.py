import unittest
from time import sleep

from selenium.webdriver.common.by import By

from src.common.browser import Browser
from src.forms.phase_4.form32 import Form_32


class Form_32_Tests(unittest.TestCase):

    def setUp(self):
        self.br = Browser()
        self.f = Form_32(self.br.dr)
        self.br.load_page(self.f.URL, self.f.form_title)

    def test_captcha_nevalidni(self):
        """
        Test změny obrázku captchy, překročení neplatných pokusů
        Vyuziva se zde Form32, ale jde o sdilenou komponentu
        """
        f = self.f
        br = self.br
        br.load_page(f.URL, self.f.form_title)

        self.assertIn("Opište text z obrázku", br.page_source)
        for _ in range(0, 150):
            br.dr.find_element(By.CSS_SELECTOR, "small").click()

        for _ in range(0, 5):
            br.dr.find_element(By.XPATH, f.XPATH_CAPTCHA_INPUT).send_keys(500 * "X")
            f.click_button_by_name("Ověřit")

        self.assertIn("Více než 5 neplatných pokusů. Čekejte:", br.page_source)
        sleep(31)
        self.assertNotIn("Více než 5 neplatných pokusů. Čekejte:", br.page_source)
        self.assertIn("Opište text z obrázku", br.page_source)

    def tearDown(self):
        self.br.close_browser()


if __name__ == '__main__':
    unittest.main()



