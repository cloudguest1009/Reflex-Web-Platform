import reflex as rx
import asyncio
from typing import TypedDict


class Message(TypedDict):
    sender: str
    text: str
    is_typing: bool


class ChatState(rx.State):
    chat_is_open: bool = False
    messages: list[Message] = [
        {
            "sender": "bot",
            "text": "Hello! How can I help you today?",
            "is_typing": False,
        }
    ]
    current_message: str = ""

    @rx.event
    def toggle_chat(self):
        self.chat_is_open = not self.chat_is_open

    @rx.event(background=True)
    async def send_message(self, form_data: dict):
        user_message = form_data.get("message", "").strip()
        async with self:
            if not user_message:
                return
            self.messages.append(
                {"sender": "user", "text": user_message, "is_typing": False}
            )
            self.current_message = ""
        async with self:
            self.messages.append({"sender": "bot", "text": "", "is_typing": True})
        await asyncio.sleep(1.5)
        bot_response = f"Echoing: {user_message}"
        async with self:
            self.messages.pop()
            self.messages.append(
                {"sender": "bot", "text": bot_response, "is_typing": False}
            )

    @rx.event
    def on_submit_message(self, form_data: dict):
        return ChatState.send_message(form_data)