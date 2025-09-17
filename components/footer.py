from nicegui import ui

def show_footer():
    ui.add_head_html('<script src="https://kit.fontawesome.com/ccba89e5d4.js" crossorigin="anonymous"></script>')

    with ui.element("footer").classes("w-full bg-deeppurple items-center justify-center px-10 py-5 flex flex-auto flex-wrap"):
        with ui.row().classes("items-center justify-center text-4xl font-bold mb-4"):
            ui.label("MEST").classes("text-purple-500")
            ui.label("EV MANAGER").classes("text-purple-500")

        with ui.row().classes("items-center justify-center text-white mb-8"):
            ui.input(placeholder="Enter your mail").props("outlined").classes("bg-white w-64")
            ui.button("Subscribe").props("color=deep-purple-7").classes("px-20 py-4")

        ui.html("<hr>").classes("mt-16")

        with ui.element("div").classes("flex flex-row justify-between text-white px-4 py-8"):
            with ui.row():
                ui.label("English")
                ui.label("French")
                ui.label("Twi")

            with ui.row().classes("gap-4 justify-center text-4xl text-purple"):
                ui.html('<a href="https://facebookcom" target="blank"><i class="fa-brands fa-facebook"></i></a>')
                ui.html('<a href="https://instagram.com" target="blank"><i class="fa-brands fa-instagram"></i></a>')
                ui.html('<a href="https://twitter.com" target="blank"><i class="fa-brands fa-twitter"></i></a>')

