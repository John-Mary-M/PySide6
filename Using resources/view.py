# 1/08/2025 
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QIcon
from ui_Cwidget import Ui_Custom_Widget

import resource_rc # this is the hook to displaying the compiled resources

class Custom_Widget_App(QWidget,  Ui_Custom_Widget):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle('Add or Subtract')
        self.spin_Box.setValue(50)
        self.plus_btn.clicked.connect(self.plus)
        self.minus_btn.clicked.connect(self.minus)

        # Icon locations from designer
        plus_icon = QIcon(':/images/plus.png')
        minus_icon = QIcon(':/images/minus.png')

        # set the icons
        self.plus_btn.setIcon(plus_icon)
        self.minus_btn.setIcon(minus_icon)

    def plus (self):
        value = self.spin_Box.value()
        self.spin_Box.setValue(value + 1)

    def minus (self):
        value = self.spin_Box.value()
        self.spin_Box.setValue(value - 1)