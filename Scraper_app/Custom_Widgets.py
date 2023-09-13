from PyQt6 import QtWidgets


class CustomListItem(QtWidgets.QWidget):
    """Custom List item for entering html tags data for Scraping"""
    
    def __init__(self):
        super().__init__()
        
        self.allQBoxLayout = QtWidgets.QHBoxLayout()
        self.setLayout(self.allQBoxLayout)
        
        self.tag_element = QtWidgets.QLineEdit()
        self.elem_attr = QtWidgets.QLineEdit()
        self.attr_value = QtWidgets.QLineEdit()
        self.column_name = QtWidgets.QLineEdit()
        self.delete_btn = QtWidgets.QPushButton('X', self)
        self.delete_btn.clicked.connect(self.delete_self)
        self.delete_btn.setFixedSize(25, 25)
        self.delete_btn.setStyleSheet('background-color: red; color: white; border:none; '
                                    'border-radius: 10; font-style: bold'
                                    )
        
        self.allQBoxLayout.addWidget(self.tag_element)
        self.allQBoxLayout.addWidget(self.elem_attr)
        self.allQBoxLayout.addWidget(self.attr_value)
        self.allQBoxLayout.addWidget(self.column_name)
        self.allQBoxLayout.addWidget(self.delete_btn)
        
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


"""
#*: Getting current item and index:
I couldn't find a straightforword method to locate current item on which a button is
clicked (may be another item is selected, and actually this is a custom widget (QWidget)
not a QlistItem so either reasons it won't work)
So in this methhod I'm iterating through these custom widgets, converting them into 
list items, and checking whether they're the current object (self). if so.. so be it.

"""