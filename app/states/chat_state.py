import reflex as rx
import asyncio
from typing import TypedDict
import httpx
import logging


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
        bot_response = "Sorry, something went wrong."
        try:
            webhook_url = "https://n8n.dhaadhsolutions.com/webhook/DhaAdh"
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    webhook_url, json={"message": user_message}, timeout=30
                )
                response.raise_for_status()
                response_data = response.json()
                bot_response = response_data.get(
                    "response", "Sorry, I could not process that."
                )
        except httpx.HTTPStatusError as e:
            logging.exception(f"HTTP error calling webhook: {e}")
            bot_response = (
                f"Error communicating with AI assistant: {e.response.status_code}"
            )
        except Exception as e:
            logging.exception(f"Error calling webhook: {e}")
            bot_response = "An unexpected error occurred."
        async with self:
            self.messages.pop()
            self.messages.append(
                {"sender": "bot", "text": bot_response, "is_typing": False}
            )

    @rx.event
    def on_submit_message(self, form_data: dict):
        return ChatState.send_message(form_data)