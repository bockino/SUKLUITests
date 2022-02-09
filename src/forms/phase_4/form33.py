from src.common.form import Form
from src.common.constants import Constants as C


class Form_33(Form):
    URL = C.FORM_33

    CSS_DRZITEL_RADIO = "[id^='/hlaseniPodava-drzitel-rozhodnuti-o-registraci']"
    CSS_PROVOZOVATEL_RADIO = "[id^='/hlaseniPodava-provozovatel']"
    CSS_PACIENT_RADIO = "[id^='/hlaseniPodava-pacient-nebo-jina-osoba']"

    CSS_REGISTROVANE = "[id^='/zavadaInfo/lecivoTyp-registrovane']"
    CSS_NEREGISTROVANE = "[id^='/zavadaInfo/lecivoTyp-neregistrovane']"

    CSS_TOTOZNY_S_HLASITELEM_CHECKBOX = "[id^='/zavadaInfo/lecivo/0/drzitelNeniHlasitel']"

    CSS_KOD_SUKL_GENERAL = "[id^='/zavadaInfo/lecivo/{}/lecivyPripravek/suklKod']"




