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


def remember_entered_value(element, explicit_assert_value=None):
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

    element_id, _ = element.get_attribute("id").split("_____")
    if not element_id:
        sys.exit(f"nenalezen attribut 'id' elementu {element}")

    if explicit_assert_value:
        element_value = explicit_assert_value
    else:
        element_value = element.get_attribute("value")
        if not element_value:
            sys.exit(f"nenalezen attribut 'value' elementu {element}")

    G.entered_values[element] = {
        "id": element_id,
        "value": element_value,
        "is_checkable": is_checkable,
        "is_checked": is_checked
    }
    print(G.entered_values[element])
