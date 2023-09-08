from PyQt6 import QtWidgets


class CustomListItem(QtWidgets.QWidget):
    """Custom List item for entering html tags data for Scraping"""
    
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
        
        self.setPlaceHolder_tag_elem('tag element')
        self.setPlaceHolder_elem_attr('attribute')
        self.setPlaceHolder_attr_vlaue('value')
        self.setPlaceHolder_column('column name')
        
        self.setLayout(self.allQBoxLayout)
        
    def setPlaceHolder_tag_elem(self, text):
        self.tag_element.setPlaceholderText(text)
    
    def setPlaceHolder_elem_attr(self, text):
        self.elem_attr.setPlaceholderText(text)

    def setPlaceHolder_attr_vlaue(self, text):
        self.attr_value.setPlaceholderText(text)

    def setPlaceHolder_column(self, text):
        self.column_name.setPlaceholderText(text)
