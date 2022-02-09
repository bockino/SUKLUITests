import re
import time
from random import randint
import warnings

from selenium.webdriver.common.by import By
from unittest import TestCase

from selenium.webdriver.support.select import Select

from src.common.functions import CommonElementActions
from src.common.constants import Constants as C
from src.common.functions import remember_entered_value

import datetime as dt


class Randomize:

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
            return C.DATA_TYPES_EXAMPLES[data_type]
        if data_type == "iban":
            return C.DATA_TYPES_EXAMPLES[data_type]

    @staticmethod
    def _is_valid_format(element):
        if not element.get_attribute("value"):
            return 0
        if re.search("is-invalid", element.get_attribute("class")):
            return 0
        return 1

    @staticmethod
    def _rad_not_yet_selected(container):
        return container.find_elements(By.CSS_SELECTOR, "[type=radio]") \
               and not container.find_elements(By.CSS_SELECTOR, "[class*=active]")

    def _find_suitable_format(self, element):
        for data_type in C.DATA_TYPES_EXAMPLES:
            element.send_keys(C.DATA_TYPES_EXAMPLES[data_type])
            if self._is_valid_format(element):
                element.clear()
                return data_type
            element.clear()
        self.tc.fail("nenalezen validni format pro input")

    def randomize_radio_buttons(self):
        """
        TODO
        """

        iteration = 0
        while True:
            iteration += 1
            need_next_iteration = False
            containers = self.dr.find_elements(By.CSS_SELECTOR, "[class=radios-container]")
            for container in filter(self._rad_not_yet_selected, containers):
                rad_buttons = container.find_elements(By.CSS_SELECTOR, "[type=radio]")
                if len(rad_buttons) == 1:
                    warnings.warn("v kontejneru je pouze jeden radiobutton - bude preskocen (resit explicitne)")
                    continue
                rad_button = rad_buttons[randint(0, len(rad_buttons) - 1)]
                self.cea.precise_click(rad_button)
                remember_entered_value(rad_button)
                need_next_iteration = True
            if not need_next_iteration:
                break

    def randomize_checkbox_inputs(self):
        """
        Najde vsechny checkboxy a mozna je zaskrtne
        Zde se nepocita, ze by se po zaskrtnuti checkboxu zobrazily dalsi checkboxy nebo radbuttony
        """
        checkboxes = self.dr.find_elements(By.CSS_SELECTOR, "[type=checkbox]:not([checked])")
        for checkbox in checkboxes:
            if bool(checkbox.get_attribute("checked")):
                continue
            if randint(0, 1) == 1:
                self.cea.precise_click(checkbox)
            remember_entered_value(checkbox)

    def randomize_datepicker_inputs(self):
        datepicker_containers = self.dr.find_elements(By.CSS_SELECTOR, ".react-datepicker__input-container")
        for container in datepicker_containers:
            datepicker = container.find_element(By.CSS_SELECTOR, "input[type='text']")
            datepicker.click()
            self.dr.find_element(By.CSS_SELECTOR, ".react-datepicker__navigation--next").click()
            days_buttons = self.dr.find_elements(By.CSS_SELECTOR, ".react-datepicker__day")
            days_buttons[randint(0, len(days_buttons) - 1)].click()
            remember_entered_value(datepicker)

    def randomize_text_inputs(self):
        text_inputs = self.dr.find_elements(By.CSS_SELECTOR, ".input-noprint:not([readonly]),"
                                                             ".textarea-noprint:not([readonly]")
        for text_input in text_inputs:
            if not text_input.get_attribute("value"):
                suitable_format = self._find_suitable_format(text_input)
                text_input.send_keys(self.generate_value(suitable_format))
                remember_entered_value(text_input)

    def randomize_select_inputs(self):
        select_inputs = self.dr.find_elements(By.CSS_SELECTOR, "select")
        for select_input in select_inputs:
            options = select_input.find_elements(By.CSS_SELECTOR, "option:not([disabled])")
            text_option = options[randint(0, len(options)-1)].text
            Select(select_input).select_by_visible_text(text_option)
            # remember_entered_value(select_input)

    def randomize_file_inputs(self):
        file_inputs = self.dr.find_elements(By.CSS_SELECTOR, "input[type=file]:not([hidden])")
        for file_input in file_inputs:
            file_input.send_keys(C.TEST_FILE_PATH)
            # remember_entered_value(file_input, explicit_assert_value=C.TEST_FILE_PATH)

    def randomize_category_selection(self):
        self.dr.find_element(By.XPATH, "//button[text()='Vybrat kategorii']").click()
        choose_buttons = self.dr.find_elements(By.XPATH, "//button[text()='Zvolit kategorii ']")
        choose_buttons[randint(0, len(choose_buttons) - 1)].click()
