# 1/08/2025 
from PySide6.QtWidgets import QWidget
from ui_Cwidget import Ui_Custom_Widget

class Custom_Widget_App(QWidget,  Ui_Custom_Widget):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle('Add or Subtract')
        self.spin_Box.setValue(50)
        self.plus_btn.clicked.connect(self.plus)
        self.minus_btn.clicked.connect(self.minus)

    def plus (self):
        value = self.spin_Box.value()
        self.spin_Box.setValue(value + 1)

    def minus (self):
        value = self.spin_Box.value()
        self.spin_Box.setValue(value - 1)