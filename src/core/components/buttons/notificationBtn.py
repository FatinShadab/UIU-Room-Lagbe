from flet import PopupMenuButton, PopupMenuItem, Row, Icon, icons, TextButton, Text


class NotificationBtn(PopupMenuButton):
    def __init__(self, notification_messages=[], **kwargs):
        super().__init__(icon=icons.NOTIFICATIONS_ACTIVE_ROUNDED, **kwargs)
        self.notification_messages = notification_messages
        self.update_menu_items()

    def update_menu_items(self):
        # Clear existing items
        self.items = []
        
        # Add each notification as a PopupMenuItem with a close button
        for i, message in enumerate(self.notification_messages):
            self.items.append(
                PopupMenuItem(
                    content=Row(
                        controls=[
                            Icon(icons.NOTIFICATIONS, size=16),  # Notification icon
                            Text(message),                       # Notification message
                            TextButton("Close", on_click=lambda e, idx=i: self.remove_notification(idx))
                        ],
                        alignment="spaceBetween"
                    )
                )
            )

    def remove_notification(self, index):
        # Remove the notification at the specified index
        self.notification_messages.pop(index)
        
        # Update the popup menu items
        self.update_menu_items()
        
        # Trigger a page update
        self.page.update()