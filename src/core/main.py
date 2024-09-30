import flet as ft

from utils.config import APP_NAME, COLOR_SCHEMA

from components.navigation import AppBarBtm
from components.navigation import Header
from components.buttons import ScannerBtn


def main(page: ft.Page):
    page.horizontal_alignment = page.vertical_alignment = "center"
    page.floating_action_button = ScannerBtn(bgcolor=COLOR_SCHEMA["WHITE"], foreground_color=COLOR_SCHEMA["ORANGE"])
    page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED

    page.appbar = Header(
        APP_NAME,
        bgcolor=COLOR_SCHEMA["ORANGE"],
        automatically_imply_leading=False
    )
    
    page.bottom_appbar = AppBarBtm(
        bgcolor=COLOR_SCHEMA["ORANGE"],
        shape=ft.NotchShape.CIRCULAR,
    )

    page.update()


if __name__ == "__main__":
    ft.app(main)
    