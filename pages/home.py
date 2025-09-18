from nicegui import ui
from components.navbar import show_navbar
from components.footer import show_footer

@ui.page("/home")
def show_home_page():
    show_navbar()

    # === Hero Section ===
    with ui.element().classes('relative w-full h-[80vh] flex items-center justify-center bg-black'):
        # Background Image
        ui.image(
            "https://craftworldevents.com/wp-content/uploads/2022/10/Corporate-Events.jpg"
        ).classes("absolute inset-0 w-full h-full object-cover opacity-70")

        # Overlay Content
        with ui.column().classes("relative z-10 items-center text-center text-white space-y-6"):
            ui.label("YOUR HUB").classes("text-5xl font-extrabold drop-shadow-lg")
            ui.label("FOR ALL COOPORATE EVENTS").classes("text-5xl font-extrabold drop-shadow-lg")

        # Search Filters (positioned at bottom of hero)
        with ui.row().classes(
            "absolute bottom-8 inset-x-0 max-w-5xl mx-auto justify-center bg-[#0f0220] text-white rounded-xl shadow-lg"
        ):
            with ui.column().classes("p-4"):
                ui.label("Looking for").classes("text-xs uppercase opacity-70")
                ui.input("UI UX Promotion").props("borderless dense").classes("bg-transparent text-white")

            with ui.column().classes("p-4"):
                ui.label("In").classes("text-xs uppercase opacity-70")
                ui.input("Jakarta Selatan").props("borderless dense").classes("bg-transparent text-white")

            with ui.column().classes("p-4"):
                ui.label("When").classes("text-xs uppercase opacity-70")
                ui.input("Any Date").props("borderless dense").classes("bg-transparent text-white")


    # # === Featured Events (placeholder) ===
    # with ui.column().classes("w-full max-w-6xl mx-auto mt-16 mb-12"):
    #     ui.label("Upcoming Events").classes("text-2xl font-bold mb-4")

    #     with ui.grid(columns=3).classes("gap-6 w-full"):
    #         for i in range(6):
    #             with ui.card().classes("p-6"):
    #                 ui.label(f"Event Title {i+1}")
    #                 ui.label("Event Description here...")

    with ui.column().classes("w-full max-w-6xl mx-auto mt-16 mb-12 px-4"):
            # Header and filters
            with ui.row().classes('items-center w-full justify-between mb-8'):
                ui.label("Upcoming Events").classes("text-4xl font-bold")
                with ui.row().classes('items-center space-x-4'):
                    ui.select(options=['Weekdays', 'Weekends'], value='Weekdays').props('outlined dense')
                    ui.select(options=['Event Type', 'Concert', 'Conference'], value='Event Type').props('outlined dense')
                    ui.select(options=['Any Category', 'Music', 'Tech'], value='Any Category').props('outlined dense')

            # Events Grid 
            with ui.grid(columns=3).classes("gap-6 w-full"):
                for e in range(6):
                    with ui.card().classes("p-6"):
                        ui.label(f"Event Title {e+1}")
                        ui.label("Event Description here...")
                
                
                # First event card
                with ui.card().classes("relative rounded-xl p-0 overflow-hidden shadow-lg"):
                    ui.image('https://www.srisowbarnikaadecorator.com/wp-content/uploads/2023/01/10-Tips-for-Professional-Corporate-Event-Planning.jpg').classes('w-full h-48 object-cover')
                    with ui.element('div').classes('absolute top-4 left-4 rounded-full bg-white bg-opacity-80 px-3 py-1 text-black font-semibold'):
                        ui.label('$10.00').classes('text-xs')
                    with ui.element('div').classes('absolute top-4 right-4 flex space-x-2'):
                        ui.button(icon='favorite_border').classes('bg-white bg-opacity-80 rounded-full text-black').props('flat dense')
                        ui.button(icon='upload').classes('bg-white bg-opacity-80 rounded-full text-black').props('flat dense')

                    with ui.column().classes("p-4"):
                        with ui.row().classes("text-sm font-semibold text-gray-500"):
                            ui.label("SEP").classes("uppercase")
                            ui.label("20")
                        ui.label("Indonesia - Korea Conference").classes("text-lg font-bold")
                        ui.label("Soehanna, Daerah Khusus Ibukota Yogyakarta, Indonesia").classes("text-sm text-gray-500")

                # Second event card (Placeholder)
                with ui.card().classes("relative rounded-xl p-0 overflow-hidden shadow-lg"):
                    ui.image('https://d1jhy9q0556ci9.cloudfront.net/wp-content/uploads/2018/11/riverwind-meet-corporate-events-main-1200x675.jpg').classes('w-full h-48 object-cover')
                    with ui.element('div').classes('absolute top-4 left-4 rounded-full bg-green-500 bg-opacity-80 px-3 py-1 text-white font-semibold'):
                        ui.label('FREE').classes('text-xs')
                    with ui.element('div').classes('absolute top-4 right-4 flex space-x-2'):
                        ui.button(icon='favorite_border').classes('bg-white bg-opacity-80 rounded-full text-black').props('flat dense')
                        ui.button(icon='upload').classes('bg-white bg-opacity-80 rounded-full text-black').props('flat dense')
                    with ui.column().classes("p-4"):
                        with ui.row().classes("text-sm font-semibold text-gray-500"):
                            ui.label("SEP").classes("uppercase")
                            ui.label("23")
                        ui.label("Dream World Wide in Jakarta").classes("text-lg font-bold")
                        ui.label("Soehanna, Daerah Khusus Ibukota Yogyakarta, Indonesia").classes("text-sm text-gray-500")

                # Third event card (Placeholder)
                with ui.card().classes("relative rounded-xl p-0 overflow-hidden shadow-lg"):
                    ui.image('https://alwaince.com/wp-content/uploads/2021/05/corporate-events.jpg').classes('w-full h-48 object-cover')
                    with ui.element('div').classes('absolute top-4 left-4 rounded-full bg-white bg-opacity-80 px-3 py-1 text-black font-semibold'):
                        ui.label('$12.00').classes('text-xs')
                    with ui.element('div').classes('absolute top-4 right-4 flex space-x-2'):
                        ui.button(icon='favorite_border').classes('bg-white bg-opacity-80 rounded-full text-black').props('flat dense')
                        ui.button(icon='upload').classes('bg-white bg-opacity-80 rounded-full text-black').props('flat dense')
                    with ui.column().classes("p-4"):
                        with ui.row().classes("text-sm font-semibold text-gray-500"):
                            ui.label("SEP").classes("uppercase")
                            ui.label("25")
                        ui.label("Pesta Kembang Api Terbesar").classes("text-lg font-bold")
                        ui.label("Soehanna, Daerah Khusus Ibukota Yogyakarta, Indonesia").classes("text-sm text-gray-500")
                    
    
    show_footer()



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

# @ui.page("/")
# def show_home_page():
#     show_navbar()
#     #Herosection
#     ui.label("Welcome to MEST EVENT MANAGER")
#     with ui.element().style("flex-wrap:no-wrap"):
#         ui.image("https://cdn.pixabay.com/photo/2016/02/10/13/35/hotel-1191718_1280.jpg").classes("w-full h-[1/4]")
#         ui.label("Cover photo")
    
#     # #Featured events section
#     # with ui.row():
#     #     ui.label("Upcoming events")
#     #     with ui.row():
#     #         ui.select[(1,2,3)]
#     #         ui.select[(1,2,3)]
#     #         ui.select[(1,2,3)]
#     # with ui.grid(columns=3).classes("w-full"):
#     #     for i in range(6):
#     #         with ui.card():
#     #             ui.label("Event title")

#     # with ui.row():
#     #     # ui.link("Signup", "/signup")
#     #     # ui.link("Signin", "/signin")
#     #     ui.button("Create Event Here", on_click=lambda: ui.navigate.to('/create_event'))
#     #     with ui.link("", "/not_found"):
#     #         ui.button("Don't Click")

    
#     show_footer()