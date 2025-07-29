from PySide6.QtWidgets import QApplication
from view import QlistDemo

app = QApplication([])
window = QlistDemo()
window.show()
app.exec()