from flet import BottomAppBar, NotchShape, IconButton, Container, Row, icons, colors
from utils.config import COLOR_SCHEMA


class AppBarBtm(BottomAppBar):
    def __init__(self, bgcolor=None, automatically_imply_leading=True, **kwargs):
        super().__init__(bgcolor=bgcolor, **kwargs)
        self.automatically_imply_leading = automatically_imply_leading
        self.content=Row(
            controls=[
                IconButton(icon=icons.MENU, icon_color=colors.WHITE),
                Container(expand=True),
                IconButton(icon=icons.SEARCH, icon_color=colors.WHITE),
                IconButton(icon=icons.ACCOUNT_BOX_ROUNDED, icon_color=colors.WHITE),
            ]
        )