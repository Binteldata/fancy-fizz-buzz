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