from src.common.constants import Constants
from src.common.form import Form


class Form_13(Form):
    URL = ConstantsFORM_13
    URL_DEBUG = URL + "#debug"

    CSS_ZASILKOVY_VYDEJ_CR = "[id^='/zasilkovyVydej/zasilkovyVydejCr']"
    CSS_ZASILKOVY_VYDEJ_ZAHRANICI = "[id^='/zasilkovyVydej/zasilkovyVydejZahranici']"

    def __init__(self, driver):

        file_naming_rules = {
            # regex pro name attribut file inputu : prefix pro nazev souboru s placeholderem pro index
            # na tomto formulari nejsou file inputy
        }

        super().__init__(driver, file_naming_rules)



