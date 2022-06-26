from app.services.service import Service

class MobileHotspot:
    """Manage windows mobile hotspot"""
    def __init__(self) -> None:
        self.service = Service()
        self.service._open_action_center()
        self.service.locate_hotspot_button()

    def turn_mobile_hotspot_on(self) -> None:
        """Turn windows mobile hotspot on"""
        self.service.click_hotspot_button()

    def hotspot_is_on(self) -> bool:
        """Check windows mobile hotspot is on"""
        return self.service.hotspot_button_location is not None

    def exit(self) -> None:
        return self.service._scape_action_center()

    def run(self):
        """Start the script"""
        hotspot_is_on = self.hotspot_is_on()
        if not hotspot_is_on:
            self.turn_mobile_hotspot_on()
        self.exit()
