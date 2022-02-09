from src.common.form import Form
from src.common.constants import Constants as C


class Form_34(Form):
    URL = C.FORM_34
    URL_DEBUG = URL + "#debug"

    CSS_UDAJE_PRAVDIVE = "[id^='/udajeJsouPravdive']"
    CSS_ZADATEL_JE_DRZITEL = "[id^='/zadatelJeDrzitel-ano']"
    XPATH_LOAD_FORM_INPUT = "/html/body/div[1]/div/div[1]/div/form/div[3]/fieldset/div/div/div/div/div[2]/input"
    SEKLECTOR_LOAD_FORM_INPUT = r"#\/undefined > div > div > div > div > div.files > input[type=file]"

    # Obecne selektory
    CSS_KOD_PRIPRAVKU_DEFAULT = "[id^='/lecivePripravky/{}/informaceOPripravku/kodSukl']"
    CSS_NACIST_PRIPRAVEK = "[id^='/lecivePripravky/{}/informaceOPripravku/undefined']"
