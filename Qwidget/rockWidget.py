from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton

class RockWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rock Widget")

        button1 = QPushButton("Button 1")
        button1.clicked.connect(self.button1_clicked)
        button2 = QPushButton("Button 2")
        button2.clicked.connect(self.button2_clicked)
        button3 = QPushButton("Button 3")
        button3.clicked.connect(self.button3_clicked)

        button_layout = QHBoxLayout()
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)
        button_layout.addWidget(button3)

        self.setLayout(button_layout)

    def button1_clicked(self):
        print("Button 1 clicked")

    def button2_clicked(slef):
        print("Button 2 clicked")

    def button3_clicked(self):
        print("Button 3 clicked")