from flet import AppBar, Text, Row, Container
from components.buttons import NotificationBtn

class Header(AppBar):
    def __init__(self, title, center_title=True, bgcolor=None, automatically_imply_leading=True, **kwargs):
        super().__init__(bgcolor=bgcolor, **kwargs)
        
        # Create the title on the left
        self.title = Text(title)

        # Create the notification button on the right
        notification_button = NotificationBtn(notification_messages=[
            "You have a new message",
            "Your download is complete",
            "A new update is available"
        ])
        
        # Use a Row to align title to the left and notification button to the right
        self.actions = [
            Row(
                controls=[
                    notification_button           # Notification button on the right
                ],
                alignment="spaceBetween"         # Aligns items with space between them
            )
        ]
