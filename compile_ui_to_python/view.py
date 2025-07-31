# 31/07/2025
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from ui_widget import Ui_Widget

class Custom_Widget(QWidget, Ui_Widget):    # Ui_Widget is the class that was generated when we compiled the ui file
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("User Data")
        self.submit_btn.clicked.connect(self.do_something)

    def do_something(self):
        print(f"{self.full_name_line_edit.text()} is a {self.occupation_line_edit.text()}")