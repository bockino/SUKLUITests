
from src.common.constants import Constants


class URLs:
    def __init__(self):
        if Constants.INSTANCE_UNDER_TEST == 'dev':
            self.instance_base_url = "https://e2.dev.eforms.sukl.cz/"
            self.api_base_url = "https://server.dev.eforms.qcm.cz/api/submissions"

        elif Constants.INSTANCE_UNDER_TEST == 'test':
            self.instance_base_url = "https://tformulare.sukl.cz/"
            self.api_base_url = "https://server.tformulare.sukl.cz/api/submissions"

        self.saved_form_url_base = self.instance_base_url + "submission/"
        self.form_02 = self.instance_base_url + "form/zadost-o-stanoveni-maximalni-ceny"
        self.form_09 = self.instance_base_url + "form/zadost-o-kvalifikaci-do-uhradove-souteze"
        self.form_10 = self.instance_base_url + "form/form/zadost-o-provedeni-zkracene-revize-systemu-uhrad"
        self.form_11 = self.instance_base_url + "form/zadost-o-prepis-maximalni-ceny-vyrobce-vyse-a-podminek-uhrady"
        self.form_12 = self.instance_base_url + "form/hlaseni-ceny-puvodce"
        self.form_13 = self.instance_base_url + "form/oznameni-o-zahajeni-preruseni-ukonceni-zasilkoveho-vydeje"
        self.form_14 = self.instance_base_url + "form/hlaseni-o-zahajeni-preruseni-obnoveni-a-ukonceni-uvadeni-leciveho-pripravku-na-trh"
        self.form_17 = self.instance_base_url + "form/oznameni-o-pouziti-nlp"
        self.form_26 = self.instance_base_url + "form/zadost-o-poskytnuti-informace"
        self.form_01 = self.instance_base_url + "form/zadost-o-stanoveni-vyse-a-podminek-uhrady"
        self.form_03 = self.instance_base_url + "form/zadost-o-stanoveni-maximalni-ceny-vyrobce-a-vyse-podminek-uhrady"
        self.form_04 = self.instance_base_url + "form/zadost-o-zmenu-vyse-a-podminek-uhrady"
        self.form_05 = self.instance_base_url + "form/zadost-o-zmenu-maximalni-ceny-vyrobce"
        self.form_06 = self.instance_base_url + "form/zadost-o-zmenu-maximalni-ceny-vyrobce-a-vyse-uhrady"
        self.form_08 = self.instance_base_url + "form/zadost-o-zruseni-maximalni-ceny"
        self.form_16 = self.instance_base_url + "form/hlaseni-nps-ukonceni?prev=kUQFOXzCNNtMJLt3nRNrgWbJjFOyUBmp"
        self.form_19 = self.instance_base_url + "form/hlaseni-nps-uvodni"
        self.form_20 = self.instance_base_url + "form/zadost-o-souhlas-s-dovozem-leciveho-pripravku-ze-treti-zeme"
        self.form_21 = self.instance_base_url + "form/specificky-lecebny-program"
        self.form_24 = self.instance_base_url + "form/zadost-o-vypracovani-odborneho-stanoviska"
        self.form_27_01 = self.instance_base_url + "form/platby-nahrady-vydaju-zdravotnicke-prostredky"
        self.form_27_02 = self.instance_base_url + "form/platby-nahrady-vydaju-registrace"
        self.form_27_03 = self.instance_base_url + "form/platby-nahrady-vydaju-inspekce-distribuce"
        self.form_27_04 = self.instance_base_url + "form/platby-nahrady-vydaju-lidske-tkane-a-bunky"
        self.form_27_05 = self.instance_base_url + "form/platby-nahrady-vydaju-lekarny-prodejci"
        self.form_27_06 = self.instance_base_url + "form/platby-nahrady-vydaju-obecne-vcetne-reklamy"
        self.form_27_07 = self.instance_base_url + "form/platby-nahrady-vydaju-klinicke-hodnoceni"
        self.form_27_08 = self.instance_base_url + "form/platby-nahrady-vydaju-rocni-udrzovaci-platba"
        self.form_27_09 = self.instance_base_url + "form/platby-spravni-poplatky-registrace"
        self.form_27_10 = self.instance_base_url + "form/form/platby-spravni-poplatky-vyroba-ltb"
        self.form_27_11 = self.instance_base_url + "form/platby-spravni-poplatky-distribuce"
        self.form_27_12 = self.instance_base_url + "form/platby-spravni-poplatky-ceny-a-uhrady"
        self.form_27_13 = self.instance_base_url + "form/platby-spravni-poplatky-lecebne-konopi"
        self.form_27_14 = self.instance_base_url + "form/platby-spravni-poplatky-vydani-stejnopisu-opisu-kopie"
        self.form_27_15 = self.instance_base_url + "form/platby-spravni-poplatky-zadost-o-poseckani-s-platbou"
        self.form_27_16 = self.instance_base_url + "form/platby-pokuty"
        self.form_32 = self.instance_base_url + "form/hlaseni-podezreni-na-vyskyt-padelku-lp"
        self.form_33 = self.instance_base_url + "form/hlaseni-podezreni-na-zavadu-lp"
        self.form_34 = self.instance_base_url + "form/zadost-o-umozneni-uvedeni-cizojazycne-sarze-leciveho-pripravku-do-obehu"
