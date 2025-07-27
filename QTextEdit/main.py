from PySide6.QtWidgets import QApplication
from view import Text_Editor

app = QApplication()

window = Text_Editor()
window.show()
app.exec()