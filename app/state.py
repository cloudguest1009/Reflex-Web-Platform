import reflex as rx
import asyncio
from typing import TypedDict, Optional


class Service(TypedDict):
    title: str
    description: str
    image: str
    bg_gradient: str


class ServiceDetail(Service):
    points: list[str]


class TrainingCourse(TypedDict):
    title: str
    description: str
    duration: str
    level: str


class BlogPost(TypedDict):
    title: str
    author: str
    date: str
    image: str
    content_preview: str


class NewsFeedItem(TypedDict):
    title: str
    platform: str
    date: str
    link: str
    preview: str


class AppState(rx.State):
    services: list[Service] = [
        {
            "title": "AI Solutions",
            "description": "Unlock the power of artificial intelligence to drive innovation and efficiency in your business.",
            "image": "/ai-solutions.svg",
            "bg_gradient": "bg-gradient-to-br from-blue-500 to-indigo-600",
        },
        {
            "title": "Embedded Solutions",
            "description": "Custom firmware and hardware solutions for IoT and specialized devices.",
            "image": "/embedded-solutions.svg",
            "bg_gradient": "bg-gradient-to-br from-cyan-500 to-sky-600",
        },
        {
            "title": "Automotive Solutions",
            "description": "Advanced software for infotainment, ADAS, and connected vehicle platforms.",
            "image": "/automotive-solutions.svg",
            "bg_gradient": "bg-gradient-to-br from-slate-500 to-gray-600",
        },
        {
            "title": "Engineering Solutions",
            "description": "Leverage our expert engineering services to build robust, scalable, and cutting-edge products.",
            "image": "/engineering-solutions.svg",
            "bg_gradient": "bg-gradient-to-br from-emerald-500 to-green-600",
        },
        {
            "title": "Automation Solutions",
            "description": "Streamline your operations and reduce manual effort with our intelligent automation platforms.",
            "image": "/automation-solutions.svg",
            "bg_gradient": "bg-gradient-to-br from-purple-500 to-violet-600",
        },
        {
            "title": "Gateway Solutions",
            "description": "Secure and scalable gateway solutions for managing data flow and connectivity.",
            "image": "/gateway-solutions.svg",
            "bg_gradient": "bg-gradient-to-br from-orange-500 to-amber-600",
        },
    ]
    services_details: list[ServiceDetail] = [
        {
            "title": "AI Solutions",
            "description": "Unlock the power of artificial intelligence to drive innovation and efficiency in your business.",
            "image": "/ai-solutions.svg",
            "bg_gradient": "bg-gradient-to-br from-blue-500 to-indigo-600",
            "points": [
                "Predictive Analytics & Forecasting",
                "Natural Language Processing (NLP)",
                "Computer Vision Systems",
                "Custom Machine Learning Models",
            ],
        },
        {
            "title": "Embedded Solutions",
            "description": "Custom firmware and hardware solutions for IoT and specialized devices.",
            "image": "/embedded-solutions.svg",
            "bg_gradient": "bg-gradient-to-br from-cyan-500 to-sky-600",
            "points": [
                "Firmware Development",
                "Real-Time Operating Systems (RTOS)",
                "Hardware Abstraction Layers (HAL)",
                "IoT Device Integration",
            ],
        },
        {
            "title": "Automotive Solutions",
            "description": "Advanced software for infotainment, ADAS, and connected vehicle platforms.",
            "image": "/automotive-solutions.svg",
            "bg_gradient": "bg-gradient-to-br from-slate-500 to-gray-600",
            "points": [
                "In-Vehicle Infotainment (IVI)",
                "ADAS Software Development",
                "CAN, LIN, Ethernet Protocol Stacks",
                "AUTOSAR Compliant Solutions",
            ],
        },
        {
            "title": "Engineering Solutions",
            "description": "Leverage our expert engineering services to build robust, scalable, and cutting-edge products.",
            "image": "/engineering-solutions.svg",
            "bg_gradient": "bg-gradient-to-br from-emerald-500 to-green-600",
            "points": [
                "Cloud-Native Application Development",
                "DevOps & CI/CD Implementation",
                "System Architecture Design",
                "API & Microservices Development",
            ],
        },
        {
            "title": "Automation Solutions",
            "description": "Streamline your operations and reduce manual effort with our intelligent automation platforms.",
            "image": "/automation-solutions.svg",
            "bg_gradient": "bg-gradient-to-br from-purple-500 to-violet-600",
            "points": [
                "Robotic Process Automation (RPA)",
                "Business Process Automation (BPA)",
                "Automated Quality Assurance",
                "Infrastructure Automation",
            ],
        },
        {
            "title": "Gateway Solutions",
            "description": "Secure and scalable gateway solutions for managing data flow and connectivity.",
            "image": "/gateway-solutions.svg",
            "bg_gradient": "bg-gradient-to-br from-orange-500 to-amber-600",
            "points": [
                "IoT Gateway Development",
                "API Gateway Management",
                "Cloud-to-Device Communication",
                "Secure OTA Updates",
            ],
        },
    ]
    training_courses: list[TrainingCourse] = [
        {
            "title": "AI & Machine Learning",
            "description": "Comprehensive training from fundamentals to advanced applications in AI and ML.",
            "duration": "12 Weeks",
            "level": "Beginner to Advanced",
        },
        {
            "title": "Embedded Systems",
            "description": "Deep dive into firmware, RTOS, and hardware interfacing for embedded devices.",
            "duration": "10 Weeks",
            "level": "Intermediate",
        },
        {
            "title": "Automotive Electronics",
            "description": "Master the complexities of automotive software, including AUTOSAR and ADAS.",
            "duration": "8 Weeks",
            "level": "Advanced",
        },
    ]
    all_newsfeeds: list[NewsFeedItem] = [
        {
            "title": "Exploring the Future of Automotive Software",
            "platform": "linkedin",
            "date": "2024-08-01",
            "link": "#",
            "preview": "A new article on the challenges and opportunities in modern automotive software engineering...",
        },
        {
            "title": "Introduction to Embedded Systems",
            "platform": "youtube",
            "date": "2024-07-29",
            "link": "#",
            "preview": "Check out our new video series covering the fundamentals of embedded systems development...",
        },
        {
            "title": "The Role of AI in Industrial Automation",
            "platform": "linkedin",
            "date": "2024-07-25",
            "link": "#",
            "preview": "How DhaAdh Solutions is leveraging AI to transform industrial automation processes...",
        },
        {
            "title": "DhaAdh Solutions Company Launch",
            "platform": "instagram",
            "date": "2024-07-22",
            "link": "#",
            "preview": "We are excited to announce the launch of DhaAdh Solutions! Follow us for updates...",
        },
    ]
    contact_form_data: dict = {}
    contact_submitted: bool = False
    contact_submission_message: str = ""
    current_service_index: int = 0
    is_playing: bool = True

    @rx.var
    def current_service(self) -> Service:
        return self.services[self.current_service_index]

    @rx.event(background=True)
    async def carousel_worker(self):
        while self.is_playing:
            await asyncio.sleep(5)
            async with self:
                if self.is_playing:
                    self.current_service_index = (self.current_service_index + 1) % len(
                        self.services
                    )

    @rx.event
    def on_load_and_scroll(self) -> rx.event.EventSpec:
        return AppState.carousel_worker

    @rx.event
    def toggle_play_pause(self) -> rx.event.EventSpec | None:
        self.is_playing = not self.is_playing
        if self.is_playing:
            return AppState.carousel_worker
        return

    @rx.event
    def set_service_index(self, index: int):
        self.current_service_index = index
        self.is_playing = False

    @rx.event
    def submit_contact_form(self, form_data: dict):
        self.contact_form_data = form_data
        print(f"Contact form submitted: {self.contact_form_data}")
        self.contact_submitted = True
        self.contact_submission_message = (
            f"Thank you, {form_data['name']}! Your message has been received."
        )
        yield AppState.reset_contact_form

    @rx.event
    def reset_contact_form(self):
        self.contact_form_data = {}