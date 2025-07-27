# 27/07/2025    - Grid Layout
from PySide6.QtWidgets import QApplication
from view import GridLayoutApp

app = QApplication([])
window = GridLayoutApp()
window.show()
app.exec()