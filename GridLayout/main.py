from PySide6.QtWidgets import QApplication
from view import GridLayoutApp

app = QApplication([])
window = GridLayoutApp()
window.show()
app.exec()