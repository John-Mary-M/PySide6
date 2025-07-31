from PySide6.QtCore import QObject
from PySide6.QtWidgets import QWidget
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()

class User_Interface(QObject):
    def __init__(self):
        super().__init__()
        self.ui = loader.load('widget.ui', None)    # load ui
        self.ui.setWindowTitle("User Data")     # set ui title
        self.ui.submit_btn.clicked.connect(self.do_something)   # connect slot

    def show_ui(self):
        self.ui.show()

    def do_something(self):
        print(f"{self.ui.full_name_line_edit.text()} is a {self.ui.occupation_line_edit.text()}")
