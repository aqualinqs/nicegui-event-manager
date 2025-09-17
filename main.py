from nicegui import ui, app
from pages.home import *
from pages.welcome import *
from pages.create_event import *
from pages.signin import *
from pages.signup import *
from pages.event import *
from pages.college import *
from pages.contact import *
from pages.not_found import *


# Expose the assets folder to the nicegui server
app.add_static_files("/assets", "assets")

# def page_layout(content_func, with_footer: bool = True):
#     """Reusable page layout with navbar, page content, and footer."""
#     def wrapper():
#         show_navbar()
#         content_func()
#         if with_footer:
#             show_footer()
#     return wrapper


# @ui.page("/signin")
# def signin_page():
#     show_signin_page()

# @ui.page("/signup")
# def signup_page():
#     show_signup_page()


# @ui.page("/notfound")
# def not_found_page():
#     show_not_found_page()


ui.run(port=8000)
