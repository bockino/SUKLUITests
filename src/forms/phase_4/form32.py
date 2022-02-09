import time

from src.common.form import Form
from src.common.constants import Constants as C


class Form_32(Form):
    URL = C.FORM_32
    URL_DEBUG = URL + "#debug"

    CSS_DRZITEL_RADIO = "[id^='/hlaseniPodava-drzitel-rozhodnuti-o-registraci']"
    CSS_PROVOZOVATEL_RADIO = "[id^='/hlaseniPodava-provozovatel']"
    CSS_PACIENT_RADIO = "[id^='/hlaseniPodava-pacient-nebo-jina-osoba']"

    CSS_REGISTROVANE_RADIO = "[id^='/typLeciva-registrovane']"
    CSS_NEREGISTROVANE_RADIO = "[id^='/typLeciva-neregistrovane']"

    XPATH_CAPTCHA_INPUT = "/html/body/div/div/div[1]/div/form/div[4]/fieldset/div/div/div/div[2]/input"
