
class Constants:
    RUN_HEADLESS = False
    # INSTANCE_UNDER_TEST = "dev"
    INSTANCE_UNDER_TEST = "test"

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


