from PyQt6.QtWidgets import (QLineEdit, QPushButton, QDialog, QVBoxLayout, QLabel)

class CustomDialog(QDialog):
    """Dialog to obtain data on the run from user"""

    def __init__(self):
        super().__init__()
        
        self.create_layout()
        self.connect_buttons()
        

    def create_layout(self):
        
        self.layout = QVBoxLayout()
        
        self.label_1 = QLabel("Pattern:")
        self.line_edit_1 = QLineEdit(self)
        self.label_2 = QLabel("Replace with:")
        self.line_edit_2 = QLineEdit(self)
        self.submit_btn = QPushButton('Ok', self)
        self.cancel_btn = QPushButton('Cancel', self)
        
        self.layout.addWidget(self.label_1)
        self.layout.addWidget(self.line_edit_1)
        self.layout.addWidget(self.label_2)
        self.layout.addWidget(self.line_edit_2)
        self.layout.addWidget(self.submit_btn)
        self.layout.addWidget(self.cancel_btn)
        
        self.setLayout(self.layout)
    
    def connect_buttons(self):

        self.submit_btn.clicked.connect(self.accept)
        self.cancel_btn.clicked.connect(self.close)
    
    def get_input(self):
        
        if self.line_edit_1.text() == '' and  self.line_edit_2.text() == '':  
            return None
        else:
            return self.line_edit_1.text(), self.line_edit_2.text()
        
    
    def set_input(self, text_1, text_2):
        """fill the dialog line eidts with pre-added values if exists"""
        
        self.line_edit_1.setText(text_1)
        self.line_edit_2.setText(text_2)
