from flet import FloatingActionButton, icons
from flet_core.buttons import CircleBorder
from utils.config import ROUTES

class ScannerBtn(FloatingActionButton):
    def __init__(self, role, **kwargs):
        super().__init__(
            icon=icons.QR_CODE_SCANNER if role == 0 else icons.STOP_CIRCLE,
            **kwargs
        )
        self.shape = CircleBorder()
        self.autofocus = True
        self.on_click = self._on_press_start if role == 0 else self._on_press_end

    def _on_press_start(self, event):
        event.page.go(ROUTES["Scan"])
        
    def _on_press_end(self, event):
        event.page.go(ROUTES["Home"])