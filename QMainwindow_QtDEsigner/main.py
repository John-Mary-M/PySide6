from PySide6.QtWidgets import QApplication
from views import TextEditor_App

app = QApplication([])
window = TextEditor_App(app)
window.show()
app.exec()