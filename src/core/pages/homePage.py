from flet import View, NotchShape, FloatingActionButtonLocation

from components.navigation import AppBarBtm
from components.navigation import Header
from components.buttons import ScannerBtn

from utils.config import APP_NAME, COLOR_SCHEMA


class HomePage(View):
    def __init__(self, route, **kwargs):
        super().__init__(route=route, **kwargs)  # Make sure route is passed here
        
        self.appbar = Header(
                APP_NAME,
                bgcolor=COLOR_SCHEMA["ORANGE"],
                automatically_imply_leading=False
        )
        
        self.bottom_appbar = AppBarBtm(
                bgcolor=COLOR_SCHEMA["ORANGE"],
                shape=NotchShape.CIRCULAR,
        )
        
        self.floating_action_button = ScannerBtn(bgcolor=COLOR_SCHEMA["WHITE"], foreground_color=COLOR_SCHEMA["ORANGE"])
        self.floating_action_button_location = FloatingActionButtonLocation.CENTER_DOCKED
        
        self.controls = []
        
        self.horizontal_alignment = self.vertical_alignment = "center"
        self.spacing = 10
