from PySide6.QtWidgets import QApplication
from view import Custom_Widget_App

app = QApplication([])
window = Custom_Widget_App()
window.show()
app.exec()