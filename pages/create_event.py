from nicegui import ui
from components.navbar import show_navbar
from components.footer import show_footer

def create_event_page():
    """This function contains all the UI elements for the event creation form."""
    with ui.row().classes('w-full h-full justify-center items-center p-8 gap-10'):
        # Left side: Event creation form
        with ui.column().classes('w-full md:w-1/2 lg:w-2/5 p-4 bg-white shadow-lg rounded-lg'):
            ui.label("Create New Event").classes('text-3xl font-bold mb-6 text-center')

            # Event Title and Venue
            ui.label("Event Title").classes('text-lg font-semibold mt-4')
            ui.input(placeholder="Enter event title").classes('w-full mb-4')

            ui.label("Event Venue").classes('text-lg font-semibold')
            ui.input(placeholder="Enter event venue").classes('w-full mb-4')

            # Start and End Time/Date
            with ui.row().classes('w-full justify-between'):
                with ui.column().classes('w-[48%]'):
                    ui.label("Start Date").classes('text-lg font-semibold')
                    ui.input(placeholder="dd/mm/yyyy").classes('w-full')
                with ui.column().classes('w-[48%]'):
                    ui.label("End Date").classes('text-lg font-semibold')
                    ui.input(placeholder="dd/mm/yyyy").classes('w-full')
            
            with ui.row().classes('w-full justify-between mt-4'):
                with ui.column().classes('w-[48%]'):
                    ui.label("Start Time").classes('text-lg font-semibold')
                    ui.input(placeholder="hh:mm").classes('w-full')
                with ui.column().classes('w-[48%]'):
                    ui.label("End Time").classes('text-lg font-semibold')
                    ui.input(placeholder="hh:mm").classes('w-full')

            # Description
            ui.label("Event Description").classes('text-lg font-semibold mt-6')
            ui.textarea(placeholder="Enter a detailed description of the event").classes('w-full h-32 mb-4')
            
            # Image Upload Area
            ui.label("Event Image").classes('text-lg font-semibold')
            with ui.card().classes('w-full h-48 flex items-center justify-center bg-gray-200 text-gray-600 mb-4'):
                ui.label("Click or drag an image here to upload").classes('text-center')
            
            # Submit Button
            ui.button("Create Event", on_click=lambda: ui.notify('Event Created!')).classes('w-full mt-6 bg-blue-600 text-white hover:bg-blue-700')

        # Right side: Image section
        with ui.column().classes('hidden md:flex md:w-1/2 lg:w-3/5 items-center justify-center'):
            # This image will occupy the right half of the screen on medium and larger devices
            ui.image("https://cdn.pixabay.com/photo/2017/08/07/23/07/concert-2608405_1280.jpg").classes('w-full h-full object-cover rounded-lg shadow-lg')
            # I've used a concert image as a placeholder. You can replace this URL with any image you prefer.

# def page_layout(content_func, with_footer: bool = True):
#     """Reusable page layout with navbar, page content, and footer."""
#     show_navbar()
#     content_func()
#     if with_footer:
#         show_footer()

# @ui.page("/create_event")
# def show_create_event_page():
    


# from nicegui import ui
# from components.navbar import show_navbar
# from components.footer import show_footer

# # def page_layout(content_func, with_footer: bool = True):
# #     """Reusable page layout with navbar, page content, and footer."""
# #     def wrapper():
# #         show_navbar()
# #         content_func()
# #         if with_footer:
# #             show_footer()
# #     return wrapper

# @ui.page("/create_event")
# def show_create_event_page():
#     ui.label("This is the event creation here")

# with ui.row().style("flex-wrap:no-wrap"):
#     ui.image("https://cdn.pixabay.com/photo/2016/02/10/13/35/hotel-1191718_1280.jpg")
#     ui.label("Cover photo")

