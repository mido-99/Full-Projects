from PyQt6 import QtGui, QtWidgets, QtCore
from PyQt6.uic import loadUi

#*1
class CustomWdiget(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()
        
        # Text layout which has 2 labels in this example
        self.textQVBoxLayout = QtWidgets.QVBoxLayout()
        self.textUplabel = QtWidgets.QLabel()
        self.textDownlabel = QtWidgets.QLabel()
        self.textQVBoxLayout.addWidget(self.textUplabel)
        self.textQVBoxLayout.addWidget(self.textDownlabel)
        
        # Bigger layout with icon to the right, labels to the left
        self.allQBoxLayout = QtWidgets.QHBoxLayout()
        self.Qiconlabel = QtWidgets.QLabel()
        self.allQBoxLayout.addWidget(self.Qiconlabel, 0)
        self.allQBoxLayout.addLayout(self.textQVBoxLayout, 1)
        self.setLayout(self.allQBoxLayout)
        
    # methods for entering data
    def setTextUp(self, text):
        self.textUplabel.setText(text)
        
    def setTextDown(self, text):
        self.textDownlabel.setText(text)
    
    def setIcon(self, icon):
        self.Qiconlabel.setPixmap(QtGui.QPixmap(icon))


#*2 Step 2
class MainApp(QtWidgets.QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        # Loading ui
        loadUi('main.ui', self)
        
        # Create a QlistWidget object
        self.myQlistWidget = QtWidgets.QListWidget()
        # Filling the list
        for index, name, pic in [
            ('NO.1', 'Name 1', 'pic.jpeg'),
            ('NO.2', 'Name 2', 'pic.jpeg'),
            ('NO.3', 'Name 3', 'pic.jpeg')
        ]:
            # Create a custom widget instance and fill it with values
            myCustom = CustomWdiget()
            myCustom.setTextUp(index)
            myCustom.setTextDown(name)
            myCustom.setIcon(pic)
            
            # Set the custom widget as a QlistWidgetItem 
            myQlistItem = QtWidgets.QListWidgetItem(self.listWidget)
            myQlistItem.setSizeHint(QtCore.QSize(300, 140))
            self.listWidget.setItemWidget(myQlistItem, myCustom)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    widget = MainApp()
    widget.show()
    app.exec()


"""
** Create a custom widgets steps **

#* Create a Custom widget class inherting from QtWidgets.QWidget
This widget will be like the blueprint of how each widget item will look like, 
so construct it using layouts like: QVBoxLayout, QHBoxLayout, to contain smaller widgets

- At the end of this class, use self.setlayout(self.allLayout) where all is the bigger
layout that contain all the items

- In this class also; define any input/output methods that are used to enter or get data
from widgets inside these list items.

#*2 Create The main app widget and Load already-made ui
In this step we have some consideration:
- loadui(uiPath): it's different from self.setupUi(self) that you can modify the ui; so
we can add our customs and still get the existing ui in other parts
- Next we create an instance of QlistWidget that will be populated with our custom widgets
(which are still list items in this case).
- For lists' nature of being iterable, we can do a for loop to populate the list. 

That's what I did here and inside each loop I did the following:
:: Create a custom widget instance (the widget we've built its class)
:: Setting empty widgets in the list using its instance methods
:: Create an instance of QlistWidgetItem(#!parent=self.<list name in ui>)
:: Set size for the list using setSizeHint()
(Either with w & h, or with CustomWidget.setSizeHint())
# Next are still inside loop, Add listitem into listWidget:
:: self.QlistWidget.setItemWidget(QlistwidgetItem, CustomWidget)

NOTE when we create an instance of QlistWidgetItem -in red line- and specify its parent 
in its constructor, we don't need to use this line:
:: self.listWidget.addItem(myQlistItem)
Otherwise, we have to use it to add the new QlistWidgetItem.

- The last line is the MOST IMPORTANT line in fact, in which we set the QlistWidgetItem
to our custom widget.

"""