from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout

class LabelEdit(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QLabel and QLineEdit")

        label = QLabel("Full Name: ")
        self.line_edit = QLineEdit()
        self.line_edit.textChanged.connect(self.text_changed)
        # self.line_edit.cursorPositionChanged.connect(self.cursor_position_changed)
        # self.line_edit.editingFinished.connect(self.editing_finished)
        # self.line_edit.returnPressed.connect(self.return_pressed)
        # self.line_edit.selectionChanged.connect(self.selection_changed)
        self.line_edit.textEdited.connect(self.text_edited)

        button  = QPushButton("Grab data")
        button.clicked.connect(self.button_clicked)
        self.text_holder_label = QLabel("I AM HERE")

        h_layout =QHBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(self.line_edit)

        v_master_layout = QVBoxLayout()
        v_master_layout.addLayout(h_layout)
        v_master_layout.addWidget(button)
        v_master_layout.addWidget(self.text_holder_label)

        self.setLayout(v_master_layout)

    # slots
    def button_clicked(self):
        # print(f"Full Name : {self.line_edit.text()}")
        self.text_holder_label.setText(self.line_edit.text())

    def text_changed(self):
        self.text_holder_label.setText(self.line_edit.text())
    
    def cursor_position_changed(self, old, new):
        print(f"Old cursor position : {old}, -new position : {new}")

    def editing_finished(self):
        print("editing finished")

    def return_pressed(self):
        print("Return key pressed")

    def selection_changed(self):
        print(f"Selection Changed : {self.line_edit.selectedText()}")

    def text_edited(self, new_text):
        print(f"Text edited. New Text : {new_text}")