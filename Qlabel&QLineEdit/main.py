from PySide6.QtWidgets import QApplication
from view import LabelEdit

app = QApplication()
window = LabelEdit()
window.show()
app.exec()