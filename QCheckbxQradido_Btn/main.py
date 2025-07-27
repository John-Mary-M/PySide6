from PySide6.QtWidgets import QApplication
from view import RadCheckBtn

app = QApplication([])
window = RadCheckBtn()
window.show()
app.exec()