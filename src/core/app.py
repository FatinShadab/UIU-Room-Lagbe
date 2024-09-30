from flet import Page, RouteChangeEvent, View, Text
from utils.config import APP_NAME, COLOR_SCHEMA, ROUTES
from pages import HomePage, ScanPage


class App:
    def __init__(self, page: Page):
        self.page = page
        self.page.title = APP_NAME
    
        self.__map_pages()
        self.page.on_route_change = self.__handle_route_change
        self.page.on_view_pop = self.__handle_view_pop
        
    def __map_pages(self):
        self.routes = {
            ROUTES["Home"]: HomePage(ROUTES["Home"]),
            ROUTES["Scan"]: ScanPage(ROUTES["Scan"]),
        }
    
    def __handle_route_change(self, event: RouteChangeEvent):
        self.page.views.clear()

        if event.route in self.routes:
            self.page.views.append(self.routes[event.route])
        else:
            # Handle case where the route does not exist
            self.page.views.append(View(event.route, controls=[Text("Page not found!")]))
        
        self.page.update()  # Update the page to reflect changes
    
    def __handle_view_pop(self):
        if len(self.page.views) > 1:
            self.page.views.pop()
            self.page.go(self.page.views[-1].route)
        else:
            self.page.go("/")
            
        self.page.update()
        
    def run(self):
        self.page.go(ROUTES["Home"])
        self.page.update()
