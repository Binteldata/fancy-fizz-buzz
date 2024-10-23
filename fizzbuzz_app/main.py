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