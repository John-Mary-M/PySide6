from PySide6.QtWidgets import QApplication
from view import QtabWidget_Demo

app = QApplication([])
window = QtabWidget_Demo()
window.show()

app.exec()