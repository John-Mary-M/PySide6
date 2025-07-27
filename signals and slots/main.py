# Version 1: responding to the button click
"""
from PySide6.QtWidgets import QApplication, QPushButton

# the slot: responds when somethin happens
def button_clicked():
    print("You clicked the button, didn't you!")

app  =QApplication()

button = QPushButton("Click me")
button.clicked.connect(button_clicked)

button.show()
app.exec()
"""

#Version 2: Signals sending values capture values in slots
"""
from PySide6.QtWidgets import QApplication, QPushButton

# The slot : responds when something happens (responds to a signal/ event)
def button_clicked(data):
    if data:
        data = "On"
    else: 
        data = "Off"
    print("You clicked the button, didn't you!", data)

app = QApplication()
button = QPushButton("Click me")
button.setCheckable(True)   # Makes the button checkable. It's unchecked by default
                            # further clicks toggles between checked and unchecked states
button.clicked.connect(button_clicked)

button.show()
app.exec()

"""

# Version 3: Slider
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QSlider

# Slot: Responds when something happens
def respond_to_slider(data):
    print(f"Slider moved to : {data}dB")

app = QApplication()
slider = QSlider(Qt.Vertical)
slider.setMinimum(-6)
slider.setMaximum(6)
slider.setValue(0)
# do the connection
slider.valueChanged.connect(respond_to_slider)
slider.show()
app.exec()