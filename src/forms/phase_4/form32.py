from src.common.form import Form
from src.common.urls import URLs


class Form_32(Form):
    CSS_JE_DRZITEL_RADIO = "[id^='/hlaseniPodava-drzitel-rozhodnuti-o-registraci']"
    CSS_JE_PROVOZOVATEL_RADIO = "[id^='/hlaseniPodava-provozovatel']"
    CSS_JE_PACIENT_RADIO = "[id^='/hlaseniPodava-pacient-nebo-jina-osoba']"

    CSS_REGISTROVANE_RADIO = "[id^='/typLeciva-registrovane']"
    CSS_NEREGISTROVANE_RADIO = "[id^='/typLeciva-neregistrovane']"

    XPATH_CAPTCHA_INPUT = "/html/body/div/div/div[1]/div/form/div[4]/fieldset/div/div/div/div[2]/input"

    CSS_DRZITEL_KONTAKT_OSOBA_EMAIL = "[id^='/hlasitelDrzitel/kontaktniOsoba/email']"

    def __init__(self, driver):
        self.url = URLs().form_32
        self.url_debug = self.url + "#debug"

        file_naming_rules = {
            # regex pro name attribut file inputu : prefix pro nazev souboru s placeholderem pro index
            r"\/leciva\/\d+\/prilohy": "lp{}_"
        }
        super().__init__(driver, file_naming_rules)

        self.url = self.urls.FORM_32
        self.url_debug = self.url + "#debug"
