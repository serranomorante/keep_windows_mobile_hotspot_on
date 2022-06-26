from typing import Tuple, Union

import time

import pyautogui


class Service:
    """GUI control service"""
    def __init__(self) -> None:
        self.action_center_is_open = False
        self.hotspot_button_location = None
        self.hotspot_turned_on = False

    def _get_hotspot_button_location(self) -> Union[Tuple[int, int], None]:
        """Get hotpost button location"""
        for i in range(2):
            i += 1
            location = pyautogui.locateCenterOnScreen(f"hotspot_screenshots/hotspot{i}.png", confidence=0.7)
            if location: return location

    def locate_hotspot_button(self) -> Union[Tuple[int, int], None]:
        """Locate the hotspot button on the screen"""
        location = self._get_hotspot_button_location()
        self.hotspot_button_location = location
        return location

    def _open_action_center(self) -> None:
        """Opens windows action center"""
        pyautogui.hotkey("win", "a")
        self.action_center_is_open = True

    def click_hotspot_button(self) -> None:
        """Click windows hotspot button"""
        if not self.hotspot_button_location:
            raise Exception("Hotspot button cannot be found.")
        button_x, button_y = self.hotspot_button_location
        pyautogui.click(button_x, button_y)
        self.hotspot_turned_on = True

    def _scape_action_center(self) -> None:
        """Escape windows action center"""
        pyautogui.press("esc")
        time.sleep(0.25)
