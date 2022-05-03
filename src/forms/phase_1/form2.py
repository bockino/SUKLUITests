from src.common.form import Form
from src.common.constants import Constants


class Form_2(Form):
    URL = ConstantsFORM_02

    CSS_CESTNE_PROHLASENI_CHECK = "[id^='/prilohy/cestneProhlaseni/prohlasuji']"
    CSS_S_KODEM_RADIO = "[id^='/identifikacePripravku/isKod-withcode']"
    CSS_BEZ_KODU_RADIO = "[id^='/identifikacePripravku/isKod-withoutcode']"
    CSS_PLNA_MOC_PREDKLADA_RADIO = "[id^='/prilohy/administrativni/plnaMoc-predklada']"
    CSS_PLNA_MOC_PREDLOZENA_RADIO = "[id^='/prilohy/administrativni/plnaMoc-predlozena']"
    CSS_KOD_SUKL_TXT = "[id^='/identifikacePripravku/kod/suklKod']"
