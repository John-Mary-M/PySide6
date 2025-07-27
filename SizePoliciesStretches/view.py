from PySide6.QtWidgets import QWidget, QSizePolicy, QPushButton, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout

class SizeP(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Sizes and Stretches")

        # Size Policy: How widgets behave if container space is expanded or shrinked
        label = QLabel("Some Text : ")
        input = QLineEdit()
        btn_one = QPushButton("One")
        btn_two = QPushButton("Two")
        btn_three = QPushButton("Three")

        # To make the input/ lineEdit expand horizonatally but not vertically
        input.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        # label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        h_layout = QHBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(input)

        # stretches control how much space is taken up by a widget on the interface
        h_layout_2 = QHBoxLayout()
        h_layout_2.addWidget(btn_one, 2) # second parameter defines the stretches. here btn_one stretches twice as much as btn_2 and btn_3
        h_layout_2.addWidget(btn_two, 1)
        h_layout_2.addWidget(btn_three, 1)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addLayout(h_layout_2)

        self.setLayout(v_layout)
