import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a QLabel widget
        self.label = QLabel("Right-click me", self)
        self.label.setGeometry(50, 50, 200, 30)

        # Define actions for the label's context menu
        action1 = QAction("Action 1", self)
        action2 = QAction("Action 2", self)

        # Connect actions to functions
        action1.triggered.connect(self.action1_triggered)
        action2.triggered.connect(self.action2_triggered)

        # Add actions directly to the label
        self.label.addAction(action1)
        self.label.addAction(action2)

        # Set the context menu policy for the label to show actions as context menu
        self.label.setContextMenuPolicy(Qt.ContextMenuPolicy.ActionsContextMenu)  # ContextMenuPolicy.ActionsContextMenu

    def action1_triggered(self):
        print("Action 1 triggered")

    def action2_triggered(self):
        print("Action 2 triggered")

def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
