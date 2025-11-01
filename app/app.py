import reflex as rx
from app.pages.home import home
from app.pages.about import about
from app.pages.services import services
from app.pages.training import training
from app.pages.contact import contact
from app.pages.newsfeed import newsfeed
from app.state import AppState


def index() -> rx.Component:
    return home()


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Lato:wght@400;700;900&display=swap",
            rel="stylesheet",
        ),
        rx.el.script(src="https://checkout.razorpay.com/v1/checkout.js"),
        rx.el.script(src="/payment.js"),
    ],
)
app.add_page(index, route="/", title="DhaAdh Solutions - Home")
app.add_page(about, route="/about", title="About Us")
app.add_page(services, route="/services", title="Our Services")
app.add_page(training, route="/training", title="Training")
app.add_page(contact, route="/contact", title="Contact Us")
app.add_page(newsfeed, route="/newsfeed", title="NewsFeed")