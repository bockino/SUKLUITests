from time import sleep

from selenium.webdriver.common.by import By

from src.common.form import Form
from src.common.urls import URLs
from src.common.functions import log_value_of_element


class Form_20(Form):
    CSS_ZADATEL_IC = "[id^='/distributor/ic']"
    CSS_ZADATEL_NAZEV = "[id^='/distributor/nazev']"
    XPATH_VYBERTE_DISTRIBUTORA = "//*[option='INVE Medical, s.r.o.']/."
    CSS_PREVZIT_ADRESU = "[id^='/distributor/prevzitAdresu']"
    XPATH_NACIST_FORMULAR = "/html/body/div/div/div[1]/div/form/div[3]/fieldset/div/div/div/div/div[2]/input"

    # Selektory s placeholderem pro index
    CSS_ZDRAVOTNICKE_ZARIZENI_NAZEV = "[id^='/zdravotnickeZarizeni/{}/zarizeni/nazev']"

    # # Read only inputy
    # CSS_ZADATEL_ULICE = "[id^='/distributor/adresa/ulice']"
    # CSS_ZADATET_CISLO_POPISNE = "[id^='/distributor/adresa/cisloPopisne']"
    # CSS_ZADATEL_CISLO_ORIENTACNI = "[id^='/distributor/adresa/cisloOrientacni']"
    # CSS_ZADATEL_PSC = "[id^='/distributor/adresa/psc']"
    # CSS_ZADATEL_OBEC = "[id^='/distributor/adresa/obec']"

    CSS_READ_ONLY_INPUTS = (
        "[id^='/distributor/adresa/ulice']",
        "[id^='/distributor/adresa/cisloPopisne']",
        "[id^='/distributor/adresa/cisloOrientacni']",
        "[id^='/distributor/adresa/psc']",
        "[id^='/distributor/adresa/obec']",
    )

    def __init__(self, driver):
        self.url = URLs().form_20
        self.url_debug = self.url + "#debug"

        file_naming_rules = {
            # regex pro name attribut file inputu : prefix pro nazev souboru s placeholderem pro index
            r"\/souhrnUdaju": "smpc_",
            r"\/pribalovaInformacePil": "pil_",
            r"\/farmaceutickeUdaje": "farm_",
            r"\/jineDokumenty": "jine_"
        }
        super().__init__(driver, file_naming_rules)

    def log_readonly_inputs(self):
        for css_ro_input in self.CSS_READ_ONLY_INPUTS:
            ro_input = self.dr.find_element(By.CSS_SELECTOR, css_ro_input)
            log_value_of_element(ro_input)
