from PySide6.QtWidgets import QApplication
from view import QComboBox_Demo

app = QApplication([])
window = QComboBox_Demo()
window.show()
app.exec()