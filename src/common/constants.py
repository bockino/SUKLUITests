"""
TODO LIST
- co z kazde subclass volat funkci baseclass a pouze predat argumenty specificke pro kazdy subform?
- paralelni beh testu!!!
- vypsat pole nepovinnych poli, aby randomizeru mohl nevyplnit pole, presto si zalogovat hodnotu elementu
"""


class Constants:
    RUN_HEADLESS = False
    INSTANCE_UNDER_TEST = "dev"
    # INSTANCE_UNDER_TEST = "test"

    TIME_TINY = 0.1
    TIME_SHORT = 2
    TIME_MIDDLE = 5
    TIME_LONG = 10

    DATA_TYPES_EXAMPLES = {
        "string": "f'~@#$%^&*_",
        "number": "123",
        "year": "1995",
        "phone": "+420 123456789",
        "mail": "tomas.bocek@qcm.cz",
        "date": "01.01.2025",
        "iban": "BR15 0000 0000 0000 1093 2840 814 P2"
    }

    # FILE_PATH = r"source_code\resources\testovaci_soubor_1.csv"
    SOURCE_FOLDER = r"C:\Users\bocek\GIT_repositories\SUKLUITests\src"
    RESOURCES_PATH = f"{SOURCE_FOLDER}\\resources"
    TEST_FILE_NAMES = [
        "test_file_1.csv",
        "test_file_2.csv",
        "test_file_3.csv",
        "test_file_4.csv",
        "test_file_5.csv",
        "test_file_6.csv",
        "test_file_7.csv",
        "test_file_8.csv",
        "test_file_9.csv",
        "test_file_10.csv"
    ]

    RESULT_FOLDER = f"{SOURCE_FOLDER}\\output"
    DOWNLOADS_FOLDER_PATH = f"{SOURCE_FOLDER}\\resources\\downloads"

    def __init__(self):
        if self.INSTANCE_UNDER_TEST == 'dev':
            self.instance_url = "https://e2.dev.eforms.sukl.cz/"
        else:
            self.instance_url = "ttps://tformulare.sukl.cz/"

        self.SAVED_FORM_URL_BASE = self.instance_url + "submission/"
        self.FORM_02 = self.instance_url + "form/zadost-o-stanoveni-maximalni-ceny"
        self.FORM_09 = self.instance_url + "form/zadost-o-kvalifikaci-do-uhradove-souteze"
        self.FORM_10 = self.instance_url + "form/zadost-o-provedeni-zkracene-revize-systemu-uhrad"
        self.FORM_11 = self.instance_url + "form/zadost-o-prepis-maximalni-ceny-vyrobce-vyse-a-podminek-uhrady"
        self.FORM_12 = self.instance_url + "form/hlaseni-ceny-puvodce"
        self.FORM_13 = self.instance_url + "form/oznameni-o-zahajeni-preruseni-ukonceni-zasilkoveho-vydeje"
        self.FORM_14 = self.instance_url + "form/hlaseni-o-zahajeni-preruseni-obnoveni-a-ukonceni-uvadeni-leciveho-pripravku-na-trh"
        self.FORM_17 = self.instance_url + "form/oznameni-o-pouziti-nlp"
        self.FORM_26 = self.instance_url + "form/zadost-o-poskytnuti-informace"
        self.FORM_01 = self.instance_url + "form/zadost-o-stanoveni-vyse-a-podminek-uhrady"
        self.FORM_03 = self.instance_url + "form/zadost-o-stanoveni-maximalni-ceny-vyrobce-a-vyse-podminek-uhrady"
        self.FORM_04 = self.instance_url + "form/zadost-o-zmenu-vyse-a-podminek-uhrady"
        self.FORM_05 = self.instance_url + "form/zadost-o-zmenu-maximalni-ceny-vyrobce"
        self.FORM_06 = self.instance_url + "form/zadost-o-zmenu-maximalni-ceny-vyrobce-a-vyse-uhrady"
        self.FORM_08 = self.instance_url + "form/zadost-o-zruseni-maximalni-ceny"
        self.FORM_16 = self.instance_url + "form/hlaseni-nps-ukonceni?prev=kUQFOXzCNNtMJLt3nRNrgWbJjFOyUBmp"
        self.FORM_19 = self.instance_url + "form/hlaseni-nps-uvodni"
        self.FORM_20 = self.instance_url + "form/zadost-o-souhlas-s-dovozem-leciveho-pripravku-ze-treti-zeme"
        self.FORM_21 = self.instance_url + "form/specificky-lecebny-program"
        self.FORM_24 = self.instance_url + "form/zadost-o-vypracovani-odborneho-stanoviska"
        self.FORM_27_01 = self.instance_url + "form/platby-nahrady-vydaju-zdravotnicke-prostredky"
        self.FORM_27_02 = self.instance_url + "form/platby-nahrady-vydaju-registrace"
        self.FORM_27_03 = self.instance_url + "form/platby-nahrady-vydaju-inspekce-distribuce"
        self.FORM_27_04 = self.instance_url + "form/platby-nahrady-vydaju-lidske-tkane-a-bunky"
        self.FORM_27_05 = self.instance_url + "form/platby-nahrady-vydaju-lekarny-prodejci"
        self.FORM_27_06 = self.instance_url + "form/platby-nahrady-vydaju-obecne-vcetne-reklamy"
        self.FORM_27_07 = self.instance_url + "form/platby-nahrady-vydaju-klinicke-hodnoceni"
        self.FORM_27_08 = self.instance_url + "form/platby-nahrady-vydaju-rocni-udrzovaci-platba"
        self.FORM_27_09 = self.instance_url + "form/platby-spravni-poplatky-registrace"
        self.FORM_27_10 = self.instance_url + "form/platby-spravni-poplatky-vyroba-ltb"
        self.FORM_27_11 = self.instance_url + "form/platby-spravni-poplatky-distribuce"
        self.FORM_27_12 = self.instance_url + "form/platby-spravni-poplatky-ceny-a-uhrady"
        self.FORM_27_13 = self.instance_url + "form/platby-spravni-poplatky-lecebne-konopi"
        self.FORM_27_14 = self.instance_url + "form/platby-spravni-poplatky-vydani-stejnopisu-opisu-kopie"
        self.FORM_27_15 = self.instance_url + "form/platby-spravni-poplatky-zadost-o-poseckani-s-platbou"
        self.FORM_27_16 = self.instance_url + "form/platby-pokuty"
        self.FORM_32 = self.instance_url + "form/hlaseni-podezreni-na-vyskyt-padelku-lp"
        self.FORM_33 = self.instance_url + "form/hlaseni-podezreni-na-zavadu-lp"
        self.FORM_34 = self.instance_url + "form/zadost-o-umozneni-uvedeni-cizojazycne-sarze-leciveho-pripravku-do-obehu"

