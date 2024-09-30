from flet import FloatingActionButton, icons
from flet_core.buttons import CircleBorder

class ScannerBtn(FloatingActionButton):
    def __init__(self, **kwargs):
        super().__init__(icon=icons.QR_CODE_SCANNER, **kwargs)
        self.shape = CircleBorder()
        self.autofocus = True
        self.on_click = self._on_press

    def _on_press(self, event):
        print("Scanner button pressed")