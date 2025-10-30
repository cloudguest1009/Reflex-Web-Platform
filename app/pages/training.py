import reflex as rx
from app.components.layout import base_layout
from app.state import AppState


def course_card(course: rx.Var[dict]) -> rx.Component:
    return rx.el.div(
        rx.el.h3(course["title"], class_name="text-xl font-bold text-gray-800"),
        rx.el.p(course["description"], class_name="mt-2 text-gray-600"),
        rx.el.div(
            rx.el.div(
                rx.icon("clock", class_name="h-4 w-4 text-gray-500"),
                rx.el.span(course["duration"], class_name="text-sm text-gray-600"),
                class_name="flex items-center gap-2",
            ),
            rx.el.div(
                rx.icon("bar-chart-2", class_name="h-4 w-4 text-gray-500"),
                rx.el.span(course["level"], class_name="text-sm text-gray-600"),
                class_name="flex items-center gap-2",
            ),
            class_name="flex items-center gap-6 mt-4 text-sm",
        ),
        rx.el.a(
            "Enroll Now",
            href="/contact",
            class_name="mt-6 inline-block px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors font-semibold w-full text-center",
        ),
        class_name="bg-white p-6 rounded-2xl border border-gray-200 shadow-sm hover:shadow-lg transition-shadow",
    )


def training() -> rx.Component:
    return base_layout(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "Our expert-led training programs are designed to equip your team with the most in-demand technology skills.",
                    class_name="mt-6 text-lg text-gray-600 text-center max-w-3xl mx-auto",
                ),
                class_name="py-12 text-center",
            ),
            rx.el.div(
                rx.foreach(AppState.training_courses, course_card),
                class_name="grid md:grid-cols-2 lg:grid-cols-3 gap-8 max-w-6xl mx-auto items-start",
            ),
            class_name="px-4 py-12",
        )
    )