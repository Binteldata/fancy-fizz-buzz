# Directory structure:
# fizzbuzz_app/
#   ├── main.py
#   ├── config/
#   │   └── settings.py
#   ├── models/
#   │   ├── __init__.py
#   │   └── user.py
#   ├── views/
#   │   ├── __init__.py
#   │   ├── auth_window.py
#   │   ├── dashboard.py
#   │   ├── fizzbuzz_widget.py
#   │   └── styles.py
#   ├── controllers/
#   │   ├── __init__.py
#   │   ├── auth_controller.py
#   │   └── fizzbuzz_controller.py
#   └── utils/
#       ├── __init__.py
#       └── fizzbuzz_implementations.py

# config/settings.py
import os

class Settings:
    APP_NAME = "FizzBuzz Professional"
    DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "users.json")
    DARK_THEME = True
    
# utils/fizzbuzz_implementations.py
class FizzBuzzImplementations:
    @staticmethod
    def if_else_impl(n):
        result = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result

    @staticmethod
    def while_impl(n):
        result = []
        i = 1
        while i <= n:
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
            i += 1
        return result

    @staticmethod
    def function_impl(n):
        def fizzbuzz(num):
            if num % 3 == 0 and num % 5 == 0:
                return "FizzBuzz"
            elif num % 3 == 0:
                return "Fizz"
            elif num % 5 == 0:
                return "Buzz"
            return str(num)
        return [fizzbuzz(i) for i in range(1, n + 1)]

    class ClassImpl:
        def __init__(self, n):
            self.n = n
        
        def generate(self):
            return [
                "FizzBuzz" if i % 15 == 0 else
                "Fizz" if i % 3 == 0 else
                "Buzz" if i % 5 == 0 else
                str(i)
                for i in range(1, self.n + 1)
            ]

# models/user.py
import json
import hashlib
import os
from config.settings import Settings

class UserModel:
    def __init__(self):
        self.users_file = Settings.DB_PATH
        os.makedirs(os.path.dirname(self.users_file), exist_ok=True)
        self.current_user = None
        self.load_users()

    def load_users(self):
        if not os.path.exists(self.users_file):
            self.users = {}
            self.save_users()
        else:
            with open(self.users_file, 'r') as f:
                self.users = json.load(f)

    def save_users(self):
        with open(self.users_file, 'w') as f:
            json.dump(self.users, f)

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def register(self, username, password):
        if username in self.users:
            return False
        self.users[username] = self.hash_password(password)
        self.save_users()
        return True

    def login(self, username, password):
        if username in self.users and self.users[username] == self.hash_password(password):
            self.current_user = username
            return True
        return False

# views/styles.py
from PyQt6.QtCore import Qt

STYLE_SHEET = """
QMainWindow {
    background-color: #1e1e1e;
}

QWidget {
    color: #ffffff;
    font-family: 'Segoe UI', Arial, sans-serif;
}

QPushButton {
    background-color: #0078d4;
    border: none;
    color: white;
    padding: 8px 16px;
    border-radius: 4px;
    font-size: 14px;
}

QPushButton:hover {
    background-color: #1084d8;
}

QPushButton:pressed {
    background-color: #006cc1;
}

QLineEdit {
    padding: 8px;
    background-color: #2d2d2d;
    border: 1px solid #3d3d3d;
    border-radius: 4px;
    color: white;
}

QTextEdit {
    background-color: #2d2d2d;
    border: 1px solid #3d3d3d;
    border-radius: 4px;
    padding: 8px;
    color: white;
}

QTabWidget::pane {
    border: 1px solid #3d3d3d;
    background-color: #2d2d2d;
}

QTabBar::tab {
    background-color: #1e1e1e;
    color: white;
    padding: 8px 16px;
    border-top-left-radius: 4px;
    border-top-right-radius: 4px;
}

QTabBar::tab:selected {
    background-color: #2d2d2d;
}

QLabel {
    color: white;
    font-size: 14px;
}

QMessageBox {
    background-color: #2d2d2d;
}
"""

# views/auth_window.py
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                           QLineEdit, QPushButton, QFrame)
from PyQt6.QtCore import pyqtSignal

class AuthWindow(QWidget):
    login_successful = pyqtSignal()

    def __init__(self, auth_controller):
        super().__init__()
        self.auth_controller = auth_controller
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        
        # Title
        title = QLabel("FizzBuzz Professional")
        title.setStyleSheet("font-size: 24px; font-weight: bold; margin: 20px;")
        layout.addWidget(title, alignment=Qt.AlignmentFlag.AlignHCenter)

        # Form container
        form_container = QFrame()
        form_container.setStyleSheet("""
            QFrame {
                background-color: #2d2d2d;
                border-radius: 8px;
                padding: 20px;
            }
        """)
        form_layout = QVBoxLayout()

        # Username
        self.username_entry = QLineEdit()
        self.username_entry.setPlaceholderText("Username")
        form_layout.addWidget(QLabel("Username"))
        form_layout.addWidget(self.username_entry)

        # Password
        self.password_entry = QLineEdit()
        self.password_entry.setPlaceholderText("Password")
        self.password_entry.setEchoMode(QLineEdit.EchoMode.Password)
        form_layout.addWidget(QLabel("Password"))
        form_layout.addWidget(self.password_entry)

        # Buttons
        button_layout = QHBoxLayout()
        self.login_button = QPushButton("Login")
        self.register_button = QPushButton("Register")
        self.register_button.setStyleSheet("""
            background-color: #107c41;
        """)
        
        button_layout.addWidget(self.login_button)
        button_layout.addWidget(self.register_button)
        form_layout.addLayout(button_layout)

        form_container.setLayout(form_layout)
        layout.addWidget(form_container)

        self.setLayout(layout)

        # Connect signals
        self.login_button.clicked.connect(self.login)
        self.register_button.clicked.connect(self.register)

    def login(self):
        self.auth_controller.login(
            self.username_entry.text(),
            self.password_entry.text()
        )

    def register(self):
        self.auth_controller.register(
            self.username_entry.text(),
            self.password_entry.text()
        )

# views/fizzbuzz_widget.py
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                           QLineEdit, QPushButton, QTextEdit)
from PyQt6.QtCore import Qt

class FizzBuzzWidget(QWidget):
    def __init__(self, implementation, title, controller):
        super().__init__()
        self.implementation = implementation
        self.title = title
        self.controller = controller
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        # Title
        title_label = QLabel(self.title)
        title_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title_label, alignment=Qt.AlignmentFlag.AlignHCenter)

        # Input area
        input_layout = QHBoxLayout()
        input_layout.addWidget(QLabel("Enter N:"))
        self.n_entry = QLineEdit()
        self.n_entry.setFixedWidth(100)
        input_layout.addWidget(self.n_entry)
        
        generate_btn = QPushButton("Generate")
        generate_btn.clicked.connect(self.generate)
        input_layout.addWidget(generate_btn)
        input_layout.addStretch()
        
        layout.addLayout(input_layout)

        # Result area
        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        layout.addWidget(self.result_text)

        self.setLayout(layout)

    def generate(self):
        self.controller.generate_fizzbuzz(
            self.implementation,
            self.n_entry.text(),
            self.result_text
        )

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

# controllers/auth_controller.py
from PyQt6.QtWidgets import QMessageBox

class AuthController:
    def __init__(self, user_model, auth_window):
        self.user_model = user_model
        self.auth_window = auth_window

    def login(self, username, password):
        if not username or not password:
            self._show_error("Please fill in all fields")
            return
            
        if self.user_model.login(username, password):
            self.auth_window.login_successful.emit()
        else:
            self._show_error("Invalid credentials")

    def register(self, username, password):
        if not username or not password:
            self._show_error("Please fill in all fields")
            return
            
        if self.user_model.register(username, password):
            self._show_success("Registration successful")
        else:
            self._show_error("Username already exists")

    def _show_error(self, message):
        QMessageBox.critical(self.auth_window, "Error", message)

    def _show_success(self, message):
        QMessageBox.information(self.auth_window, "Success", message)

# controllers/fizzbuzz_controller.py
from PyQt6.QtWidgets import QMessageBox

class FizzBuzzController:
    def generate_fizzbuzz(self, implementation, n_text, result_widget):
        try:
            n = int(n_text)
            if n <= 0:
                raise ValueError
            
            if isinstance(implementation, type):
                result = implementation(n).generate()
            else:
                result = implementation(n)
                
            result_widget.setPlainText("\n".join(result))
            
        except ValueError:
            QMessageBox.critical(
                None,
                "Error",
                "Please enter a positive integer"
            )

# main.py
import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt
from models.user import UserModel
from views.auth_window import AuthWindow
from views.dashboard import Dashboard
from controllers.auth_controller import AuthController
from controllers.fizzbuzz_controller import FizzBuzzController
from views.styles import STYLE_SHEET
from config.settings import Settings

class FizzBuzzApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.app.setStyleSheet(STYLE_SHEET)
        
        # Initialize models
        self.user_model = UserModel()
        
        # Initialize controllers
        self.fizzbuzz_controller = FizzBuzzController()
        
        # Initialize views
        self.auth_window = AuthWindow(None)  # Will set controller later
        self.auth_controller = AuthController(self.user_model, self.auth_window)
        self.auth_window.auth_controller = self.auth_controller
        
        # Connect signals
        self.auth_window.login_successful.connect(self.show_dashboard)
        
    def show_dashboard(self):
        self.dashboard = Dashboard(self.user_model, self.fizzbuzz_controller)
        self.dashboard.show()
        self.auth_window.close()

    def run(self):
        self.auth_window.show()
        sys.exit(self.app.exec())

if __name__ == "__main__":
    FizzBuzzApp().run()
