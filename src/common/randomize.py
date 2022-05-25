import datetime as dt
import re
import warnings
from random import randint
from unittest import TestCase

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from src.common.constants import Constants
# todo importovat cely modul namisto funkci?
# todo presice click pouze jako funkce?
from src.common.functions import CommonElementActions
from src.common.functions import log_attached_file
from src.common.functions import log_value_of_element


class Randomize:
    # TODO PRIDAT KONTROLU JESTLI UZ NENI PRO INPUT ZAPAMATOVANA HODNOTA, PRO VSECHNY FUNKCE!
    def __init__(self, driver):
        self.dr = driver
        self.tc = TestCase()
        self.cea = CommonElementActions(self.dr)
        self.growing_num = 0

    def generate_value(self, data_type):
        self.growing_num += 1
        if data_type == "date":
            return (dt.date.today() + dt.timedelta(days=randint(-500, 500))).strftime("%d.%m.%Y")
        if data_type == "year":
            return str(2025 + self.growing_num)
        if data_type == "string":
            return f"~@#$%^&*_{self.growing_num}"
        if data_type == "number":
            return str(randint(0, 100))
        if data_type == "phone":
            return f"+420 {randint(100000000, 1000000000)}"
        if data_type == "mail":
            return Constants.DATA_TYPES_PATTERNS[data_type]
        if data_type == "iban":
            return Constants.DATA_TYPES_PATTERNS[data_type]

    @staticmethod
    def _is_valid_format(element):
        if not element.get_attribute("value"):
            return 0
        if re.search("is-invalid", element.get_attribute("class")):
            return 0
        return 1

    @staticmethod
    def _has_active_radio(container):
        return container.find_elements(By.CSS_SELECTOR, "[type=radio]") \
               and not container.find_elements(By.CSS_SELECTOR, "[class*=active]")

    def _find_suitable_format(self, element):
        for data_type in Constants.DATA_TYPES_PATTERNS:
            element.send_keys(Constants.DATA_TYPES_PATTERNS[data_type])
            if self._is_valid_format(element):
                element.clear()
                return data_type
            element.clear()
        self.tc.fail("nenalezen validni format pro input")

    def randomize_radio_inputs(self):
        """
        Najde vsechny kontejnery s radiobuttonama a nahodne nektery zvoli, pokud jeste zadny zvoleny neni
        Takto iteruje dokud neni v kazdem kontejneru neco checked (muzou se postupne odkryvat dalsi sekce)
        """

        while True:
            need_next_iteration = False
            containers = self.dr.find_elements(By.CSS_SELECTOR, "[class=radios-container]")
            for container in filter(self._has_active_radio, containers):
                rad_buttons = container.find_elements(By.CSS_SELECTOR, "[type=radio]")
                if len(rad_buttons) == 1:
                    warnings.warn("v kontejneru je pouze jeden radiobutton - bude preskocen (resit explicitne)")
                    continue
                rad_button = rad_buttons[randint(0, len(rad_buttons) - 1)]
                self.cea.precise_click(rad_button)
                log_value_of_element(rad_button)
                need_next_iteration = True
            if not need_next_iteration:
                break

    def randomize_checkbox_inputs(self):
        """
        Najde vsechny checkboxy a nahodne je zaskrtne
        Zde se nepocita, ze by se po zaskrtnuti checkboxu zobrazily dalsi checkboxy nebo radbuttony
        """
        checkboxes = self.dr.find_elements(By.CSS_SELECTOR, "[type=checkbox]:not([checked])")
        for checkbox in checkboxes:
            if bool(checkbox.get_attribute("checked")):
                continue
            if randint(0, 1) == 1:
                self.cea.precise_click(checkbox)
            log_value_of_element(checkbox)

    def randomize_datepicker_inputs(self):
        datepicker_containers = self.dr.find_elements(By.CSS_SELECTOR, ".react-datepicker__input-container")
        for container in datepicker_containers:
            datepicker = container.find_element(By.CSS_SELECTOR, "input[type='text']")
            datepicker.click()
            self.dr.find_element(By.CSS_SELECTOR, ".react-datepicker__navigation--next").click()
            days_buttons = self.dr.find_elements(By.CSS_SELECTOR, ".react-datepicker__day")
            days_buttons[randint(0, len(days_buttons) - 1)].click()
            log_value_of_element(datepicker)

    def randomize_text_inputs(self):
        text_inputs = self.dr.find_elements(By.CSS_SELECTOR, ".input-noprint:not([readonly]),"
                                                             ".textarea-noprint:not([readonly]")
        for text_input in text_inputs:
            if not text_input.get_attribute("value"):
                suitable_format = self._find_suitable_format(text_input)
                text_input.send_keys(self.generate_value(suitable_format))
                log_value_of_element(text_input)

    def randomize_select_inputs(self):
        select_inputs = self.dr.find_elements(By.CSS_SELECTOR, "select")
        for select_input in select_inputs:
            options = select_input.find_elements(By.CSS_SELECTOR, "option:not([disabled])")
            text_option = options[randint(0, len(options)-1)].text
            Select(select_input).select_by_visible_text(text_option)
            log_value_of_element(select_input)

    def randomize_category_selection(self):
        self.dr.find_element(By.XPATH, "//button[text()='Vybrat kategorii']").click()
        choose_buttons = self.dr.find_elements(By.XPATH, "//button[text()='Zvolit kategorii ']")
        choose_buttons[randint(0, len(choose_buttons) - 1)].click()

    def randomize_file_inputs(self):
        """
        Nalezne vsechny not hidden file inputy a do vsech vlozi minimalne 1 soubor
        Na kazde dalsi vlozeny soubor je 1/2 sance, max dokud nedojdou testovaci soubory
        Vlozene soubory se zapamatuji pro pozdejsi kontrolu
        """
        file_inputs = self.dr.find_elements(By.CSS_SELECTOR, "input[type=file]:not([hidden])")
        for file_input in file_inputs:
            i = 0
            files_insert_string = f"{Constants.RESOURCES_PATH}\\{Constants.TEST_FILE_NAMES[i]}"
            file_names = [Constants.TEST_FILE_NAMES[i]]
            while randint(0, 1) and i < len(Constants.TEST_FILE_NAMES):
                print(f"debug: index {i} z pole o velikosti {len(Constants.TEST_FILE_NAMES)}")
                i += 1
                files_insert_string += f"\n{Constants.RESOURCES_PATH}\\{Constants.TEST_FILE_NAMES[i]}"
                file_names.append(Constants.TEST_FILE_NAMES[i])
            file_input.send_keys(files_insert_string)
            log_attached_file(file_input, file_names)
