from nicegui import ui
from components.navbar import show_navbar
from components.footer import show_footer

# def page_layout(content_func, with_footer: bool = True):
#     """Reusable page layout with navbar, page content, and footer."""
#     def wrapper():
#         show_navbar()
#         content_func()
#         if with_footer:
#             show_footer()
#     return wrapper

@ui.page("/create_event")
def show_create_event_page():
    ui.label("This is the event creation here")

with ui.row().style("flex-wrap:no-wrap"):
    ui.image("https://cdn.pixabay.com/photo/2016/02/10/13/35/hotel-1191718_1280.jpg")
    ui.label("Cover photo")

