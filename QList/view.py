from PySide6.QtWidgets import QWidget, QListWidget, QPushButton, QLineEdit, QVBoxLayout, QAbstractItemView

class QlistDemo(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QList Widget Demo")

        self.list_widget = QListWidget(self)
        self.list_widget.setSelectionMode(QAbstractItemView.MultiSelection) # allowing selection of multiple items

        self.list_widget.addItem("One") # adding items one by one
        self.list_widget.addItems(["Two", "Three"]) # adding multiple items
        self.list_widget.currentItemChanged.connect(self.current_item_changed)
        self.list_widget.currentTextChanged.connect(self.current_text_changed)

        add_item_btn = QPushButton("Add Item")
        add_item_btn.clicked.connect(self.add_item)

        delete_item_btn = QPushButton("Delete Item")
        delete_item_btn.clicked.connect(self.delete_item)
        
        count_item_btn = QPushButton("Count Item")
        count_item_btn.clicked.connect(self.item_count)

        selected_items_btn = QPushButton("Selected Items")
        selected_items_btn.clicked.connect(self.selected_items)

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.list_widget)
        v_layout.addWidget(add_item_btn)
        v_layout.addWidget(delete_item_btn)
        v_layout.addWidget(count_item_btn)
        v_layout.addWidget(selected_items_btn)

        self.setLayout(v_layout)


    def current_item_changed(self, item):
        pass

    def current_text_changed(self, text):
        pass

    def add_item(self):
        self.list_widget.addItem("New Item")

    def delete_item(self, item):
        self.list_widget.takeItem(self.list_widget.currentRow())
    
    def item_count(self):
        print(f"Item Count : {self.list_widget.count()}")
    
    def selected_items(self):
        list = self.list_widget.selectedItems()
        for i in list:
            print(i.text())

    