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

@ui.page("/college")
def show_college_page():
    ui.label("This is the College page")