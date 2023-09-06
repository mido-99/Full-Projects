from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QSize
from PyQt6 import QtWidgets
# from PyQt6.uic.load_ui import loadUiType
from PyQt6.uic import loadUi


# Form_class, _ = loadUiType('main.ui')   # Load the ui file in dir

class CustomWdiget(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.allQBoxLayout = QtWidgets.QHBoxLayout()
        
        self.tag_element = QtWidgets.QLineEdit()
        self.elem_attr = QtWidgets.QLineEdit()
        self.attr_value = QtWidgets.QLineEdit()
        self.column_name = QtWidgets.QLineEdit()
        self.allQBoxLayout.addWidget(self.tag_element)
        self.allQBoxLayout.addWidget(self.elem_attr)
        self.allQBoxLayout.addWidget(self.attr_value)
        self.allQBoxLayout.addWidget(self.column_name)
        
        self.setLayout(self.allQBoxLayout)
        
    def setPlaceHolder_tag_elem(self, text):
        self.tag_element.setPlaceholderText(text)
    
    def setPlaceHolder_elem_attr(self, text):
        self.elem_attr.setPlaceholderText(text)

    def setPlaceHolder_attr_vlaue(self, text):
        self.attr_value.setPlaceholderText(text)

    def setPlaceHolder_column(self, text):
        self.column_name.setPlaceholderText(text)


class MainApp(QtWidgets.QMainWindow, Form_class):
    
    def __init__(self):
        super().__init__()
        loadUi('main.ui', self)
        
        self.myQlistWidget = QtWidgets.QListWidget()
        
        self.handle_ui()
        self.handle_buttons()
        
    def handle_ui(self):
        pass
    
    def handle_buttons(self):
        pass
    

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    widget = MainApp()
    widget.show()
    sys.exit(app.exec())