from PyQt6 import QtWidgets
from PyQt6.uic.load_ui import loadUiType
import sys


Form_class, _ = loadUiType('main.ui')   # Load the ui file in dir


# class FieldBox(QtWidgets)

class MainApp(QtWidgets.QMainWindow, Form_class):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)      #* Run the layout defined in .ui file
        
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