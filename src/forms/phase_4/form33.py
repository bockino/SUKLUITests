from time import sleep

from src.common.form import Form
from src.common.constants import Constants as C


class Form_33(Form):
    URL = C.FORM_33
    URL_DEBUG = URL + "#debug"

    CSS_DRZITEL_RADIO = "[id^='/hlaseniPodava-drzitel-rozhodnuti-o-registraci']"
    CSS_PROVOZOVATEL_RADIO = "[id^='/hlaseniPodava-provozovatel']"
    CSS_PACIENT_RADIO = "[id^='/hlaseniPodava-pacient-nebo-jina-osoba']"

    CSS_REGISTROVANE = "[id^='/zavadaInfo/lecivoTyp-registrovane']"
    CSS_NEREGISTROVANE = "[id^='/zavadaInfo/lecivoTyp-neregistrovane']"
    CSS_KOD_SUKL_GENERAL = "[id^='/zavadaInfo/lecivo/{}/lecivyPripravek/suklKod']"

    def __init__(self, driver):

        file_naming_rules = {
            # regex pro name attribut file inputu : prefix pro nazev souboru s placeholderem pro index
            r"\/zavadaInfo\/lecivo\/\d+\/zavadaDuleziteInfo\/certifikaty\/prilohy": "lp{}_certifikaty_",
            r"\/zavadaInfo\/lecivo\/\d+\/zavadaDuleziteInfo\/rizika\/prilohy": "lp{}_rizika_",
            r"\/zavadaInfo\/lecivo\/\d+\/zavadaDuleziteInfo\/opatreni\/prilohy": "lp{}_opatreni_",
            r"\/zavadaInfo\/lecivo\/\d+\/zavadaDuleziteInfo\/informace\/prilohy": "lp{}_informace_",
            r"\/zavadaInfo\/lecivo\/\d+\/prilohy": "lp{}_"
        }
        super().__init__(driver, file_naming_rules)

    def load_lp(self, lp_code, lp_index):
        full_code_format = (7 - len(lp_code)) * "0" + lp_code
        self.write_to_textbox(lp_code, self.CSS_KOD_SUKL_GENERAL.format(lp_index), explicit_assert_value=full_code_format)
        sleep(0.5)
        self.click_button_by_name("Načíst přípravek", index=lp_index)
        sleep(0.5)
