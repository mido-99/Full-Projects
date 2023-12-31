from PyQt6.QtGui import QIcon, QMovie
from PyQt6.QtCore import QSize, QThread
from PyQt6.QtWidgets import (QMainWindow, QApplication, QListWidgetItem, QFileDialog,
QMessageBox)
from PyQt6.uic import loadUi
from custom_widgets.q_list_item import CustomListItem
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from globals import Main_Role, Sub_Role

APP_ICON = 'icons/scraper.png'
LOADING_ICON = 'icons/Spinner-1s-200px (1).gif'
settings = get_project_settings()


class MainApp(QMainWindow):
    
    def __init__(self):
        super().__init__()
        loadUi('main.ui', self)
        
        self.save_path = None
        
        self.handle_ui()
        self.handle_buttons()
        
    # Main 2 App Methods
    def handle_ui(self):
        self.setWindowTitle('Scraper')
        self.setWindowIcon(QIcon(APP_ICON))
        self.add_loading_gif()
    
    def handle_buttons(self):
        self.pushButton_2.clicked.connect(self.add_field)
        self.pushButton.clicked.connect(self.get_save_path)
        self.pushButton_3.clicked.connect(self.start_crawling)  #*2
        self.pushButton_4.clicked.connect(self.dummy_method)
    
    
    def add_loading_gif(self):
        self.load_gif = QMovie(LOADING_ICON)
        self.label_4.setMovie(self.load_gif)
        self.label_4.setScaledContents(True)
    
    def gif_loading(self):
        '''start loading animation as scrping starts'''

        self.label_4.setVisible(True)
        self.load_gif.start()
    
    def gif_stop(self):
        '''stops loading animation when scraping finishes'''
        
        self.label_4.setVisible(False)    
        self.load_gif.stop()

    def add_field(self):
        """Add a new field to the list when user clicks add"""

        myCustomListItem = CustomListItem()
        list_widget = QListWidgetItem(self.listWidget)
        list_widget.setData(Main_Role, True)
        
        list_widget.setSizeHint(QSize(400, 60))
        self.listWidget.setItemWidget(list_widget, myCustomListItem)
    
    # These setters and getters are used to retrieve data in spider file from current 
    # running app instance
    
    # Input 
    def set_url(self):
        """Fetch start url"""
        
        self.url = self.lineEdit.text().strip()
        return self.url
    
    def set_parent(self):
        """Parent element attributes"""
        
        self.parent_tag = self.lineEdit_2.text().strip()
        self.parent_attr = self.lineEdit_3.text().strip()
        self.parent_attr_value = self.lineEdit_4.text().strip().replace(' ', '.')
        
        return all((self.parent_tag, self.parent_attr, self.parent_attr_value))

    def item_generator(self):
        '''Generates the CustomListItem object and corresponding listWidgetItem
        in the same row'''

        for i in range(self.listWidget.count()):
            item = self.listWidget.item(i)
            custom = self.listWidget.itemWidget(item) #*5
            yield custom, item

    def get_user_input(self):
        """Retrieve data from QlineEdit widgets in a custom Listitem Widget"""
        
        self.data_list = []
        for custom, item in self.item_generator():
            # check if listItem is main or sub
            if item.data(Main_Role):
                item_type = 'main'
            elif item.data(Sub_Role):
                item_type = 'sub'
            
            # Getting info from lineEdits
            data = custom.retrieve_fields()
            data["type"] = item_type
            
            self.data_list.append(data)
    
    def get_output_format(self):
        '''Get curent selected output format'''
        return self.comboBox.currentText()
    
    def get_save_path(self):
        """Get file save location and extension"""
        
        self.file_format = self.get_output_format()
        self.save_path, _ = QFileDialog.getSaveFileName(self, 
            'Save to', 
            f'Output.{self.file_format}', 
            f"{self.file_format} files (*.{self.file_format});;"
            )
        return self.save_path
    
    def set_output_file(self, settings):
        """Pass final file and format to settings file"""

        settings.set('FEED_FORMAT', f"{self.file_format}")
        settings.set('FEED_URI', f'{self.save_path}')
    
    def get_data(self):
        """Retrieve all collected data into spider file"""

        return (self.url, self.data_list, self.parent_tag, self.parent_attr, 
                self.parent_attr_value)

    # Validate before proceeding to crawling
    def validate_input(self):
        """Validate user input fields before starting spider to raise related error
        messageBox or warning"""
        
        if not self.set_url():
            QMessageBox.critical(self, 
                'Empty URL!', 'Please Provide a URL')
        elif not self.set_parent():
            QMessageBox.critical(self, 
                'Empty Field!', 'Please Fill parent element data')
        else:
            return True

#TODO Validate each field in customItem, may be done inside get_user_input
    def validate_field(self):
        pass
    
    def validate_save_file(self):
        """Ensure user has entered save file name"""

        return True if self.save_path else bool(self.get_save_path())

    def start_crawling(self):
        """Method chain activator"""
        
        if self.validate_input() and self.validate_save_file():
            self.get_user_input()            
            self.set_output_file(settings)
            self.gif_loading()
            
            process = CrawlerProcess(settings) #*4
            process.crawl('scraper_app')
            process.start()
            self.gif_stop()
            
            self.data_list.clear()
        
    def dummy_method(self):
        if self.load_gif.state() == QMovie.MovieState.NotRunning:
            self.label_4.setVisible(True)
            self.load_gif.start()
        elif self.load_gif.state() == QMovie.MovieState.Running:
            print('Running')
            self.load_gif.stop()
            self.label_4.setVisible(False)
            

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

#*5 .self Importance
Unless self here, the thread will be destroyed before it finishes its work (treated as
garbage). so self must be used

"""