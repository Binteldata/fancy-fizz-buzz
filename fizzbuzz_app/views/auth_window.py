# Import necessary libraries from PyQt6
from PyQt6.QtCore import Qt  # For alignment flags
from PyQt6.QtWidgets import (
    QWidget,  # Base class for windows
    QVBoxLayout, QHBoxLayout,  # Layout managers
    QLabel, QLineEdit, QPushButton, QFrame  # UI elements
)
from PyQt6.QtCore import pyqtSignal  # For custom signals

# Define a class called AuthWindow
class AuthWindow(QWidget):

    # Define a custom signal named login_successful that emits when login is successful
    login_successful = pyqtSignal()

    def __init__(self, auth_controller):
        # Call the superclass (QWidget) constructor
        super().__init__()

        # Store the provided auth_controller object
        self.auth_controller = auth_controller

        # Call the setup_ui method to create the user interface
        self.setup_ui()

    def setup_ui(self):
        # Create a vertical box layout for the main window
        layout = QVBoxLayout()

        # Create a label for the title
        title = QLabel("FizzBuzz Professional")
        # Set the style for the title (font size, weight, margin)
        title.setStyleSheet("font-size: 24px; font-weight: bold; margin: 20px;")
        # Add the title label to the layout with centered alignment
        layout.addWidget(title, alignment=Qt.AlignmentFlag.AlignHCenter)

        # Create a frame to hold the login form elements
        form_container = QFrame()
        # Set the style for the form container (background color, border radius, padding)
        form_container.setStyleSheet("""
            QFrame {
                background-color: #2d2d2d;
                border-radius: 8px;
                padding: 20px;
            }
        """)

        # Create a vertical box layout for the form elements
        form_layout = QVBoxLayout()

        # Create a label for the username field
        username_label = QLabel("Username")
        # Add the username label to the form layout
        form_layout.addWidget(username_label)

        # Create a line edit for username input
        self.username_entry = QLineEdit()
        # Set a placeholder text for the username field
        self.username_entry.setPlaceholderText("Username")
        # Add the username line edit to the form layout
        form_layout.addWidget(self.username_entry)

        # Create a label for the password field
        password_label = QLabel("Password")
        # Add the password label to the form layout
        form_layout.addWidget(password_label)

        # Create a line edit for password input
        self.password_entry = QLineEdit()
        # Set a placeholder text for the password field
        self.password_entry.setPlaceholderText("Password")
        # Set the password field to hide characters as they are typed (echo mode)
        self.password_entry.setEchoMode(QLineEdit.EchoMode.Password)
        # Add the password line edit to the form layout
        form_layout.addWidget(self.password_entry)

        # Create a horizontal box layout for the buttons
        button_layout = QHBoxLayout()

        # Create a button for login functionality
        self.login_button = QPushButton("Login")
        # Add the login button to the button layout
        button_layout.addWidget(self.login_button)

        # Create a button for registration functionality
        self.register_button = QPushButton("Register")
        # Set a custom style for the register button (background color)
        self.register_button.setStyleSheet("""
            background-color: #107c41;
        """)
        # Add the register button to the button layout
        button_layout.addWidget(self.register_button)

        # Add the button layout to the form layout
        form_layout.addLayout(button_layout)

        # Set the form layout as the layout for the form container
        form_container.setLayout(form_layout)

        # Add the form container to the main window layout
        layout.addWidget(form_container)

        # Set the main window layout
        self.setLayout(layout)

        # Connect button clicks to their corresponding methods
        self.login_button.clicked.connect(self.login)
        self.register_button.clicked.connect(self.register)

    def login(self):
        # Get username and password text from the line edits
        username = self.username_entry.text()
        password = self.password_entry.text()

        # Call the login method of the auth_controller with the obtained username and password
        self.auth_controller.login(username, password)
