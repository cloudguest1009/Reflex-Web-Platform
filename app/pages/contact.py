import reflex as rx
from app.components.layout import base_layout
from app.state import AppState


def contact_form_field(
    label: str, name: str, placeholder: str, field_type: str = "text"
) -> rx.Component:
    return rx.el.div(
        rx.el.label(label, class_name="block text-sm font-medium text-gray-700 mb-1"),
        rx.el.input(
            name=name,
            placeholder=placeholder,
            type=field_type,
            required=True,
            class_name="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500 transition-shadow",
        ),
        class_name="w-full",
    )


def contact_form() -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            "Send us a Message", class_name="text-3xl font-bold text-gray-900 mb-6"
        ),
        rx.cond(
            AppState.contact_submitted,
            rx.el.div(
                rx.el.p(
                    AppState.contact_submission_message,
                    class_name="text-green-600 font-semibold",
                ),
                class_name="p-4 mb-4 bg-green-100 border border-green-200 rounded-lg text-center",
            ),
            rx.el.form(
                rx.el.div(
                    contact_form_field("Full Name", "name", "John Doe"),
                    contact_form_field(
                        "Email Address",
                        "email",
                        "john.doe@example.com",
                        field_type="email",
                    ),
                    class_name="grid md:grid-cols-2 gap-6",
                ),
                contact_form_field("Subject", "subject", "Regarding AI Solutions"),
                rx.el.div(
                    rx.el.label(
                        "Message",
                        class_name="block text-sm font-medium text-gray-700 mb-1",
                    ),
                    rx.el.textarea(
                        name="message",
                        placeholder="Your message here...",
                        required=True,
                        rows=5,
                        class_name="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500 transition-shadow",
                    ),
                ),
                rx.el.button(
                    "Send Message",
                    type="submit",
                    class_name="w-full px-8 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors font-semibold shadow-lg hover:shadow-blue-500/30",
                ),
                on_submit=AppState.submit_contact_form,
                reset_on_submit=True,
                class_name="space-y-6",
            ),
        ),
    )


def contact_info() -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            "Contact Information", class_name="text-3xl font-bold text-gray-900 mb-6"
        ),
        rx.el.div(
            rx.el.div(
                rx.icon("mail", class_name="h-6 w-6 text-blue-600"),
                rx.el.div(
                    rx.el.h3("Email", class_name="font-semibold text-gray-800"),
                    rx.el.a(
                        "support@dhaadhsolutions.com",
                        href="mailto:support@dhaadhsolutions.com",
                        class_name="text-gray-600 hover:text-blue-500",
                    ),
                ),
                class_name="flex items-start gap-4 p-4 bg-gray-50 rounded-lg",
            ),
            rx.el.div(
                rx.icon("phone", class_name="h-6 w-6 text-blue-600"),
                rx.el.div(
                    rx.el.h3("Phone", class_name="font-semibold text-gray-800"),
                    rx.el.p("+91-8179675679", class_name="text-gray-600"),
                ),
                class_name="flex items-start gap-4 p-4 bg-gray-50 rounded-lg",
            ),
            rx.el.div(
                rx.icon("map-pin", class_name="h-6 w-6 text-blue-600"),
                rx.el.div(
                    rx.el.h3("Office", class_name="font-semibold text-gray-800"),
                    rx.el.p("Hyderabad, India", class_name="text-gray-600"),
                ),
                class_name="flex items-start gap-4 p-4 bg-gray-50 rounded-lg",
            ),
            class_name="space-y-4",
        ),
    )


def currency_selector() -> rx.Component:
    return rx.el.div(
        rx.el.label(
            "Select Currency", class_name="block text-sm font-medium text-gray-700 mb-2"
        ),
        rx.el.div(
            rx.foreach(
                AppState.currencies,
                lambda currency: rx.el.button(
                    rx.el.span(currency["flag"], class_name="text-lg"),
                    rx.el.span(currency["code"], class_name="font-semibold"),
                    on_click=lambda: AppState.select_currency(currency["code"]),
                    class_name=rx.cond(
                        AppState.selected_currency == currency["code"],
                        "flex items-center gap-2 px-4 py-2 rounded-lg border-2 border-blue-500 bg-blue-50 transition-all",
                        "flex items-center gap-2 px-4 py-2 rounded-lg border border-gray-300 bg-white hover:bg-gray-50 transition-all",
                    ),
                ),
            ),
            class_name="flex gap-2 overflow-x-auto pb-2",
        ),
        class_name="w-full mb-6",
    )


def payment_section() -> rx.Component:
    return rx.el.div(
        rx.el.h2("Make a Payment", class_name="text-3xl font-bold text-gray-900 mb-6"),
        currency_selector(),
        rx.cond(
            AppState.show_qr_code,
            rx.el.div(
                rx.image(
                    src=AppState.paynow_qr_code_url,
                    class_name="w-48 h-48 mx-auto rounded-lg border p-1",
                ),
                rx.el.p(
                    "Scan the QR code with your banking app.",
                    class_name="text-center text-sm text-gray-600 mt-2",
                ),
                class_name="flex flex-col items-center justify-center p-4 bg-gray-50 rounded-lg",
            ),
            rx.el.div(
                rx.el.p(
                    f"You are paying in {AppState.selected_currency}.",
                    class_name="text-sm text-gray-600",
                ),
                rx.el.input(
                    placeholder=AppState.amount_placeholder,
                    type="number",
                    on_change=AppState.set_payment_amount,
                    class_name="w-full px-4 py-2 mt-2 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500 transition-shadow",
                ),
                rx.el.button(
                    "Pay Now",
                    on_click=AppState.initiate_payment,
                    class_name="w-full mt-4 px-8 py-3 bg-green-600 text-white rounded-lg hover:bg-green-700 transition-colors font-semibold shadow-lg hover:shadow-green-500/30",
                ),
                class_name="space-y-4",
            ),
        ),
        rx.el.p(
            AppState.payment_status, class_name="mt-4 text-sm text-gray-600 text-center"
        ),
        class_name="bg-white p-8 md:p-12 rounded-2xl border border-gray-200 shadow-sm",
    )


def contact() -> rx.Component:
    return base_layout(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "We're here to help. Whether you have a question about our services or want to start a project, we'd love to hear from you.",
                    class_name="mt-6 text-lg text-gray-600 text-center max-w-3xl mx-auto",
                ),
                class_name="py-12 text-center",
            ),
            rx.el.div(
                contact_info(),
                rx.el.div(
                    rx.el.div(
                        contact_form(),
                        class_name="bg-white p-8 md:p-12 rounded-2xl border border-gray-200 shadow-sm",
                    ),
                    rx.el.div(payment_section()),
                    class_name="grid gap-8 items-start",
                ),
                class_name="grid lg:grid-cols-2 gap-16 max-w-7xl mx-auto px-4 pb-16 items-start",
            ),
            on_mount=AppState.reset_contact_form,
        )
    )