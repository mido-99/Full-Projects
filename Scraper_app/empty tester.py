from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QSize
from PyQt6 import QtWidgets
# from PyQt6.uic.load_ui import loadUiType
from PyQt6.uic import loadUi
from Custom_Widgets import CustomListItem


start_url = ''      # Start URL for scraping
data_list = []      # Final list of tags to be scraped

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
        self.pushButton_3.clicked.connect(self.get_url)
        
        
    def add_field(self):
        """Add a new field to the list when user clicks add"""

        myCustom = CustomListItem()
        
        myQlistItem = QtWidgets.QListWidgetItem(self.listWidget)
        myQlistItem.setSizeHint(QSize(400, 50))
        self.listWidget.setItemWidget(myQlistItem, myCustom)
        
    def get_user_input(self):
        """Retrieve data from QlineEdit widgets in a custom Listitem Widget"""
                
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
    
    def get_url(self):
        start_url = self.lineEdit.text()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    widget = MainApp()
    widget.show()
    app.exec()


"""
#* This line works like the opposite side of the coin for setItemWidget(QlistItem, custom).
the latter is used to change a normal item into a custom widget, while the former is used 
to transform an item to the custom one, so we can access its methods and attributs.
"""