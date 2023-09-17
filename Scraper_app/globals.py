from PyQt6.QtCore import Qt

# Current running MainApp instance
main_app_instance = None

# Custom ListItem widgets roles
Main_Role = Qt.ItemDataRole.UserRole + 1
Sub_Role = Qt.ItemDataRole.UserRole + 2