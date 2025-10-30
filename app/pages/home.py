import reflex as rx
from app.state import AppState
from app.components.layout import base_layout


def service_card(service: rx.Var[dict], index: rx.Var[int]) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h3(
                service["title"], class_name="text-2xl md:text-3xl font-bold text-white"
            ),
            rx.el.p(service["description"], class_name="mt-2 text-white/80 max-w-md"),
            rx.el.a(
                "Learn More",
                rx.icon("arrow-right", class_name="ml-2 h-4 w-4"),
                href="/services",
                class_name="mt-6 inline-flex items-center px-6 py-3 bg-white/20 text-white rounded-lg backdrop-blur-sm hover:bg-white/30 transition-colors font-semibold",
            ),
            class_name="relative z-10 p-8 md:p-12",
        ),
        rx.image(
            src=service["image"],
            class_name="absolute inset-0 w-full h-full object-cover opacity-10",
        ),
        class_name=rx.cond(
            AppState.current_service_index == index,
            "relative w-full h-full overflow-hidden transition-opacity duration-500 ease-in-out opacity-100",
            "absolute inset-0 w-full h-full overflow-hidden transition-opacity duration-500 ease-in-out opacity-0",
        ),
    )


def carousel_controls() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.foreach(
                AppState.services,
                lambda _, index: rx.el.button(
                    on_click=lambda: AppState.set_service_index(index),
                    class_name=rx.cond(
                        AppState.current_service_index == index,
                        "w-6 h-2 bg-white rounded-full transition-all duration-300",
                        "w-2 h-2 bg-white/50 rounded-full transition-all duration-300 hover:bg-white",
                    ),
                ),
            ),
            class_name="flex gap-3",
        ),
        rx.el.button(
            rx.cond(
                AppState.is_playing,
                rx.icon("pause", class_name="h-5 w-5 text-white"),
                rx.icon("play", class_name="h-5 w-5 text-white"),
            ),
            on_click=AppState.toggle_play_pause,
            class_name="p-2 bg-white/20 rounded-full hover:bg-white/30 transition-colors backdrop-blur-sm",
        ),
        class_name="absolute bottom-6 left-1/2 -translate-x-1/2 z-20 flex items-center gap-6",
    )


def home() -> rx.Component:
    return base_layout(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "At DhaAdh Solutions, we craft intelligent AI, robust engineering, and seamless automation to propel your business forward. We deliver innovative solutions that drive growth, efficiency, and competitive advantage.",
                    class_name="mt-6 text-lg text-gray-600 text-center max-w-3xl",
                ),
                rx.el.div(
                    rx.el.a(
                        "Our Services",
                        href="/services",
                        class_name="px-8 py-4 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors font-semibold shadow-lg hover:shadow-blue-500/30",
                    ),
                    rx.el.a(
                        "Contact Us",
                        href="/contact",
                        class_name="px-8 py-4 bg-gray-100 text-gray-800 rounded-lg hover:bg-gray-200 transition-colors font-semibold",
                    ),
                    class_name="mt-10 flex justify-center gap-4",
                ),
                class_name="max-w-4xl mx-auto py-16 md:py-24",
            ),
            rx.el.div(
                rx.el.div(
                    rx.foreach(AppState.services, service_card),
                    carousel_controls(),
                    class_name=AppState.current_service["bg_gradient"]
                    + " relative w-full max-w-5xl mx-auto h-96 rounded-2xl shadow-2xl shadow-black/20 transition-all duration-500 ease-in-out",
                ),
                class_name="w-full px-4",
            ),
            rx.el.div(class_name="h-24"),
            on_mount=AppState.on_load_and_scroll,
        )
    )