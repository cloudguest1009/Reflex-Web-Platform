import reflex as rx
from app.states.chat_state import ChatState


def message_bubble(message: rx.Var[dict]) -> rx.Component:
    return rx.cond(
        message["sender"] == "user",
        rx.el.div(
            rx.el.div(
                message["text"],
                class_name="px-4 py-2 text-white bg-blue-600 rounded-2xl max-w-xs md:max-w-md break-words",
            ),
            class_name="flex justify-end mb-4",
        ),
        rx.el.div(
            rx.el.div(
                rx.cond(
                    message["is_typing"],
                    rx.el.div(
                        rx.el.div(
                            class_name="w-2 h-2 bg-gray-400 rounded-full animate-pulse"
                        ),
                        rx.el.div(
                            class_name="w-2 h-2 bg-gray-400 rounded-full animate-pulse delay-75"
                        ),
                        rx.el.div(
                            class_name="w-2 h-2 bg-gray-400 rounded-full animate-pulse delay-150"
                        ),
                        class_name="flex items-center gap-1 p-2",
                    ),
                    message["text"],
                ),
                class_name="px-4 py-2 text-gray-800 bg-gray-200 rounded-2xl max-w-xs md:max-w-md break-words",
            ),
            class_name="flex justify-start mb-4",
        ),
    )


def chatbot_window() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h3("AI Assistant", class_name="text-lg font-bold text-gray-800"),
                rx.el.button(
                    rx.icon("x", class_name="h-5 w-5 text-gray-600"),
                    on_click=ChatState.toggle_chat,
                    class_name="p-1 hover:bg-gray-200 rounded-full",
                ),
                class_name="flex items-center justify-between p-4 border-b border-gray-200",
            ),
            rx.el.div(
                rx.foreach(ChatState.messages, message_bubble),
                class_name="flex-1 p-4 overflow-y-auto",
            ),
            rx.el.form(
                rx.el.input(
                    placeholder="Type your message...",
                    name="message",
                    class_name="flex-1 px-4 py-2 bg-gray-100 border border-transparent rounded-full focus:outline-none focus:ring-2 focus:ring-blue-500",
                    default_value=ChatState.current_message,
                ),
                rx.el.button(
                    rx.icon("arrow-up", class_name="h-5 w-5 text-white"),
                    type="submit",
                    class_name="p-2 bg-blue-600 rounded-full hover:bg-blue-700 transition-colors",
                ),
                on_submit=ChatState.on_submit_message,
                reset_on_submit=True,
                class_name="flex items-center gap-2 p-4 border-t border-gray-200 bg-white",
            ),
            class_name="flex flex-col h-full bg-white rounded-2xl shadow-2xl border border-gray-200",
        ),
        class_name=rx.cond(
            ChatState.chat_is_open,
            "fixed bottom-24 right-4 w-96 h-[60vh] max-h-[700px] z-50 transform translate-y-0 opacity-100 transition-all duration-300 ease-in-out",
            "fixed bottom-24 right-4 w-96 h-[60vh] max-h-[700px] z-50 transform translate-y-10 opacity-0 pointer-events-none transition-all duration-300 ease-in-out",
        ),
    )


def chatbot_widget() -> rx.Component:
    return rx.el.div(
        chatbot_window(),
        rx.el.button(
            rx.icon(
                rx.cond(ChatState.chat_is_open, "x", "message-circle-more"),
                class_name="h-8 w-8 text-white",
            ),
            on_click=ChatState.toggle_chat,
            class_name="fixed bottom-4 right-4 p-4 bg-blue-600 rounded-full shadow-lg hover:bg-blue-700 hover:scale-110 transition-all duration-200 z-50",
        ),
    )