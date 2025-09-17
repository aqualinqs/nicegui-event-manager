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
            "https://cdn.pixabay.com/photo/2016/11/29/05/08/adult-1869620_1280.jpg"
        ).classes("absolute inset-0 w-full h-full object-cover opacity-70")

        # Overlay Content
        with ui.column().classes("relative z-10 items-center text-center text-white space-y-6"):
            ui.label("MADE FOR").classes("text-5xl font-extrabold drop-shadow-lg")
            ui.label("THOSE WHO DO").classes("text-5xl font-extrabold drop-shadow-lg")

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


    # === Featured Events (placeholder) ===
    with ui.column().classes("w-full max-w-6xl mx-auto mt-16 mb-12"):
        ui.label("Featured Events").classes("text-2xl font-bold mb-4")

        with ui.grid(columns=3).classes("gap-6 w-full"):
            for i in range(6):
                with ui.card().classes("p-6"):
                    ui.label(f"Event Title {i+1}")
                    ui.label("Event Description here...")

    with ui.column().classes("w-full max-w-6xl mx-auto mt-16 mb-12 px-4"):
            # Header and filters
            with ui.row().classes('items-center w-full justify-between mb-8'):
                ui.label("Upcoming Events").classes("text-4xl font-bold")
                with ui.row().classes('items-center space-x-4'):
                    ui.select(options=['Weekdays', 'Weekends'], value='Weekdays').props('outlined dense')
                    ui.select(options=['Event Type', 'Concert', 'Conference'], value='Event Type').props('outlined dense')
                    ui.select(options=['Any Category', 'Music', 'Tech'], value='Any Category').props('outlined dense')

            # Events Grid 
            # with ui.grid(columns=3).classes("gap-6 w-full"):
            #     # for e in range(6):
            #     #     with ui.card().classes("p-6"):
            #     #         ui.label(f"Event Title {e+1}")
            #     #         ui.label("Event Description here...")

            with ui.grid(columns=3).classes("gap-6 w-full"):  
                # First event card
                with ui.card().classes("relative rounded-xl p-0 overflow-hidden shadow-lg"):
                    ui.image('https://cdn.pixabay.com/photo/2017/02/16/19/33/dj-2072138_1280.jpg').classes('w-full h-48 object-cover')
                    with ui.element('div').classes('absolute top-4 left-4 rounded-full bg-white bg-opacity-80 px-3 py-1 text-black font-semibold'):
                        ui.label('$10.00').classes('text-xs')
                    with ui.element('div').classes('absolute top-4 right-4 flex space-x-2'):
                        ui.button(icon='favorite_border').classes('bg-white bg-opacity-80 rounded-full text-black').props('flat dense')
                        ui.button(icon='upload').classes('bg-white bg-opacity-80 rounded-full text-black').props('flat dense')

                    with ui.column().classes("p-4"):
                        with ui.row().classes("text-sm font-semibold text-gray-500"):
                            ui.label("SEP").classes("uppercase")
                            ui.label("18")
                        #with ui.element().classes("text-sm font-semibold text-gray-500"):
                            ui.button("Book Now", on_click=lambda: ui.navigate.to('/contact')).classes('text-white font-bold shadow-sm rounded-full mt-0 hover:bg-purple ml-100px').props("color=orange-6")
                        ui.label("Indonesia - Korea Conference").classes("text-lg font-bold")
                        ui.label("Soehanna, Daerah Khusus Ibukota Yogyakarta, Indonesia").classes("text-sm text-gray-500")

                # Second event card (Placeholder)
                with ui.card().classes("relative rounded-xl p-0 overflow-hidden shadow-lg"):
                    ui.image('https://cdn.pixabay.com/photo/2018/02/27/02/54/wedding-3185382_1280.jpg').classes('w-full h-48 object-cover')
                    with ui.element('div').classes('absolute top-4 left-4 rounded-full bg-green-500 bg-opacity-80 px-3 py-1 text-white font-semibold'):
                        ui.label('FREE').classes('text-xs')
                    with ui.element('div').classes('absolute top-4 right-4 flex space-x-2'):
                        ui.button(icon='favorite_border').classes('bg-white bg-opacity-80 rounded-full text-black').props('flat dense')
                        ui.button(icon='upload').classes('bg-white bg-opacity-80 rounded-full text-black').props('flat dense')
                    with ui.column().classes("p-4"):
                        with ui.row().classes("text-sm font-semibold text-gray-500"):
                            ui.label("SEP").classes("uppercase")
                            ui.label("17")
                        ui.label("Dream World Wide in Jakarta").classes("text-lg font-bold")
                        ui.label("Soehanna, Daerah Khusus Ibukota Yogyakarta, Indonesia").classes("text-sm text-gray-500")

                # Third event card (Placeholder)
                with ui.card().classes("relative rounded-xl p-0 overflow-hidden shadow-lg"):
                    ui.image('https://cdn.pixabay.com/photo/2016/11/22/19/23/fire-1850123_1280.jpg').classes('w-full h-48 object-cover')
                    with ui.element('div').classes('absolute top-4 left-4 rounded-full bg-white bg-opacity-80 px-3 py-1 text-black font-semibold'):
                        ui.label('$12.00').classes('text-xs')
                    with ui.element('div').classes('absolute top-4 right-4 flex space-x-2'):
                        ui.button(icon='favorite_border').classes('bg-white bg-opacity-80 rounded-full text-black').props('flat dense')
                        ui.button(icon='upload').classes('bg-white bg-opacity-80 rounded-full text-black').props('flat dense')
                    with ui.column().classes("p-4"):
                        with ui.row().classes("text-sm font-semibold text-gray-500"):
                            ui.label("SEP").classes("uppercase")
                            ui.label("16")
                        ui.label("Pesta Kembang Api Terbesar").classes("text-lg font-bold")
                        ui.label("Soehanna, Daerah Khusus Ibukota Yogyakarta, Indonesia").classes("text-sm text-gray-500")
                    
    
    show_footer()
