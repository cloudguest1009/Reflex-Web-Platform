import reflex as rx
from app.components.layout import base_layout
from app.state import AppState


def newsfeed_card(item: rx.Var[dict]) -> rx.Component:
    return rx.el.a(
        rx.el.div(
            rx.el.div(
                rx.icon(item["platform"], class_name="h-6 w-6"),
                class_name=rx.cond(
                    item["platform"] == "linkedin",
                    "text-blue-500",
                    rx.cond(
                        item["platform"] == "youtube", "text-red-500", "text-pink-500"
                    ),
                ),
            ),
            rx.el.div(
                rx.el.h3(item["title"], class_name="text-lg font-bold text-gray-800"),
                rx.el.p(item["preview"], class_name="mt-1 text-gray-600 text-sm"),
                rx.el.span(item["date"], class_name="text-xs text-gray-400 mt-2"),
                class_name="flex-1",
            ),
            rx.icon("arrow-right", class_name="h-5 w-5 text-gray-400"),
            class_name="flex items-center gap-4 p-4 bg-white rounded-2xl border border-gray-200 shadow-sm hover:shadow-lg transition-shadow",
        ),
        href=item["link"],
        is_external=True,
        width="100%",
    )


def newsfeed() -> rx.Component:
    return base_layout(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "Follow our journey and insights on various platforms.",
                    class_name="mt-6 text-lg text-gray-600 text-center max-w-3xl mx-auto",
                ),
                class_name="py-12 text-center",
            ),
            rx.el.div(
                rx.foreach(AppState.all_newsfeeds, newsfeed_card),
                class_name="grid md:grid-cols-2 gap-6 max-w-4xl mx-auto",
            ),
            class_name="px-4 py-12",
        )
    )