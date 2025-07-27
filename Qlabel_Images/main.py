from PySide6.QtWidgets import QApplication
from view import Widget

app = QApplication()

window = Widget()
window.show()

app.exec()