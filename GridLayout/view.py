from PySide6.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy

class GridLayoutApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Playing with the Grid Layout")

        btn_one = QPushButton("One")
        btn_two = QPushButton("Two")
        btn_three = QPushButton("Three")
        btn_three.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        btn_four = QPushButton("Four")
        btn_five = QPushButton("Five")
        btn_six = QPushButton("Six")
        btn_seven = QPushButton("Seven")

        grid_layout = QGridLayout()
        grid_layout.addWidget(btn_one, 0,0)
        grid_layout.addWidget(btn_two, 0,1,1,2) # Take up 1 row and 2 columns
        grid_layout.addWidget(btn_three, 1,0,2,1) # Take up 2 rows and 1 column
        grid_layout.addWidget(btn_four, 1, 1)
        grid_layout.addWidget(btn_five, 1, 2)
        grid_layout.addWidget(btn_six, 2, 1)
        grid_layout.addWidget(btn_seven, 2, 2)

        self.setLayout(grid_layout)