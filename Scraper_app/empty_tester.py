from PyQt6.QtWidgets import QInputDialog, QVBoxLayout, QLineEdit, QApplication

class CustomInputDialog(QInputDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setLayout(QVBoxLayout(self))

        self.lineEdit1 = QLineEdit(self)
        self.lineEdit2 = QLineEdit(self)

        self.layout().addWidget(self.lineEdit1)
        self.layout().addWidget(self.lineEdit2)

    def getValues(self):
        return self.lineEdit1.text(), self.lineEdit2.text()


app = QApplication([])
dialog = CustomInputDialog()
result = dialog.exec()

if result == QInputDialog.DialogCode.Accepted:
    print(dialog.getValues())
