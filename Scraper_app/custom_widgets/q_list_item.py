from PyQt6.QtWidgets import (QWidget, QHBoxLayout, QLineEdit, QPushButton, 
QListWidgetItem, QVBoxLayout)
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt, QSize
from .q_dialog import CustomDialog
from globals import Sub_Role, Main_Role

CLOSE_ICON = 'icons/close.jpeg'
SETTING_ICON = 'icons/icons8-3-dots-50 (1).png'  #"https://icons8.com/icon/36944/ellipsis"


class CustomListItem(QWidget):
    """Custom List item for entering html tags data for Scraping"""
    
    def __init__(self):
        super().__init__()
        
        self.regex_tuple = None  #Tuple of regex pattern to be used
        
        self.Create_widgets()
        self.Context_Menu()
        

    def Create_widgets(self):
        """Create children widgets of the list items"""
        
        self.allLayout = QHBoxLayout()
        self.setLayout(self.allLayout)
        
        self.text_layout = QHBoxLayout()
        self.btns_layout = QVBoxLayout()
        self.btns_layout.setSpacing(1)
        
        self.allLayout.addLayout(self.text_layout)
        self.allLayout.addLayout(self.btns_layout)
        
        # Main Scraping fields
        self.tag_element = QLineEdit()
        self.elem_attr = QLineEdit()
        self.attr_value = QLineEdit()
        self.column_name = QLineEdit()

        # Delete Button
        self.delete_btn = QPushButton()
        self.delete_btn.clicked.connect(self.delete_self)
        self.delete_btn.setIcon(QIcon(CLOSE_ICON))
        self.delete_btn.setStyleSheet('border-radius: 5; ')
        
        # Setting Button 
        # self.setting_btn = QPushButton()
        # self.setting_btn.clicked.connect(self.Context_Menu)
        # self.setting_btn.setIcon(QIcon(SETTING_ICON))
        # self.setting_btn.setStyleSheet('border-radius: 5; ')
        #! Deprecated till I find a use
        
        # Add elements to widget layout
        self.text_layout.addWidget(self.tag_element)
        self.text_layout.addWidget(self.elem_attr)
        self.text_layout.addWidget(self.attr_value)
        self.text_layout.addWidget(self.column_name)
        
        # self.btns_layout.addWidget(self.setting_btn)
        self.btns_layout.addWidget(self.delete_btn)
        
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
        """Returns the current (QListItem) widget instance and its row number"""
        
        self.list_widget = self.parent().parent()
        
        for i in range(self.list_widget.count()):
            item = self.list_widget.item(i)
            if self.list_widget.itemWidget(item) == self:
                return item, i
        return None
    
    def delete_self(self):
        curr_item, index = self.get_current_item_and_index()
        next_item = self.list_widget.item(index + 1) if index + 1 < self.list_widget.count() else None

        if next_item and curr_item.data(Main_Role) and next_item.data(Sub_Role):
            for _ in range(2):
                self.list_widget.takeItem(index)
        else:
            self.list_widget.takeItem(index)


    
    
    ## ContextMenu methods ##
    def Context_Menu(self):
        
        # ContextMenu Actions
        add_alt_action = QAction("add sub", self)
        apply_regex_action = QAction("apply regex", self)
        write_py_action = QAction("write python code", self)
        delete_item = QAction("delete", self)
        
        self.addAction(add_alt_action)
        self.addAction(apply_regex_action)
        self.addAction(write_py_action)
        self.addAction(delete_item)
        
        add_alt_action.triggered.connect(self.add_alt)
        apply_regex_action.triggered.connect(self.apply_regex)
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

        list_item.setSizeHint(QSize(400, 50))
        self.list_widget.setItemWidget(list_item, sub_item)    
    
    def apply_regex(self):
        """Apply regex to replace text in the scraped data"""
        
        custom_dialog = CustomDialog()
        
        if self.regex_tuple is not None:      # if user entered some text already; fill inputs
            custom_dialog.set_input(*self.regex_tuple)
        
        result = custom_dialog.exec()
        
        if result == custom_dialog.DialogCode.Accepted:     # if Ok clicked
            self.regex_tuple = custom_dialog.get_input()
    
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
        apply_regex_action = QAction("apply RegEx", self)
        write_py_action = QAction("write python code", self)
        delete_item = QAction("delete", self)
        
        self.addAction(apply_regex_action)
        self.addAction(write_py_action)
        self.addAction(delete_item)
        
        apply_regex_action.triggered.connect(self.apply_regex)
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