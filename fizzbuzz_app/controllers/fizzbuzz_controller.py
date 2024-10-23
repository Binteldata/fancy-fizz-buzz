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