from PySide6.QtWidgets import QApplication
from view import Custom_Widget
app = QApplication([])

window = Custom_Widget()
window.show()

app.exec()