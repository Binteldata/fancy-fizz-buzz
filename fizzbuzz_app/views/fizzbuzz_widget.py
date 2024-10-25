# views/fizzbuzz_widget.py
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QSplitter)
from PyQt6.QtCore import Qt

class FizzBuzzWidget(QWidget):
    def __init__(self, implementation, title, controller, code):
        super().__init__()
        self.implementation = implementation
        self.title = title
        self.controller = controller
        self.code = code
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        # Title
        title_label = QLabel(self.title)
        title_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title_label, alignment=Qt.AlignmentFlag.AlignHCenter)

        # Input area
        input_layout = QHBoxLayout()
        input_layout.addWidget(QLabel("Enter Number:"))
        self.n_entry = QLineEdit()
        self.n_entry.setFixedWidth(100)
        input_layout.addWidget(self.n_entry)
        
        generate_btn = QPushButton("Generate")
        generate_btn.clicked.connect(self.generate)
        input_layout.addWidget(generate_btn)
        input_layout.addStretch()
        
        layout.addLayout(input_layout)

        # Splitter to divide code and result areas
        splitter = QSplitter(Qt.Orientation.Horizontal)

        # Code area
        self.code_text = QTextEdit()
        self.code_text.setReadOnly(True)
        self.code_text.setPlainText(self.code)  # Display the FizzBuzz code
        splitter.addWidget(self.code_text)

        # Result area
        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        splitter.addWidget(self.result_text)

        layout.addWidget(splitter)

        self.setLayout(layout)

    def generate(self):
        self.controller.generate_fizzbuzz(
            self.implementation,
            self.n_entry.text(),
            self.result_text
        )
