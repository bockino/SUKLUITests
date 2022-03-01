import re
import sys

from selenium.webdriver.common.action_chains import ActionChains
from src.common import globals as G


class CommonElementActions:
    def __init__(self, driver):
        self.action = ActionChains(driver)
        # self.dr = driver_inicialize()

    def precise_click(self, element):
        self.action.move_to_element(element)
        self.action.click()
        self.action.perform()
        self.action.reset_actions()


def precise_click_func(driver, element):
    ActionChains(driver).move_to_element(element).click().perform()
    # .reset_actions() ?


def input_names_to_regex():
    pass


def log_attached_file(element, file_names):
    element_name, _ = element.get_attribute("name").split("_____")
    G.attached_files_log[element_name] = file_names
    print(f"zapamatovane prilohy pro {element_name} : {G.attached_files_log[element_name]}")


def log_value_of_element(element, explicit_assert_value=None):
    """
    Vycte a ulozi "name" a "value" z objektu elementu pro pozdejsi asserty
    Pokud uz je ulozena hodnota elementu, aktualizuje se (v pripade ze po random vyplneni
    nasleduje explicitni zadani hodnoty)
    """
    is_checkable = False
    is_checked = None

    if element.get_attribute("type") in ["checkbox", "radio"]:
        is_checkable = True
        is_checked = bool(element.get_attribute("checked"))

    element_id = re.sub("_+\d+", "", element.get_attribute("id"))
    if not element_id:
        sys.exit(f"nenalezen attribut 'id' elementu {element}")

    if explicit_assert_value:
        element_value = explicit_assert_value
    else:
        element_value = element.get_attribute("value")
        if element_value is None:
            sys.exit(f"nenalezen attribut 'value' elementu {element}")

    G.element_values_log[element_id] = {
        "entered_value": element_value,
        "is_checkable": is_checkable,
        "is_checked": is_checked
    }
    print(f"zapamatovane hodnoty pro {element_id} : {G.element_values_log[element_id]}")
