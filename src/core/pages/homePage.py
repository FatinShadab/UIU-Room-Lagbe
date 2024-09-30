from .base import BasePage
from flet import Text, FloatingActionButtonLocation
from components.buttons import ScannerBtn
from utils.config import COLOR_SCHEMA


class HomePage(BasePage):
    def __init__(self, route, **kwargs):
        super().__init__(route=route, **kwargs)  # Make sure route is passed here
        
        self.controls = [
                Text("Home Page")
        ]
        
        self.floating_action_button = ScannerBtn(role=0, bgcolor=COLOR_SCHEMA["WHITE"], foreground_color=COLOR_SCHEMA["ORANGE"])
        self.floating_action_button_location = FloatingActionButtonLocation.CENTER_DOCKED
