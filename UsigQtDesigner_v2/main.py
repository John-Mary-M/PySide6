from PySide6.QtWidgets import QApplication
from view import User_Interface

app = QApplication([])

window = User_Interface()
window.show_ui()

app.exec()