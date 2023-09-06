from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QSize
from PyQt6 import QtWidgets
# from PyQt6.uic.load_ui import loadUiType
from PyQt6.uic import loadUi
import sys


# Form_class, _ = loadUiType('main.ui')   # Load the ui file in dir

class CustomWdiget(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.allQBoxLayout = QtWidgets.QHBoxLayout()
        
        self.tag_element = QtWidgets.QLineEdit()
        self.elem_attr = QtWidgets.QComboBox()
        self.attr_value = QtWidgets.QLineEdit()
        self.column_name = QtWidgets.QLineEdit()
        self.allQBoxLayout.addWidget(self.tag_element)
        self.allQBoxLayout.addWidget(self.elem_attr)
        self.allQBoxLayout.addWidget(self.attr_value)
        self.allQBoxLayout.addWidget(self.column_name)
        
        self.setLayout(self.allQBoxLayout)
        
    def setPlaceHolder_tag_elem(self, text):
        self.tag_element.setPlaceholderText(text)
    
    def setComboItems(self, items):
        self.elem_attr.addItems(items)

    def setPlaceHolder_attr_vlaue(self, text):
        self.attr_value.setPlaceholderText(text)

    def setPlaceHolder_column(self, text):
        self.column_name.setPlaceholderText(text)


class MainApp(QtWidgets.QMainWindow):
    
    def __init__(self):
        super().__init__()
        loadUi('main.ui', self)
        
        self.myQlistWidget = QtWidgets.QListWidget()
        for index, name, pic in [
            ('NO.1', 'Name 1', 'pic.jpeg'),
            ('NO.2', 'Name 2', 'pic.jpeg'),
            ('NO.3', 'Name 3', 'pic.jpeg')
        ]:
            myCustom = CustomWdiget()
            myCustom.setPlaceHolder_tag_elem(index)
            myCustom.setPlaceHolder_attr_vlaue(name)
            myCustom.setPlaceHolder_column(pic)
            myCustom.setComboItems(('class', 'name', 'id'))
            
            myQlistItem = QtWidgets.QListWidgetItem(self.listWidget)
            myQlistItem.setSizeHint(QSize(400, 50))
            self.listWidget.setItemWidget(myQlistItem, myCustom)    

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    widget = MainApp()
    widget.show()
    app.exec()
    