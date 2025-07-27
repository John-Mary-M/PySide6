from PySide6.QtWidgets import QMainWindow, QPushButton, QHBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Custom MainWindow")

        # Menubar and menus
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_app)
        #
        edit_menu = menu_bar.addMenu("Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")
        #
        menu_bar.addMenu("Window")
        menu_bar.addMenu("setting")
        menu_bar.addMenu("Help")
        #
        button = QPushButton("Click")
        button.clicked.connect(self.button_clicked)
        button.pressed.connect(self.button_pressed)
        button.released.connect(self.button_released)
        
        # layout
        layout = QHBoxLayout()
        layout.addWidget(button)

        # Create a central widget and set the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def quit_app(self):
        self.app.quit()

    def button_clicked(self):
        print("Button clicked")
        
    def button_pressed(self):
        print("Button pressed")

    def button_released(self):
        print("Button released")