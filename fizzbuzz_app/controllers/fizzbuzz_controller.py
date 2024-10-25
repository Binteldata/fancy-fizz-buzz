# Import QMessageBox from PyQt6.QtWidgets library
# This allows us to display pop-up messages to the user
from PyQt6.QtWidgets import QMessageBox

# Define a class called FizzBuzzController
class FizzBuzzController:

    # This function takes three arguments:
    #   - implementation: This can be either a class or a function that implements the FizzBuzz logic
    #   - n_text: The text entered by the user, representing the number for FizzBuzz
    #   - result_widget: This is a UI element (likely a text box) where the result will be displayed
    def generate_fizzbuzz(self, implementation, n_text, result_widget):
        try:
            # Try to convert the entered text (n_text) to an integer (n)
            n = int(n_text)

            # Check if the number is positive (n must be greater than 0)
            if n <= 0:
                # Raise a ValueError if the number is not positive
                raise ValueError

            # Check if the implementation is a class type
            if isinstance(implementation, type):
                # If it's a class, create an instance of that class and call its generate() method
                result = implementation(n).generate()
            else:
                # If it's not a class, assume it's a function and call it directly with n
                result = implementation(n)

            # Join the results list with newline characters and set the text in the result_widget
            result_widget.setPlainText("\n".join(result))

        except ValueError:
            # If there's an error converting the text or the number is not positive
            # Show an error message to the user using QMessageBox
            QMessageBox.critical(
                None,  # Parent window can be set to None for a global pop-up
                "Error",
                "Please enter a positive integer"
            )