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


# url = ''      # Start URL for scraping
# data_list = []      # Final list of tags to be scraped

class MainApp(QMainWindow):
    
    def __init__(self):
        super().__init__()
        loadUi('main.ui', self)
        
        self.handle_ui()
        self.handle_buttons()
        
    def handle_ui(self):
        self.setWindowTitle('Scraper')
        self.setWindowIcon(QIcon('scraper.png'))
        self.myQlistWidget = QListWidget()
    
    def handle_buttons(self):
        self.pushButton_2.clicked.connect(self.add_field)
        self.pushButton.clicked.connect(self.get_save_path)
        self.pushButton_3.clicked.connect(self.start_crawling)
        
        
    def add_field(self):
        """Add a new field to the list when user clicks add"""

        myCustom = CustomListItem()
        
        myQlistItem = QListWidgetItem(self.listWidget)
        myQlistItem.setSizeHint(QSize(400, 50))
        self.listWidget.setItemWidget(myQlistItem, myCustom)
    
    def set_data(self, data):
        self.data_list = [data]
        
    def get_data(self):
        return self.data_list
        
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
            self.set_data(data)
    
    def get_url(self):
        """Fetch start url"""

        url = self.lineEdit.text()
    
    def get_save_path(self):
        """Get file save location and type"""
        
        save = QFileDialog.getSaveFileName(self, 'Save to', 'Data.jsonl', 
            "jsonl files (*.jsonl);; json files (*.json);; csv files (*.csv)")
    
    def start_crawling(self):
        """Method chain activator"""
        
        self.get_url()
        self.get_save_path()
        self.get_user_input()

        process = CrawlerProcess(get_project_settings())
        process.crawl('scraper_app')
        process.start()
        
        self.data_list.clear()


import globals
if __name__ == '__main__':
    app = QApplication([])
    widget = MainApp()
    globals.main_app_instance = widget
    widget.show()
    app.exec()


"""
#* This line works like the opposite side of the coin for setItemWidget(QlistItem, custom).
the latter is used to change a normal item into a custom widget, while the former is used 
to transform an item to the custom one, so we can access its methods and attributs.
"""