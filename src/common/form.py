from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from src.common.functions import CommonElementActions
from src.common.functions import remember_entered_value
from src.common.randomize import Randomize


class Form:
    def __init__(self, driver):
        self.dr = driver
        self.ra = Randomize(self.dr)
        self._cea = CommonElementActions(self.dr)
        self._ac = ActionChains(self.dr)

    # def add_sections_max(self, button_text):
    #     while True:
    #         buttons = self.dr.find_elements(By.XPATH, f"//button[text()='{button_text}']")
    #         if not buttons:
    #             return
    #         for button in buttons:
    #             button.click()

    def find_and_click_button(self, button_text, index=0, repeat_cnt=1):
        for _ in range(0, repeat_cnt):
            buttons = self.dr.find_elements(By.XPATH, f"//button[text()='{button_text}']")
            buttons[index].click()

    def find_and_write_textbox(self, value, locator_string=By.CSS_SELECTOR, locator_type=By.CSS_SELECTOR,
                               index=0, remember_value=True, explicit_assert_value=None):
        textboxes = self.dr.find_elements(locator_type, locator_string)
        textboxes[index].send_keys(value)
        if remember_value:
            remember_entered_value(textboxes[index], explicit_assert_value=explicit_assert_value)

    def find_and_click_radio(self, locator_string, locator_type=By.CSS_SELECTOR, index=0,
                             remember_value=True):
        switches = self.dr.find_elements(locator_type, locator_string)
        self._cea.precise_click(switches[index])
        if remember_value:
            remember_entered_value(switches[index])

    def find_and_check_checkbox(self, locator_string, checked=True, locator_type=By.CSS_SELECTOR, index=0,
                                remember_value=True):
        switches = self.dr.find_elements(locator_type, locator_string)
        if checked:
            self._cea.precise_click(switches[index])
        if remember_value:
            remember_entered_value(switches[index])

    def find_and_insert_file(self, file_path, locator_string=By.CSS_SELECTOR, locator_type=By.CSS_SELECTOR,
                             index=0, remember_value=True, explicit_assert_value=None):
        file_inputs = self.dr.find_elements(locator_type, locator_string)
        file_input = file_inputs[index]
        file_input.send_keys(file_path)
        if remember_value:
            remember_entered_value(file_input, explicit_assert_value=explicit_assert_value)

    def find_and_select_list(self, text_option, locator_string, locator_type=By.CSS_SELECTOR, index=0,
                             remember_value=True):
        selects = self.dr.find_elements(locator_type, locator_string)
        select = selects[index]
        Select(select).select_by_visible_text(text_option)
        if remember_value:
            remember_entered_value(select)



