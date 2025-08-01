from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_custom_mainwindow import Ui_MainWindow

class TextEditor_App(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super().__init__()

        self.setupUi(self)
        self.app = app
        self.setWindowTitle("Text Editor")

        self.actionQuit.triggered.connect(self.quit)
        self.actionCopy.triggered.connect(self.copy)
        self.actioncut.triggered.connect(self.cut)
        self.actionpaste.triggered.connect(self.paste)
        self.actionRedo.triggered.connect(self.redo)
        self.actionUndo.triggered.connect(self.undo)
        self.actionAbout.triggered.connect(self.about)
        self.actionAbout_Qt.triggered.connect(self.about_Qt)

    def quit (self):
        self.app.quit()

    def copy (self):
        self.inpu_textEdit.copy()

    def cut (self):
        self.inpu_textEdit.cut()

    def paste (self):
        self.inpu_textEdit.paste()

    def undo (self):
        self.inpu_textEdit.undo()

    def redo (self):
        self.inpu_textEdit.redo()

    def about(self):
        QMessageBox.information(self,"Going Pro!", "QMainWindow, QtDesigner and resources")

    def about_Qt(self):
        QApplication.aboutQt()