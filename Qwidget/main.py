from PySide6.QtWidgets import QApplication, QWidget
from rockWidget import RockWidget

app = QApplication()

window = RockWidget()
window.show()

app.exec()