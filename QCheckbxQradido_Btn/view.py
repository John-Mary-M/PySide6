# 27/07/2025        QRadioButton & QCheckbox
from PySide6.QtWidgets import QWidget, QRadioButton, QCheckBox, QGroupBox, QVBoxLayout, QButtonGroup, QHBoxLayout

class RadCheckBtn(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Radio Button and Checkbox")

        # Checkboxes: User can choose multiple operating systems
        os = QGroupBox("Choose operating system")
        windows = QCheckBox("Windows")
        windows.toggled.connect(self.windows_box_toggled)

        linux = QCheckBox("Linux")
        linux.toggled.connect(self.linux_box_toggled)

        mac  = QCheckBox("Mac")
        mac.toggled.connect(self.mac_box_toggled)

        os_layout = QVBoxLayout()
        os_layout.addWidget(windows)
        os_layout.addWidget(linux)
        os_layout.addWidget(mac)
        os.setLayout(os_layout)

        # Exclusive checkboxes: USer can only check one of the boxes
        drinks = QGroupBox("Choose your drink")

        beer = QCheckBox("Beer")
        juice = QCheckBox("Juice")
        coffee = QCheckBox("Coffee")
        beer.setChecked(True)    # beer option selected by default

        # Make checkboxes exclusive
        exclusive_butn_group = QButtonGroup(self)
        exclusive_butn_group.addButton(beer)
        exclusive_butn_group.addButton(juice)
        exclusive_butn_group.addButton(coffee)
        exclusive_butn_group.setExclusive(True)

        drink_layout = QVBoxLayout()
        drink_layout.addWidget(beer)
        drink_layout.addWidget(juice)
        drink_layout.addWidget(coffee)
        drinks.setLayout(drink_layout)
        
        # Radio buttons: answers
        answers = QGroupBox("Choose An Answer")

        answer_a = QRadioButton("A")
        answer_b = QRadioButton("B")
        answer_c = QRadioButton("C")
        answer_d = QRadioButton("D")
        answer_a.setChecked(True) # checked by default

        answer_layout = QVBoxLayout()
        answer_layout.addWidget(answer_a)
        answer_layout.addWidget(answer_b)
        answer_layout.addWidget(answer_c)
        answer_layout.addWidget(answer_d)
        answers.setLayout(answer_layout)

        master_layout = QHBoxLayout()
        master_layout.addWidget(os)
        master_layout.addWidget(drinks)
        master_layout.addWidget(answers)


        self.setLayout(master_layout)

    def windows_box_toggled(self, checked):
        if (checked):
            print("Windows box checked")
        else:
            print("Windows box unchecked")

    def linux_box_toggled(self, checked):
        if (checked):
            print("linux box checked")
        else:
            print("linux box unchecked")

    def mac_box_toggled(self, checked):
        if (checked):
            print("Mac box checked")
        else:
            print("Mac box unchecked")