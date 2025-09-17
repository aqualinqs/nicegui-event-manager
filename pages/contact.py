from nicegui import ui
from components.navbar import show_navbar
from components.footer import show_footer

@ui.page("/contact")
def show_contact_page():
    show_navbar() 

    # === Main Content Container ===
    with ui.column().classes("w-full items-center"):

        # === Page Header ===
        with ui.element('div').classes('w-full bg-gray-100 py-8 text-center'):
            ui.label("CONTACTS").classes("text-4xl font-bold text-gray-800 mb-2")
            ui.label("Home > Contact Us").classes("text-sm text-gray-500")

        # === Contact Section: Info and Map ===
        with ui.row().classes("w-full max-w-6xl mx-auto my-12 items-start justify-center p-4"):
            # Contact Information Column
            with ui.column().classes("w-full md:w-1/2 lg:w-1/2 p-4"):
                with ui.row().classes("items-center mb-4"):
                    ui.icon("location_on").classes("text-purple-600")
                    ui.label("CONTACT US / lorem ipsum").classes("text-xl font-bold text-gray-800")
                
                ui.label("Pellentesque rutrum at sapien at sollicitudin. Nam quis orci at orci fermentum mollis maximus at justo. Duis elit felis, congue egestas tristique quis, dictum vitae massa. Suspendisse at justo enim.").classes("text-sm text-gray-600 mb-4")

                with ui.column().classes("space-y-2 text-sm text-gray-600"):
                    ui.label("APPLE STORE SOHO").classes("font-bold")
                    ui.label("103 PRINCE ST. NEW YORK, NY 10012, UNITED STATES")
                    ui.label("+1 212-226-3126")
                    ui.label("hello@imevent.com").classes("text-purple-600")

            # Google Maps Placeholder
            with ui.element('div').classes("w-full md:w-1/2 lg:w-1/2 h-96 p-4"):
                # Placeholder for the map, as embedding a live map is not direct
                with ui.element('div').classes('w-full h-full bg-gray-300 flex items-center justify-center rounded-lg'):
                    ui.label("Google Maps placeholder").classes("text-gray-500 italic")

        # === Contact Form Section ===
        with ui.element('div').classes("w-full bg-red-800 py-16 flex justify-center"):
            with ui.column().classes("w-full max-w-2xl px-4 space-y-4"):
                ui.input(placeholder="Type Your Name...").classes('w-full').props('outlined rounded bg-white')
                ui.input(placeholder="Type Your Email...").classes('w-full').props('outlined rounded bg-white')
                ui.input(placeholder="Type Your Message...").classes('w-full h-32').props('type=textarea outlined rounded bg-white')
                ui.button("SEND MESSAGE", on_click=lambda: ui.notify('Message Sent!')).classes("w-48 mx-auto font-bold rounded-full").props("color=black")

    show_footer()


# from nicegui import ui

# @ui.page("/contact")
# def show_contact_page():
#     ui.label("Enquire from us today")

# with ui.row().style("flex-wrap:no-wrap"):
#     ui.image("assets\contactpage.jpg")
#     ui.label("Cover photo")