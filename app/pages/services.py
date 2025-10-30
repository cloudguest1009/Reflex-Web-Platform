import reflex as rx
from app.components.layout import base_layout
from app.state import AppState


def service_detail_card(service: rx.Var[dict]) -> rx.Component:
    return rx.el.div(
        rx.image(
            src=service["image"],
            class_name="w-full h-48 object-cover rounded-t-2xl opacity-10 absolute inset-0",
        ),
        rx.el.div(
            rx.el.h3(service["title"], class_name="text-2xl font-bold text-white mb-3"),
            rx.el.p(service["description"], class_name="text-white/80"),
            rx.el.ul(
                rx.foreach(
                    service["points"],
                    lambda point: rx.el.li(
                        rx.icon("square_check", class_name="h-5 w-5 text-green-300"),
                        rx.el.span(point, class_name="text-white/90"),
                        class_name="flex items-center gap-3",
                    ),
                ),
                class_name="mt-6 space-y-3",
            ),
            class_name="relative p-8",
        ),
        class_name=service["bg_gradient"]
        + " rounded-2xl overflow-hidden shadow-xl shadow-black/20",
    )


def services() -> rx.Component:
    return base_layout(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "We provide a suite of services designed to accelerate your business's growth and efficiency in the digital age.",
                    class_name="mt-6 text-lg text-gray-600 text-center max-w-3xl mx-auto",
                ),
                class_name="py-12 text-center",
            ),
            rx.el.div(
                rx.foreach(AppState.services_details, service_detail_card),
                class_name="grid md:grid-cols-1 lg:grid-cols-3 gap-8 max-w-7xl mx-auto",
            ),
            class_name="px-4 py-12",
        )
    )