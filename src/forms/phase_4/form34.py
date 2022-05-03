from time import sleep

from selenium.webdriver.common.by import By

from src.common.form import Form
from src.common.functions import log_value_of_element
from src.common.urls import URLs


class Form_34(Form):
    CSS_UDAJE_PRAVDIVE = "[id^='/udajeJsouPravdive']"
    CSS_JE_DRZITEL = "[id^='/zadatelJeDrzitel-ano']"
    CSS_NENI_DRZITEL = "[id^='/zadatelJeDrzitel-ne']"
    CSS_JE_PRAVICKA = "[id^='/typZadatele-pravnicka-osoba']"
    CSS_JE_FYZICKA = "[id^='/typZadatele-fyzicka-osoba']"

    XPATH_LOAD_FORM_INPUT = "/html/body/div[1]/div/div[1]/div/form/div[3]/fieldset/div/div/div/div/div[2]/input"
    SELECTOR_LOAD_FORM_INPUT = r"#\/undefined > div > div > div > div > div.files > input[type=file]"

    # Selektory s placeholderem pro index
    CSS_DRZITEL_STAT = "[id^='/lecivePripravky/{}/informaceOPripravku/adresaDrzitele/stat']"
    CSS_JAZYK_NA_OBALU = "[id^='/lecivePripravky/{}/sarzeInformace/jazykNaObalu']"
    CSS_KOD_PRIPRAVKU = "[id^='/lecivePripravky/{}/informaceOPripravku/kodSukl']"
    CSS_NACIST_PRIPRAVEK = "[id^='/lecivePripravky/{}/informaceOPripravku/undefined']"

    # # Read only inputy
    # CSS_LP_NAZEV_DEF = "[id^='/lecivePripravky/{}/informaceOPripravku/registrovanyNazevLP']"
    # CSS_LP_DOPLNEK_NAZVU_DEF = "[id^='/lecivePripravky/{}/informaceOPripravku/doplnekNazvu']"
    # CSS_LP_REGISTRACNI_CISLO_DEF = "[id^='/lecivePripravky/{}/informaceOPripravku/registracniCislo']"
    # CSS_LP_STAV_REG_KODU_DEF = "[id^='/lecivePripravky/{}/informaceOPripravku/stavRegistracnihoKodu']"
    # CSS_LP_ZPUSOB_VYDEJE_DEF = "[id^='/lecivePripravky/{}/informaceOPripravku/zpusobVydeje']"
    # CSS_LP_REGISTR_PROCEDURA_DEF = "[id^='/lecivePripravky/{}/informaceOPripravku/registracniProcedura']"

    # Read only inputy
    CSS_READ_ONLY_INPUTS = [
        "[id^='/lecivePripravky/{}/informaceOPripravku/registrovanyNazevLP']",
        "[id^='/lecivePripravky/{}/informaceOPripravku/doplnekNazvu']",
        "[id^='/lecivePripravky/{}/informaceOPripravku/registracniCislo']",
        "[id^='/lecivePripravky/{}/informaceOPripravku/stavRegistracnihoKodu']",
        "[id^='/lecivePripravky/{}/informaceOPripravku/zpusobVydeje']",
        "[id^='/lecivePripravky/{}/informaceOPripravku/registracniProcedura']"
    ]

    def __init__(self, driver):
        self.url = URLs().form_34
        self.url_debug = self.url + "#debug"

        file_naming_rules = {
            # regex pro name attribut file inputu : prefix pro nazev souboru s placeholderem pro index
            r"\/lecivePripravky\/\d+\/informaceOPripravku\/prilohy": "rozdil_",
            r"\/lecivePripravky\/\d+\/ceskaPribalovaInformace": "cpil_",
            r"\/lecivePripravky\/\d+\/originalniPribalovaInformace": "opil_",
            r"\/lecivePripravky\/\d+\/navrhDodatecnehoTextu": "navrh_",
            r"\/lecivePripravky\/\d+\/vzorVnejsihoObalu": "vzor_",
            r"\/lecivePripravky\/\d+\/analytickeCertifikaty": "cert_",
            r"\/lecivePripravky\/\d+\/plnaMoc": "pmoc_",
            r"\/lecivePripravky\/\d+\/povereniProOsobu": "pover_",
            r"\/lecivePripravky\/\d+\/doplnujiciMaterialy": "dopl_"
        }
        super().__init__(driver, file_naming_rules)

    def load_lp(self, lp_code, lp_index=0):
        full_code_format = (7 - len(lp_code)) * "0" + lp_code
        self.write_to_textbox(lp_code, self.CSS_KOD_PRIPRAVKU.format(lp_index), explicit_assert_value=full_code_format)
        sleep(0.5)
        self.click_button_by_name("Načíst přípravek", index=lp_index)
        sleep(0.5)

    def log_readonly_inputs(self, index):
        for css_ro_input in self.CSS_READ_ONLY_INPUTS:
            ro_input = self.dr.find_element(By.CSS_SELECTOR, css_ro_input.format(index))
            log_value_of_element(ro_input)
