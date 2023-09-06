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


class MainApp(QtWidgets.QMainWindow):
    
    def __init__(self):
        super().__init__()
        loadUi('main.ui', self)
        
        self.handle_ui()
        self.handle_buttons()
        
        
    def handle_ui(self):
        self.myQlistWidget = QtWidgets.QListWidget()
    
    def handle_buttons(self):
        self.pushButton_2.clicked.connect(self.add_field)
        self.pushButton_3.clicked.connect(self.get_data)
        
        
    def add_field(self):
        """Add a new field to the list when user clicks add"""

        myCustom = CustomWdiget()
        myCustom.setPlaceHolder_tag_elem('tag element')
        myCustom.setPlaceHolder_elem_attr('attribute')
        myCustom.setPlaceHolder_attr_vlaue('value')
        myCustom.setPlaceHolder_column('column name')
        
        myQlistItem = QtWidgets.QListWidgetItem(self.listWidget)
        myQlistItem.setSizeHint(QSize(400, 50))
        self.listWidget.setItemWidget(myQlistItem, myCustom)
        
    def get_data(self):
        data_list = []
        
        for i in range(self.listWidget.count()):
            item = self.listWidget.item(i)
            custom = self.listWidget.itemWidget(item) #*
            
            tag_elem = custom.tag_element.text()
            elem_attr = custom.elem_attr.text()
            attr_value = custom.attr_value.text()
            column_name = custom.column_name.text()

            data = {
            "Tag Element": tag_elem,
            "Element Attribute": elem_attr,
            "Attribute Value": attr_value,
            "Column Name": column_name
            }
            data_list.append(data)
        
        return data_list


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    widget = MainApp()
    widget.show()
    app.exec()


"""
#* This line works like the opposite side of the coin for setItemWidget(); the latter is
used to change a normal item into a custom widget, while the former is the opposite.
"""