# views/dashboard.py
from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QLabel, 
                             QTabWidget)
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
        layout.addWidget(welcome)

        # Tab widget
        tabs = QTabWidget()
        implementations = [
            ("If-Else Implementation", FizzBuzzImplementations.if_else_impl, '''# If-Else Implementation Code\nfor i in range(1, n + 1):\n    if i % 3 == 0 and i % 5 == 0:\n        result.append("FizzBuzz")\n    elif i % 3 == 0:\n        result.append("Fizz")\n    elif i % 5 == 0:\n        result.append("Buzz")\n    else:\n        result.append(str(i))'''),
            ("While Loop Implementation", FizzBuzzImplementations.while_impl, '''# While Loop Implementation Code\nwhile i <= n:\n    if i % 3 == 0 and i % 5 == 0:\n        result.append("FizzBuzz")\n    elif i % 3 == 0:\n        result.append("Fizz")\n    elif i % 5 == 0:\n        result.append("Buzz")\n    else:\n        result.append(str(i))\n    i += 1'''),
            ("Function Implementation", FizzBuzzImplementations.function_impl, '''# Function Implementation Code\ndef fizzbuzz(num):\n    if num % 3 == 0 and num % 5 == 0:\n        return "FizzBuzz"\n    elif num % 3 == 0:\n        return "Fizz"\n    elif num % 5 == 0:\n        return "Buzz"\n    return str(num)'''),
            ("Class Implementation", FizzBuzzImplementations.ClassImpl, '''# Class Implementation Code\nclass FizzBuzz:\n    def __init__(self, n):\n        self.n = n\n\n    def generate(self):\n        return ["FizzBuzz" if i % 15 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else str(i) for i in range(1, self.n + 1)]''')
        ]

        for title, impl, code in implementations:
            widget = FizzBuzzWidget(impl, title, self.fizzbuzz_controller, code)
            tabs.addTab(widget, title.split()[0])

        layout.addWidget(tabs)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
