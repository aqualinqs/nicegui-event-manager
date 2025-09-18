from nicegui import ui

def show_footer():
    ui.add_head_html('<script src="https://kit.fontawesome.com/ccba89e5d4.js" crossorigin="anonymous"></script>')
    # Make sure you have font-awesome linked in your main NiceGUI app setup
    # If not, you can add it with ui.add_head_html('<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">')
    # Your current script tag is fine but the CSS link is often easier to work with.

    with ui.element("footer").classes("w-full bg-[#1b0849] items-center justify-center p-12 flex flex-auto"):
        with ui.column().classes("w-full items-center"):
            # Brand Name/Logo
            with ui.row().classes("text-white text-4xl font-bold mb-6"):
                ui.label("MEST").classes("font-semibold")
                ui.label("EV MANAGER").classes("text-[#7d48ff]")

            # Subscription Section
            with ui.row().classes("items-center justify-center mb-10"):
                ui.input(placeholder="Enter your mail").props("rounded outlined").classes("bg-white w-64")
                ui.button("Subscribe").props('rounded color="#7d48ff"').classes("px-6 py-4")

            # Navigation Links
            with ui.row().classes("items-center justify-center mb-10 text-white font-medium gap-x-8"):
                ui.label("Home")
                ui.label("About")
                ui.label("Services")
                ui.label("Get in touch")
                ui.label("FAQs")

            # Divider Line
            ui.html("<hr>").classes("w-full my-6 border-white border-opacity-30")

            # Bottom Section: Language, Socials, Copyright
            with ui.row().classes("w-full justify-between items-center text-white text-sm"):
                # Language Selection
                with ui.row().classes("gap-x-2"):
                    ui.button("English").props('flat').classes("rounded-full bg-[#7d48ff] text-white px-3 py-1")
                    ui.button("French").props('flat').classes("rounded-full px-3 py-1 bg-transparent border border-white border-opacity-30")
                    ui.button("Hindi").props('flat').classes("rounded-full px-3 py-1 bg-transparent border border-white border-opacity-30")

                # with ui.row().classes("gap-4 justify-center text-4xl text-purple"):
                #     ui.html('<a href="https://facebookcom" target="blank"><i class="fa-brands fa-facebook"></i></a>')
                #     ui.html('<a href="https://instagram.com" target="blank"><i class="fa-brands fa-instagram"></i></a>')
                #     ui.html('<a href="https://twitter.com" target="blank"><i class="fa-brands fa-twitter"></i></a>')


                # Social Media Icons
                with ui.row().classes("gap-4 text-xl"):
                    with ui.link('https://www.linkedin.com', target='_blank').classes("text-white").style("text-decoration: none"):
                        ui.html('<i class="fa-brands fa-linkedin-in"></i>')
                    with ui.link('https://www.instagram.com', target='_blank').classes("text-white").style("text-decoration: none"):
                        ui.html('<i class="fa-brands fa-instagram"></i>')
                    with ui.link('https://www.twitter.com', target='_blank').classes("text-white").style("text-decoration: none"):
                        ui.html('<i class="fa-brands fa-x-twitter"></i>')          
                                # Copyright
                ui.label("Non Copyrighted © 2023 Upload by rich technologies").classes("text-right")


# from nicegui import ui

# def show_footer():
#     ui.add_head_html('<script src="https://kit.fontawesome.com/ccba89e5d4.js" crossorigin="anonymous"></script>')

#     with ui.element("footer").classes("w-full bg-deeppurple items-center justify-center px-10 py-5 flex flex-auto flex-wrap"):
#         with ui.row().classes("items-center justify-center text-4xl font-bold mb-4"):
#             ui.label("MEST").classes("text-purple-500")
#             ui.label("EV MANAGER").classes("text-purple-500")

#         with ui.row().classes("items-center justify-center text-white mb-8"):
#             ui.input(placeholder="Enter your mail").props("outlined").classes("bg-white w-64")
#             ui.button("Subscribe").props("color=deep-purple-7").classes("px-20 py-4")

#         ui.html("<hr>").classes("mt-16")

#         with ui.element("div").classes("flex flex-row justify-between text-white px-4 py-8"):
#             with ui.row():
#                 ui.label("English")
#                 ui.label("French")
#                 ui.label("Twi")

#             with ui.row().classes("gap-4 justify-center text-4xl text-purple"):
#                 ui.html('<a href="https://facebookcom" target="blank"><i class="fa-brands fa-facebook"></i></a>')
#                 ui.html('<a href="https://instagram.com" target="blank"><i class="fa-brands fa-instagram"></i></a>')
#                 ui.html('<a href="https://twitter.com" target="blank"><i class="fa-brands fa-twitter"></i></a>')

