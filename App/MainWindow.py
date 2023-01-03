import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QCheckBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Slot

from SatSolver.Features import MainSolver


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.window = QWidget()
        self.window.submitButton = QPushButton()
        self.window.paid = QCheckBox()

        self.loader = QUiLoader()
        self.window = self.loader.load("InputWindow.ui", self)

        self.window.submitButton.clicked.connect(self.submit_push)
        self.window.paid.isChecked()

        self.show()


    @Slot()
    def submit_push(self):
        area = int(self.window.area.text())
        paid = self.window.paid.isChecked()
        disabled = self.window.disabled.isChecked()
        underground = self.window.underground.isChecked()
        pr = self.window.pr.isChecked()
        guarded = self.window.guarded.isChecked()
        free_lots = self.window.freeLots.isChecked()
        MainSolver.run(area, paid, guarded, pr, underground, free_lots, disabled)
        self.window = QWidget()
        self.window = self.loader.load("ResultWindow.ui", self)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec())

# loader = QUiLoader()
#
# window = loader.load("InputWindow.ui", None)
# window.show()
# app.exec()
