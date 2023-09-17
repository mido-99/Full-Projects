from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLineEdit, QPushButton, QListWidgetItem
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt, QSize
from globals import Sub_Role


class CustomListItem(QWidget):
    """Custom List item for entering html tags data for Scraping"""
    
    def __init__(self):
        super().__init__()
        
        self.allQBoxLayout = QHBoxLayout()
        self.setLayout(self.allQBoxLayout)
        
        self.Create_widgets()
        self.Context_Menu()
        

    def Create_widgets(self):
        """Create children widgets of the list items"""
        
        # Main Scraping fields
        self.tag_element = QLineEdit()
        self.elem_attr = QLineEdit()
        self.attr_value = QLineEdit()
        self.column_name = QLineEdit()

        # Delete button
        self.delete_btn = QPushButton('X', self)
        self.delete_btn.clicked.connect(self.delete_self)
        self.delete_btn.setFixedSize(20, 20)
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
    
    
    ## ContextMenu methods ##
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
        write_py_action.triggered.connect(self.write_py_code)
        delete_item.triggered.connect(self.delete_self)
        
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)
    
    def add_alt(self):
        """Add an alternate scraping data to be used if the main failed"""
        
        index = self.get_current_item_and_index()[1]    # get index of current item
        
        sub_item = SubListItem()
        list_item = QListWidgetItem()   #*2
        self.list_widget.insertItem(index + 1, list_item)
        list_item.setData(Sub_Role, True)

        list_item.setSizeHint(QSize(400, 40))
        self.list_widget.setItemWidget(list_item, sub_item)    
    
    def replace_txt(self):
        pass
    
    def write_py_code(self):
        pass


class SubListItem(CustomListItem):
    """Alternate data scraping Class. Same like its parent with removal of uselesses"""

    def __init__(self):
        super().__init__()
        
        self.setStyleSheet('''QLineEdit {background-color: #D3D3D3}''')

    def Context_Menu(self):
        """Same as its parent with add_sub removed. of course we don't need unlimited
        subs right? """

        # ContextMenu Actions
        replace_txt_action = QAction("replace text", self)
        write_py_action = QAction("write python code", self)
        delete_item = QAction("delete", self)
        
        self.addAction(replace_txt_action)
        self.addAction(write_py_action)
        self.addAction(delete_item)
        
        replace_txt_action.triggered.connect(self.replace_txt)
        write_py_action.triggered.connect(self.write_py_code)
        delete_item.triggered.connect(self.delete_self)
        
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)


"""
#*: Getting current item and index:
I couldn't find a straightforword method to locate current item on which a button is
clicked (may be another item is selected, and actually this is a custom widget (QWidget)
not a QlistItem so either reasons it won't work)
So in this methhod I'm iterating through these custom widgets, converting them into 
list items, and checking whether they're the current object (self). if so.. so be it.

#*2:
NOTE In this line I'm not specifying the parent list_widget class in the same line, 
as this automatically adds the new list_item into the list bottom. So I use insertItem
in the next line where I can insert it just below the right-clicked item.


"""