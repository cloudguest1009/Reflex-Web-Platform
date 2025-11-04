import reflex as rx
from app.state import AppState
from app.states.chat_state import ChatState
from app.components.chatbot import chatbot_widget


def nav_link(text: str, href: str) -> rx.Component:
    return rx.el.a(
        text,
        href=href,
        class_name="text-gray-600 hover:text-blue-600 transition-colors font-medium",
    )


def header() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.el.a(
                rx.el.div(
                    rx.image(src="/style_minimalist_modern.png", class_name="h-8 w-8"),
                    rx.el.span(
                        "DhaAdh Solutions", class_name="font-bold text-lg text-gray-800"
                    ),
                    class_name="flex items-center gap-2",
                ),
                href="/",
            ),
            rx.el.nav(
                nav_link("Home", "/"),
                nav_link("About Us", "/about"),
                nav_link("Our Services", "/services"),
                nav_link("Training", "/training"),
                nav_link("Contact", "/contact"),
                nav_link("NewsFeed", "/newsfeed"),
                class_name="hidden md:flex items-center gap-6",
            ),
            rx.el.button(
                rx.icon("menu", class_name="h-6 w-6 text-gray-700"),
                class_name="md:hidden",
            ),
            class_name="flex items-center justify-between max-w-7xl mx-auto px-4 py-4",
        ),
        class_name="bg-white/80 backdrop-blur-md border-b border-gray-200 sticky top-0 z-50",
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.a(
                        rx.el.div(
                            rx.image(
                                src="/style_minimalist_modern.png", class_name="h-8 w-8"
                            ),
                            rx.el.span(
                                "DhaAdh Solutions",
                                class_name="font-bold text-lg text-gray-800",
                            ),
                            class_name="flex items-center gap-2",
                        ),
                        href="/",
                    ),
                    rx.el.p(
                        "© 2024 DhaAdh Solutions. All rights reserved.",
                        class_name="text-sm text-gray-500 mt-4",
                    ),
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.h3(
                            "Socials", class_name="font-semibold text-gray-700 mb-4"
                        ),
                        rx.el.div(
                            rx.el.a(
                                rx.icon("twitter", class_name="h-5 w-5"),
                                href="https://x.com/dhaadhsolutions",
                                class_name="text-gray-500 hover:text-blue-500",
                                is_external=True,
                            ),
                            rx.el.a(
                                rx.icon("linkedin", class_name="h-5 w-5"),
                                href="https://www.linkedin.com/in/dhaadh-solutions-8a7b41390",
                                class_name="text-gray-500 hover:text-blue-500",
                                is_external=True,
                            ),
                            rx.el.a(
                                rx.icon("github", class_name="h-5 w-5"),
                                href="https://github.com/dhaadhsolutions",
                                class_name="text-gray-500 hover:text-blue-500",
                                is_external=True,
                            ),
                            class_name="flex gap-4",
                        ),
                    ),
                    class_name="grid grid-cols-2 gap-8",
                ),
                class_name="grid grid-cols-1 md:grid-cols-2 gap-8",
            ),
            class_name="max-w-7xl mx-auto py-12 px-4",
        ),
        class_name="bg-gray-50 border-t border-gray-200",
    )


def base_layout(child: rx.Component, *args, **kwargs) -> rx.Component:
    return rx.el.div(
        header(),
        rx.el.main(child, class_name="flex-grow"),
        footer(),
        chatbot_widget(),
        class_name="flex flex-col min-h-screen bg-white font-['Lato']",
    )