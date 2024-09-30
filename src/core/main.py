import flet as ft
from app import App

def main(page: ft.Page):
    
    try:
        app = App(page)
        
        try:
            app.run()
        except Exception as e:
            print("[IN App.run()] " + str(e))
            app.page.show_snackbar("An error occurred. Please try again later.")
            app.page.update()
            
    except Exception as e:
        print("[IN App.__init__()] " + str(e))
        page.show_snackbar("An error occurred. Please try again later.")
        page.update()


if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")
    