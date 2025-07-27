# 27/07/2025        QRadioButton & QCheckbox
from PySide6.QtWidgets import QWidget, QRadioButton, QCheckBox

class RadCheckBtn(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Radio Button and Checkbox")
        