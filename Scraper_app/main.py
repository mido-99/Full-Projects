from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import (QMainWindow, QApplication, QListWidget, QListWidgetItem, 
QMessageBox, QFileDialog)
# from PyQt6.uic.load_ui import loadUiType
from PyQt6.uic import loadUi
from Custom_Widgets import CustomListItem
# from pathlib import Path
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


class MainApp(QMainWindow):
    
    def __init__(self):
        super().__init__()
        loadUi('main.ui', self)
        
        self.handle_ui()
        self.handle_buttons()
        
    def handle_ui(self):
        self.setWindowTitle('Scraper')
        self.setWindowIcon(QIcon('scraper.png'))
    
    def handle_buttons(self):
        self.pushButton_2.clicked.connect(self.add_field)
        self.pushButton.clicked.connect(self.get_save_path)
        self.pushButton_3.clicked.connect(self.start_crawling)  #*2
        
        
    def add_field(self):
        """Add a new field to the list when user clicks add"""

        myCustomListItem = CustomListItem()
        
        myQlistItem = QListWidgetItem(self.listWidget)
        myQlistItem.setSizeHint(QSize(400, 50))
        self.listWidget.setItemWidget(myQlistItem, myCustomListItem)
    
    # These setters and getters are used to retrieve data in spider file from current 
    # running app instance
    def set_url(self):
        """Fetch start url"""
        
        self.url = self.lineEdit.text().strip()
    
    def set_parent(self):
        """Parent element attributes"""
        
        self.parent_tag = self.lineEdit_2.text().strip()
        self.parent_attr = self.lineEdit_3.text().strip()
        self.parent_attr_value = self.lineEdit_4.text().strip().replace(' ', '.')
        
    def get_user_input(self):
        """Retrieve data from QlineEdit widgets in a custom Listitem Widget"""
        
        self.data_list = []
        for i in range(self.listWidget.count()):
            item = self.listWidget.item(i)
            custom = self.listWidget.itemWidget(item) #*
            
            tag_elem = custom.tag_element.text().strip()
            elem_attr = custom.elem_attr.text().strip()
            attr_value = custom.attr_value.text().strip().replace(' ', '.')
            column_name = custom.column_name.text().strip()
            
            data = {
            "tag": tag_elem,
            "elem_attr": elem_attr,
            "attr_value": attr_value,
            "column": column_name
            }
            self.data_list.append(data)
    
    def get_save_path(self):
        """Get file save location and type"""
        
        self.save_path, _ = QFileDialog.getSaveFileName(self, 'Save to', 'Data.jsonl', 
            "jsonl files (*.jsonl);; json files (*.json);; csv files (*.csv)")
        return self.save_path
    
    def get_data(self):
        """Retrieve all collected data into spider file"""

        return (self.url, self.data_list, self.parent_tag, self.parent_attr, 
                self.parent_attr_value)

    def start_crawling(self):
        """Method chain activator"""
        
        if self.get_save_path():
            self.set_url()
            self.set_parent()
            self.get_user_input()
            
            process = CrawlerProcess(get_project_settings()) #*4
            process.crawl('scraper_app')
            QApplication.processEvents()
            process.start()
            
            self.data_list.clear()


import globals
if __name__ == '__main__':
    app = QApplication([])
    widget = MainApp()
    globals.main_app_instance = widget  #*3
    widget.show()
    app.exec()


"""
#* This line works like the opposite side of the coin for setItemWidget(QlistItem, custom).
the latter is used to change a normal item into a custom widget, while the former is used 
to transform an item to the custom one, so we can access its methods and attributs.


#*2 Breakdown of what is going on when the button is clicked:
First of all DATA collection; this happens in set_url(), get_user_input(), and 
get_save_path() To assign the values of self.url, self.data_list and save respectively.

Our goal is to pass these data to our spider, but we can't jsut make a global variables
with their names cause they will be imported empty at the beginning of the script, and 
any reassinging to their values to update it will cause the imported vars not to reflect
these changes.
(Maybe it can work with lists since they're immutable and imports just refer to them in
memory, but still will cause problems when reassigning and won't work with strings at all)

So the idea was to def getters and setters to set their values, and retrieve them later
from the curent running instance of the MainApp in spider file.
But How to refer to the currently running instance? we don't instantiate it manually, 
it's instantiated when the app runs. Here comes point 3.


#*3 Reference to the current App instance
To be able to do it, I created a new file (globals) with just a dull empty var.
its value is assigned in main file exactly after creating an instance of MainApp, Then 
in the spider, I import the var from (globals). Since this instance reflects the curent
running MainApp; I can use its getter to retrieve the data in spider. And That's All


#*4 Running Spider from another script in same project
As mentioned before, in this project I have some imoprts from main file in spider file,
so I can't make the opposite -to refer to the Spider class- so to avoid circular imports.

Here comes the use of CrawlProcess(get_project_settings()), To run the spider.
process.crawl() usually takes a class as argument, and since I can't import the class;
I'm using the other way of writing its name as a string.
Last line of process.start() To start the crawling process.


"""