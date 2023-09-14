from PyQt6 import QtWidgets
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt


class CustomListItem(QtWidgets.QWidget):
    """Custom List item for entering html tags data for Scraping"""
    
    def __init__(self):
        super().__init__()
        
        self.allQBoxLayout = QtWidgets.QHBoxLayout()
        self.setLayout(self.allQBoxLayout)
        
        self.Create_widgets()
        self.Context_Menu()
        

    def Create_widgets(self):
        """Create children widgets of the list items"""

        # Main Scraping fields
        self.tag_element = QtWidgets.QLineEdit()
        self.elem_attr = QtWidgets.QLineEdit()
        self.attr_value = QtWidgets.QLineEdit()
        self.column_name = QtWidgets.QLineEdit()

        # Delete button
        self.delete_btn = QtWidgets.QPushButton('X', self)
        self.delete_btn.clicked.connect(self.delete_self)
        self.delete_btn.setFixedSize(25, 25)
        self.delete_btn.setStyleSheet('background-color: red; color: white; border:none; '
                                    'border-radius: 10; font-style: bold'
                                    )
        # Add elements to widget layout
        self.allQBoxLayout.addWidget(self.tag_element)
        self.allQBoxLayout.addWidget(self.elem_attr)
        self.allQBoxLayout.addWidget(self.attr_value)
        self.allQBoxLayout.addWidget(self.column_name)
        self.allQBoxLayout.addWidget(self.delete_btn)
        
        # Setting placeholders
        self.setPlaceHolder_tag_elem('tag element')
        self.setPlaceHolder_elem_attr('attribute')
        self.setPlaceHolder_attr_vlaue('value')
        self.setPlaceHolder_column('column name')
        

    def setPlaceHolder_tag_elem(self, text):
        self.tag_element.setPlaceholderText(text)
    
    def setPlaceHolder_elem_attr(self, text):
        self.elem_attr.setPlaceholderText(text)

    def setPlaceHolder_attr_vlaue(self, text):
        self.attr_value.setPlaceholderText(text)

    def setPlaceHolder_column(self, text):
        self.column_name.setPlaceholderText(text)

        
    def get_current_item_and_index(self):   #*
        self.list_widget = self.parent().parent()
        
        for i in range(self.list_widget.count()):
            item = self.list_widget.item(i)
            if self.list_widget.itemWidget(item) == self:
                return item, i
        return None
    
    def delete_self(self):
        index = self.get_current_item_and_index()[1]
        self.list_widget.takeItem(index)
    
    # ContextMenu methods
    def Context_Menu(self):
        
        # ContextMenu Actions
        add_alt_action = QAction("add sub", self)
        replace_txt_action = QAction("replace text", self)
        write_py_action = QAction("write python code", self)
        delete_item = QAction("delete", self)
        
        self.addAction(add_alt_action)
        self.addAction(replace_txt_action)
        self.addAction(write_py_action)
        self.addAction(delete_item)
        
        add_alt_action.triggered.connect(self.add_alt)
        replace_txt_action.triggered.connect(self.replace_txt)
        add_alt_action.triggered.connect(self.write_py_code)
        delete_item.triggered.connect(self.delete_self)
        
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
    
    def add_alt(self):
        pass
    
    def replace_txt(self):
        pass
    
    def write_py_code(self):
        pass
    


"""
#*: Getting current item and index:
I couldn't find a straightforword method to locate current item on which a button is
clicked (may be another item is selected, and actually this is a custom widget (QWidget)
not a QlistItem so either reasons it won't work)
So in this methhod I'm iterating through these custom widgets, converting them into 
list items, and checking whether they're the current object (self). if so.. so be it.

"""