# Import QMessageBox from PyQt6.QtWidgets library
# This allows us to display pop-up messages to the user
from PyQt6.QtWidgets import QMessageBox

# Define a class called AuthController
class AuthController:

    # This function is called when the controller is created
    # It takes two arguments:
    #   - user_model: This is an object that represents the user data and logic (likely from another file)
    #   - auth_window: This is the window object for user authentication (likely created in another file)
    def __init__(self, user_model, auth_window):
        self.user_model = user_model  # Store the user model object
        self.auth_window = auth_window  # Store the authentication window object

    # This function handles the login process
    # It takes two arguments:
    #   - username: The username entered by the user
    #   - password: The password entered by the user
    def login(self, username, password):
        # Check if username or password is empty
        if not username or not password:
            # Show an error message if fields are empty
            self._show_error("Please fill in all fields")
            return  # Exit the function if fields are empty

        # Try to log in the user using the user_model object
        if self.user_model.login(username, password):
            # If login is successful, emit a signal to the auth_window (likely for UI updates)
            self.auth_window.login_successful.emit()
        else:
            # Show an error message if login fails
            self._show_error("Invalid credentials")

    # This function handles the registration process
    # It takes two arguments:
    #   - username: The username chosen by the user
    #   - password: The password chosen by the user
    def register(self, username, password):
        # Check if username or password is empty
        if not username or not password:
            # Show an error message if fields are empty
            self._show_error("Please fill in all fields")
            return  # Exit the function if fields are empty

        # Try to register the user using the user_model object
        if self.user_model.register(username, password):
            # Show a success message if registration is successful
            self._show_success("Registration successful")
        else:
            # Show an error message if username already exists
            self._show_error("Username already exists")

    # This private function shows an error message to the user
    def _show_error(self, message):
        # Use QMessageBox to display an error message with title "Error"
        QMessageBox.critical(self.auth_window, "Error", message)

    # This private function shows a success message to the user
    def _show_success(self, message):
        # Use QMessageBox to display a success message with title "Success"
        QMessageBox.information(self.auth_window, "Success", message)