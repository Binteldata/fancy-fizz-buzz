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