# 29/07/2025
from PySide6.QtWidgets import QTabWidget, QWidget, QLabel, QLineEdit, QHBoxLayout, QPushButton, QVBoxLayout

class QtabWidget_Demo(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QTab Widget Demo")

        tab_widget = QTabWidget(self)

        # Information tab
        widget_form = QWidget()
        lbl_full_name = QLabel("Full name : ")
        full_name_input = QLineEdit()
        
        form_layout = QHBoxLayout()
        form_layout.addWidget(lbl_full_name)
        form_layout.addWidget(full_name_input)
        widget_form.setLayout(form_layout)

        # Buttons tab
        widget_btn = QWidget()
        btn_one = QPushButton("One")
        btn_two = QPushButton("Two")
        btn_three = QPushButton("Three")
        btn_one.clicked.connect(self.btn_1_clicked)

        btn_layout = QVBoxLayout()
        btn_layout.addWidget(btn_one)
        btn_layout.addWidget(btn_two)
        btn_layout.addWidget(btn_three)
        widget_btn.setLayout(btn_layout)

        # Add tabs
        tab_widget.addTab(widget_form, "Information")
        tab_widget.addTab(widget_btn, "Buttons")

        v_layout = QVBoxLayout()
        v_layout.addWidget(tab_widget)

        self.setLayout(v_layout)

    def btn_1_clicked(self):
        pass
