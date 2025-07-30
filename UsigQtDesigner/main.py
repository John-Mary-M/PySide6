from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

loader = QUiLoader()    # set up loader object

app = QApplication([])
window = loader.load('widget.ui', None) # Loading the ui - happens at run time


# accessing the fields in the form
def do_something():
    print(f"{window.full_name_line_edit.text()} is a {window.occupation_line_edit.text()}")

# Changing fields in the form
window.setWindowTitle("User Data")

# Accessing widgets in the form
window.submit_btn.clicked.connect(do_something)

window.show()
app.exec()