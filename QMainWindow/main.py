from PySide6.QtWidgets import QApplication
from view import MainWindow

app = QApplication()
window = MainWindow(app)
window.show()

app.exec()