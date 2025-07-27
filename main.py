# Version 1
"""
from PySide6.QtWidgets import  QApplication, QMainWindow, QPushButton

import sys

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("First Window App!")

button = QPushButton()
button.setText("Press Me")

window.setCentralWidget(button)
window.show()

app.exec()

"""

# Version 2: Putting the button/ window widget in its own class
"""
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Button Holder App")

        button = QPushButton("Press Me!")

        self.setCentralWidget(button)


app = QApplication()

window = ButtonHolder()
window.show()
app.exec()

"""

# Version 3: Seperate file handling the gui widgets
from PySide6.QtWidgets import QApplication
from buttonHolder import ButtonHolder

app = QApplication()

window = ButtonHolder()
window.show()

app.exec()
 