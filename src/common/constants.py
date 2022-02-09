
class Settings:
    # SETTINGS:
    RUN_HEADLESS = False
    # BROWSER = "chrome"
    BROWSER = "chrome"
    # BROWSER = "opera"
    DRIVER_WAIT = 0.1


class Constants:

    SECS_SHORT = 2
    SECS_MIDDLE = 5
    SECS_LONG = 10

    DATA_TYPES_EXAMPLES = {
        "string": "f'~@#$%^&*_",
        "number": "3",
        "year": "1995",
        "phone": "+420 123456789",
        "mail": "tomas.bocek@qcm.cz",
        "date": "01.01.2025",
        "iban": "BR15 0000 0000 0000 1093 2840 814 P2"
    }

    # FILE_PATH = r"source_code\resources\testovaci_soubor_1.csv"
    SOURCE_FOLDER = r"C:\Users\bocek\GIT_repositories\SUKLUITests\src"
    TEST_FILE_PATH = f"{SOURCE_FOLDER}\\resources\\test_file.csv"
    RESULT_FOLDER = f"{SOURCE_FOLDER}\\output"
    DOWNLOADS_FOLDER_PATH = f"{SOURCE_FOLDER}\\resources\\downloads"

    SAVED_FORM_URL_BASE = "https://e2.dev.eforms.sukl.cz/submission/"
    # /// DEV
    FORM_02 = "https://e2.dev.eforms.sukl.cz/form/zadost-o-stanoveni-maximalni-ceny"
    FORM_09 = "https://e2.dev.eforms.sukl.cz/form/zadost-o-kvalifikaci-do-uhradove-souteze"
    FORM_10 = "https://e2.dev.eforms.sukl.cz/form/zadost-o-provedeni-zkracene-revize-systemu-uhrad"
    FORM_11 = "https://e2.dev.eforms.sukl.cz/form/zadost-o-prepis-maximalni-ceny-vyrobce-vyse-a-podminek-uhrady"
    FORM_12 = "https://e2.dev.eforms.sukl.cz/form/hlaseni-ceny-puvodce"
    FORM_13 = "https://e2.dev.eforms.sukl.cz/form/oznameni-o-zahajeni-preruseni-ukonceni-zasilkoveho-vydeje"
    FORM_14 = "https://e2.dev.eforms.sukl.cz/form/hlaseni-o-zahajeni-preruseni-obnoveni-a-ukonceni-uvadeni-leciveho-pripravku-na-trh"
    FORM_17 = "https://e2.dev.eforms.sukl.cz/form/oznameni-o-pouziti-nlp"
    FORM_26 = "https://e2.dev.eforms.sukl.cz/form/zadost-o-poskytnuti-informace"
    FORM_01 = "https://e2.dev.eforms.sukl.cz/form/zadost-o-stanoveni-vyse-a-podminek-uhrady"
    FORM_03 = "https://e2.dev.eforms.sukl.cz/form/zadost-o-stanoveni-maximalni-ceny-vyrobce-a-vyse-podminek-uhrady"
    FORM_04 = "https://e2.dev.eforms.sukl.cz/form/zadost-o-zmenu-vyse-a-podminek-uhrady"
    FORM_05 = "https://e2.dev.eforms.sukl.cz/form/zadost-o-zmenu-maximalni-ceny-vyrobce"
    FORM_06 = "https://e2.dev.eforms.sukl.cz/form/zadost-o-zmenu-maximalni-ceny-vyrobce-a-vyse-uhrady"
    FORM_08 = "https://e2.dev.eforms.sukl.cz/form/zadost-o-zruseni-maximalni-ceny"
    FORM_16 = "https://e2.dev.eforms.sukl.cz/form/hlaseni-nps-ukonceni?prev=kUQFOXzCNNtMJLt3nRNrgWbJjFOyUBmp"
    FORM_19 = "https://e2.dev.eforms.sukl.cz/form/hlaseni-nps-uvodni"
    FORM_21 = "https://e2.dev.eforms.sukl.cz/form/specificky-lecebny-program"
    FORM_24 = "https://e2.dev.eforms.sukl.cz/form/zadost-o-vypracovani-odborneho-stanoviska"
    FORM_27_01 = "https://e2.dev.eforms.sukl.cz/form/platby-nahrady-vydaju-zdravotnicke-prostredky"
    FORM_27_02 = "https://e2.dev.eforms.sukl.cz/form/platby-nahrady-vydaju-registrace"
    FORM_27_03 = "https://e2.dev.eforms.sukl.cz/form/platby-nahrady-vydaju-inspekce-distribuce"
    FORM_27_04 = "https://e2.dev.eforms.sukl.cz/form/platby-nahrady-vydaju-lidske-tkane-a-bunky"
    FORM_27_05 = "https://e2.dev.eforms.sukl.cz/form/platby-nahrady-vydaju-lekarny-prodejci"
    FORM_27_06 = "https://e2.dev.eforms.sukl.cz/form/platby-nahrady-vydaju-obecne-vcetne-reklamy"
    FORM_27_07 = "https://e2.dev.eforms.sukl.cz/form/platby-nahrady-vydaju-klinicke-hodnoceni"
    FORM_27_08 = "https://e2.dev.eforms.sukl.cz/form/platby-nahrady-vydaju-rocni-udrzovaci-platba"
    FORM_27_09 = "https://e2.dev.eforms.sukl.cz/form/platby-spravni-poplatky-registrace"
    FORM_27_10 = "https://e2.dev.eforms.sukl.cz/form/platby-spravni-poplatky-vyroba-ltb"
    FORM_27_11 = "https://e2.dev.eforms.sukl.cz/form/platby-spravni-poplatky-distribuce"
    FORM_27_12 = "https://e2.dev.eforms.sukl.cz/form/platby-spravni-poplatky-ceny-a-uhrady"
    FORM_27_13 = "https://e2.dev.eforms.sukl.cz/form/platby-spravni-poplatky-lecebne-konopi"
    FORM_27_14 = "https://e2.dev.eforms.sukl.cz/form/platby-spravni-poplatky-vydani-stejnopisu-opisu-kopie"
    FORM_27_15 = "https://e2.dev.eforms.sukl.cz/form/platby-spravni-poplatky-zadost-o-poseckani-s-platbou"
    FORM_27_16 = "https://e2.dev.eforms.sukl.cz/form/platby-pokuty"
    FORM_32 = "https://e2.dev.eforms.sukl.cz/form/hlaseni-podezreni-na-vyskyt-padelku-lp"
    FORM_33 = "https://e2.dev.eforms.sukl.cz/form/hlaseni-podezreni-na-zavadu-lp"
    FORM_34 = "https://e2.dev.eforms.sukl.cz/form/zadost-o-umozneni-uvedeni-cizojazycne-sarze-leciveho-pripravku-do-obehu"

    # /// TEST
    # FORM_02 = "https://tformulare.sukl.cz/form/zadost-o-stanoveni-maximalni-ceny"
    # FORM_09 = "https://tformulare.sukl.cz/form/zadost-o-kvalifikaci-do-uhradove-souteze"
    # FORM_10 = "https://tformulare.sukl.cz/form/zadost-o-provedeni-zkracene-revize-systemu-uhrad"
    # FORM_11 = "https://tformulare.sukl.cz/form/zadost-o-prepis-maximalni-ceny-vyrobce-vyse-a-podminek-uhrady"
    # FORM_12 = "https://tformulare.sukl.cz/form/hlaseni-ceny-puvodce"
    # FORM_13 = "https://tformulare.sukl.cz/form/oznameni-o-zahajeni-preruseni-ukonceni-zasilkoveho-vydeje"
    # FORM_14 = "https://tformulare.sukl.cz/form/hlaseni-o-zahajeni-preruseni-obnoveni-a-ukonceni-uvadeni-leciveho-pripravku-na-trh"
    # FORM_17 = "https://tformulare.sukl.cz/form/oznameni-o-pouziti-nlp"
    # FORM_26 = "https://tformulare.sukl.cz/form/zadost-o-poskytnuti-informace"
    # FORM_01 = "https://tformulare.sukl.cz/form/zadost-o-stanoveni-vyse-a-podminek-uhrady"
    # FORM_03 = "https://tformulare.sukl.cz/form/zadost-o-stanoveni-maximalni-ceny-vyrobce-a-vyse-podminek-uhrady"
    # FORM_04 = "https://tformulare.sukl.cz/form/zadost-o-zmenu-vyse-a-podminek-uhrady"
    # FORM_05 = "https://tformulare.sukl.cz/form/zadost-o-zmenu-maximalni-ceny-vyrobce"
    # FORM_06 = "https://tformulare.sukl.cz/form/zadost-o-zmenu-maximalni-ceny-vyrobce-a-vyse-uhrady"
    # FORM_08 = "https://tformulare.sukl.cz/form/zadost-o-zruseni-maximalni-ceny"
    # FORM_16 = "https://tformulare.sukl.cz/form/hlaseni-nps-ukonceni?prev=kUQFOXzCNNtMJLt3nRNrgWbJjFOyUBmp"
    # FORM_19 = "https://tformulare.sukl.cz/form/hlaseni-nps-uvodni"
    # FORM_21 = "https://tformulare.sukl.cz/form/specificky-lecebny-program"
    # FORM_24 = "https://tformulare.sukl.cz/form/zadost-o-vypracovani-odborneho-stanoviska"
    # FORM_27_01 = "https://tformulare.sukl.cz/form/platby-nahrady-vydaju-zdravotnicke-prostredky"
    # FORM_27_02 = "https://tformulare.sukl.cz/form/platby-nahrady-vydaju-registrace"
    # FORM_27_03 = "https://tformulare.sukl.cz/form/platby-nahrady-vydaju-inspekce-distribuce"
    # FORM_27_04 = "https://tformulare.sukl.cz/form/platby-nahrady-vydaju-lidske-tkane-a-bunky"
    # FORM_27_05 = "https://tformulare.sukl.cz/form/platby-nahrady-vydaju-lekarny-prodejci"
    # FORM_27_06 = "https://tformulare.sukl.cz/form/platby-nahrady-vydaju-obecne-vcetne-reklamy"
    # FORM_27_07 = "https://tformulare.sukl.cz/form/platby-nahrady-vydaju-klinicke-hodnoceni"
    # FORM_27_08 = "https://tformulare.sukl.cz/form/platby-nahrady-vydaju-rocni-udrzovaci-platba"
    # FORM_27_09 = "https://tformulare.sukl.cz/form/platby-spravni-poplatky-registrace"
    # FORM_27_10 = "https://tformulare.sukl.cz/form/platby-spravni-poplatky-vyroba-ltb"
    # FORM_27_11 = "https://tformulare.sukl.cz/form/platby-spravni-poplatky-distribuce"
    # FORM_27_12 = "https://tformulare.sukl.cz/form/platby-spravni-poplatky-ceny-a-uhrady"
    # FORM_27_13 = "https://tformulare.sukl.cz/form/platby-spravni-poplatky-lecebne-konopi"
    # FORM_27_14 = "https://tformulare.sukl.cz/form/platby-spravni-poplatky-vydani-stejnopisu-opisu-kopie"
    # FORM_27_15 = "https://tformulare.sukl.cz/form/platby-spravni-poplatky-zadost-o-poseckani-s-platbou"
    # FORM_27_16 = "https://tformulare.sukl.cz/form/platby-pokuty"
    # FORM_32 = "https://tformulare.sukl.cz/form/hlaseni-podezreni-na-vyskyt-padelku-lp"
    # FORM_33 = "https://tformulare.sukl.cz/form/hlaseni-podezreni-na-zavadu-lp"
