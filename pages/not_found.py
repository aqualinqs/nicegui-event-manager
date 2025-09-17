from nicegui import ui

@ui.page("/not_found")
def show_not_found_page():
    ui.label("This is the not found page")