# views/dashboard.py
from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QLabel, QTabWidget)
from .fizzbuzz_widget import FizzBuzzWidget
from utils.fizzbuzz_implementations import FizzBuzzImplementations

class Dashboard(QMainWindow):
    def __init__(self, user_model, fizzbuzz_controller):
        super().__init__()
        self.user_model = user_model
        self.fizzbuzz_controller = fizzbuzz_controller
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("FizzBuzz Professional - Dashboard")
        self.setMinimumSize(800, 600)

        # Central widget
        central_widget = QWidget()
        layout = QVBoxLayout()

        # Welcome message
        welcome = QLabel(f"Welcome, {self.user_model.current_user}!")
        welcome.setStyleSheet("font-size: 20px; margin: 10px;")
        layout.adWidget(welcome)

        # Tab widget
        tabs = QTabWidget()
        implementations = [
            ("If-Else Implementation", FizzBuzzImplementations.if_else_impl),
            ("While Loop Implementation", FizzBuzzImplementations.while_impl),
            ("Function Implementation", FizzBuzzImplementations.function_impl),
            ("Class Implementation", FizzBuzzImplementations.ClassImpl)
        ]

        for title, impl in implementations:
            widget = FizzBuzzWidget(impl, title, self.fizzbuzz_controller)
            tabs.addTab(widget, title.split()[0])

        layout.addWidget(tabs)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)