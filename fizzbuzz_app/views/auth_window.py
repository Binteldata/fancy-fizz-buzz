# views/auth_window.py
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QFrame)
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
