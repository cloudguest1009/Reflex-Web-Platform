import reflex as rx
from app.components.layout import base_layout


def about() -> rx.Component:
    return base_layout(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "DhaAdh Solutions was founded on the principle that technology, when applied with expertise and vision, can solve the most complex challenges and create lasting value.",
                    class_name="mt-6 text-lg text-gray-600 text-center max-w-3xl mx-auto",
                ),
                class_name="py-12 md:py-16",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.h2(
                            "Our Mission",
                            class_name="text-3xl font-bold text-gray-800 mb-4",
                        ),
                        rx.el.p(
                            "To empower businesses with transformative AI, robust engineering, and intelligent automation, enabling them to achieve unparalleled efficiency, innovation, and growth.",
                            class_name="text-gray-600 leading-relaxed",
                        ),
                    ),
                    rx.el.div(
                        rx.el.h2(
                            "Our Vision",
                            class_name="text-3xl font-bold text-gray-800 mb-4",
                        ),
                        rx.el.p(
                            "To be the leading partner for businesses navigating the digital frontier, recognized for our innovative solutions, deep expertise, and unwavering commitment to client success.",
                            class_name="text-gray-600 leading-relaxed",
                        ),
                    ),
                    class_name="grid md:grid-cols-2 gap-12 max-w-6xl mx-auto",
                ),
                class_name="py-16",
            ),
            class_name="px-4",
        )
    )