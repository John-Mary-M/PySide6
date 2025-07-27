from PySide6.QtWidgets import QTextEdit, QPushButton, QWidget, QHBoxLayout, QVBoxLayout

class Text_Editor(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Text Editor v1")

        self.text_edit = QTextEdit()

        # Buttons
        current_text = QPushButton("Current Text")
        copy_button = QPushButton("Copy")
        cut_button = QPushButton("Cut")
        paste_button = QPushButton("Paste")
        undo_button = QPushButton("Undo")
        redo_button = QPushButton("Redo")
        set_plain_text_button = QPushButton("Set Plain Text")
        set_html_button = QPushButton("set html")
        clear_btn = QPushButton("Clear")

        # Connections
        current_text.clicked.connect(self.current_text_btn_clicked)
        copy_button.clicked.connect(self.text_edit.copy) # Connect directly to QTextEdit slot
        cut_button.clicked.connect(self.text_edit.cut)
        paste_button.clicked.connect(self.paste) # Go through a custom slot
        # paste_button.clicked.connect(self.text_edit.paste) 
        undo_button.clicked.connect(self.text_edit.undo)
        redo_button.clicked.connect(self.text_edit.redo)
        set_html_button.clicked.connect(self.set_html)
        set_plain_text_button.clicked.connect(self.set_plain_text)
        clear_btn.clicked.connect(self.text_edit.clear)

        h_layout = QHBoxLayout()
        h_layout.addWidget(current_text)
        h_layout.addWidget(copy_button)
        h_layout.addWidget(cut_button)
        h_layout.addWidget(paste_button)
        h_layout.addWidget(redo_button)
        h_layout.addWidget(undo_button)
        h_layout.addWidget(set_plain_text_button)
        h_layout.addWidget(set_html_button)
        h_layout.addWidget(clear_btn)
        #
        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.text_edit)

        self.setLayout(v_layout)

    # slots
    def paste (self):
        self.text_edit.paste()

    def current_text_btn_clicked(self) -> None:
        print(f"{self.text_edit.toPlainText()}")

    def set_plain_text(self):
        self.text_edit.setPlainText("Lets see how this works")

    def set_html(self):
        self.text_edit.setHtml("<h1>Kigali District</h1><p>The city of Kigali has 3 districts</p><br><ul><li>Never been</li><li>So i dont know</li></ul>")