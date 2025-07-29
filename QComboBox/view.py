from PySide6.QtWidgets import QComboBox, QWidget, QPushButton, QVBoxLayout

class QComboBox_Demo(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QComboBox Demo")

        # dropdown menu.
        self.drop_down = QComboBox(self)

        # add planents to the combbox
        self.drop_down.addItems([
            'Earth',
            'Mars',
            'Neptune',
            'Saturn',
            'Venus',
            'Pluto'
        ])

        btn_current_value = QPushButton("Current Value")
        btn_set_current_value = QPushButton("Set Value")
        btn_get_values = QPushButton("Get Values")
        #
        btn_current_value.clicked.connect(self.current_value)
        btn_set_current_value.clicked.connect(self.set_current)
        btn_get_values.clicked.connect(self.get_values)

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.drop_down)
        v_layout.addWidget(btn_current_value)
        v_layout.addWidget(btn_set_current_value)
        v_layout.addWidget(btn_get_values)
        v_layout.addSpacing(100)

        self.setLayout(v_layout)

    def current_value(self):
        print(f'Current selected item : {self.drop_down.currentText()}\nCurrent Index : {self.drop_down.currentIndex()}')

    def set_current(self):
        self.drop_down.setCurrentIndex(2)

    def get_values(self):
        for i in range(self.drop_down.count()):
            print(f"index [ i ] : {self.drop_down.itemText(i)}")

