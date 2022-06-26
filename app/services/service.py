from typing import Tuple, Union

import time

import pyautogui


class Service:
    """GUI control service"""
    def __init__(self) -> None:
        self.action_center_is_open = False
        self.hotspot_button_location = None

    def locate_hotspot_button(self) -> Union[Tuple[int, int], None]:
        """Locate the hotspot button on the screen"""
        location = pyautogui.locateCenterOnScreen("hotspot.png", confidence=0.8)
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

    def _scape_action_center(self) -> None:
        """Escape windows action center"""
        pyautogui.press("esc")
        time.sleep(0.25)
