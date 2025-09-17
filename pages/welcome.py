from nicegui import ui

@ui.page("/")
def show_welcome_page():
    # Adding the fontawesome icons
    ui.add_head_html("<script src='https://kit.fontawesome.com/ccba89e5d4.js' crossorigin='anonymous'></script>")
    
    with ui.element("div").classes("relative w-full h-screen flex flex-col items-center justify-center m-0 p-0"):
        
        # Background Image and Semi-Transparent Overlay
        ui.image("https://cdn.pixabay.com/photo/2016/02/10/13/35/hotel-1191718_1280.jpg").classes("absolute inset-0 w-full h-full object-cover")
        
        # The semi-transparent overlay to increase contrast
        ui.element("div").classes("absolute inset-0 bg-black opacity-40")
        
        # Content (Labels and Buttons)
        with ui.column().classes("relative z-10 items-center text-center text-white space-y-6"):
            ui.label("WELCOME TO").classes("text-5xl font-extrabold drop-shadow-lg")
            # Corrected a typo in the class from 'font-abold' to 'font-bold'
            ui.label("MEST EV MANAGER").classes("text-5xl font-bold drop-shadow-lg")
            
            # Buttons
            ui.button("Sign up/ Sign in", on_click=lambda: ui.navigate.to('/signup')).classes('max-w-xs w-3/4 py-3 text-white font-bold rounded-full shadow-lg mt-40 hover:bg-purple-400').props("color=orange-6")
            ui.label("Ask me again later").classes("text-1xl drop-shadow-lg")
            ui.button("Proceed to Home", on_click=lambda: ui.navigate.to('/home')).classes('max-w-xs w-3/4 py-3 font-bold rounded-full shadow-sm bg-purple-400').props("color=transparent text-white outlined")


# from nicegui import ui

# @ui.page("/")
# def show_welcome_page():
#     #  Adding the fontawesome icons
#     ui.add_head_html("<script src='https://kit.fontawesome.com/ccba89e5d4.js' crossorigin='anonymous'></script>")
     
#     with ui.element().classes("relative w-full h-full flex flex-col m-0 p-0 gap-0 items-center justify-center"):
#         # The image container
#         # with ui.element("div").classes("relative w-full h-2/3 bg-cover bg-center"):
#         ui.image("https://cdn.pixabay.com/photo/2016/02/10/13/35/hotel-1191718_1280.jpg").classes("w-full h-full object-cover opacity-80")
        
#         with ui.column().classes("relative z-10 items-center text-center text-white space-y-6"):
#             ui.label("WELCEME TO").classes("text-5xl font-extrabold drop-shadow-lg")
#             ui.label("MEST EV MANAGER").classes("text-5xl font-abold drop-shadow-lg")            

#         # The content section, styled to match the image
#         # with ui.column().classes('w-full h-1/3 bg-white flex flex-col justify-center items-center p-4 text-center'):
#         #     ui.label("And that's the cherry on top!").classes('text-3xl font-bold text-black mb-2')
#         #     ui.label("No extra fees on booking and amazing customer service. We'll get you your package within 2 business days no questions asked!").classes('text-sm text-gray-500 max-w-sm mx-auto mb-4')
            
#             # # The bullet points
#             # with ui.row().classes('items-center justify-center gap-2 mb-8'):
#             #     ui.element('div').classes('w-2 h-2 rounded-full bg-black')
#             #     ui.element('div').classes('w-2 h-2 rounded-full bg-black')
#             #     ui.element('div').classes('w-2 h-2 rounded-full bg-purple-500')
            
#             # Buttons
#             ui.button("Sign up/ Sign in", on_click=lambda: ui.navigate.to('/signup')).classes('w-1/4 py-3 bg-lime-500 text-white font-bold rounded-full shadow-lg').props("color=lime-500")
#             ui.label("Ask me again later").classes("text-5xl drop-shadow-lg")
#             ui.button("Proceed to Home", on_click=lambda: ui.navigate.to('/home')).classes('w-1/4 py-3 bg-gray-300 text-black font-bold rounded-full shadow-lg')
