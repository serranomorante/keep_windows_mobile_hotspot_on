from typing import Tuple, Union

import pyautogui

DEFAULT_PAUSE = 1
WINDOWS_11 = 3


class Service:
    """GUI control service"""
    def __init__(self) -> None:
        pyautogui.PAUSE = DEFAULT_PAUSE
        self.action_center_is_open = False
        self.hotspot_button_location = None
        self.hotspot_turned_on = False

    def _force_hotspot_button_offset(
            self, location: Tuple[int, int]
        ) -> Tuple[int, int]:
        """Windows 11 needs a y offset"""
        X = 0
        Y = 1
        Y_WITH_OFFSET = location[Y] - 50
        return [location[X], Y_WITH_OFFSET]

    def _get_hotspot_button_location(self) -> Union[Tuple[int, int], None]:
        """Get hotpost button location"""
        for i in range(3):
            i += 1
            location = pyautogui.locateCenterOnScreen(f"hotspot_screenshots/button_off_{i}.png", confidence=0.7)
            if location and i == WINDOWS_11: return self._force_hotspot_button_offset(location)
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
        pyautogui.moveTo(button_x, button_y, duration=0.5)
        pyautogui.click()
        self.hotspot_turned_on = True

    def _scape_action_center(self) -> None:
        """Escape windows action center"""
        pyautogui.press("esc")
        self.action_center_is_open = False
        self.hotspot_button_location = None
