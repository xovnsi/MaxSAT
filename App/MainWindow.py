import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QCheckBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Slot

from SatSolver.MainSolver import MainSolver


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.window = QWidget()
        self.result = None
        self.window.submitButton = QPushButton()
        self.window.paid = QCheckBox()
        self.city = None

        self.loader = QUiLoader()
        self.window = self.loader.load("InputWindow.ui", self)

        self.window.submitButton.clicked.connect(self.submit_push)
        self.window.cracow.clicked.connect(self.choose_city)
        self.window.warsaw.clicked.connect(self.choose_city)
        self.window.breslau.clicked.connect(self.choose_city)
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
        best_lots = MainSolver.run(self.city, area, paid, guarded, pr, underground, free_lots, disabled)
        self.result = ResultWindow()
        self.result.fill_data(best_lots)
        self.result.show()
        self.close()

    @Slot()
    def choose_city(self):
        self.city = self.sender().text()
        self.window.city.setText(str(self.city))
        areas = MainSolver.get_num_of_areas(self.city)
        self.window.label.setText(f"Preferred area number (from 1 to {areas})")

        self.window.area.setEnabled(True)
        self.window.paid.setEnabled(True)
        self.window.disabled.setEnabled(True)
        self.window.underground.setEnabled(True)
        self.window.pr.setEnabled(True)
        self.window.guarded.setEnabled(True)
        self.window.freeLots.setEnabled(True)


class ResultWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.loader = QUiLoader()
        # self.main = MainWindow()
        self.window = self.loader.load("ResultWindow.ui", self)
        self.show()

    def fill_data(self, best_lots):
        parking_id = best_lots[0][0]
        parking = best_lots[0][1]
        score = best_lots[0][2]

        self.window.id.setText(str(parking_id))
        self.window.area.setText(str(parking.area_num))
        self.window.score.setText(str(score))
        self.window.paid.setChecked(bool(parking.paid))
        self.window.guarded.setChecked(bool(parking.guarded))
        self.window.pr.setChecked(bool(parking.p_and_r))
        self.window.underground.setChecked(bool(parking.underground))
        self.window.disabled.setChecked(bool(parking.disabled))
        self.window.lots.setText(str(parking.free_lots))

        parking_id = best_lots[1][0]
        parking = best_lots[1][1]
        score = best_lots[1][2]

        self.window.id_2.setText(str(parking_id))
        self.window.area_2.setText(str(parking.area_num))
        self.window.score_2.setText(str(score))
        self.window.paid_2.setChecked(bool(parking.paid))
        self.window.guarded_2.setChecked(bool(parking.guarded))
        self.window.pr_2.setChecked(bool(parking.p_and_r))
        self.window.underground_2.setChecked(bool(parking.underground))
        self.window.disabled_2.setChecked(bool(parking.disabled))
        self.window.lots_2.setText(str(parking.free_lots))

        parking_id = best_lots[2][0]
        parking = best_lots[2][1]
        score = best_lots[2][2]

        self.window.id_3.setText(str(parking_id))
        self.window.area_3.setText(str(parking.area_num))
        self.window.score_3.setText(str(score))
        self.window.paid_3.setChecked(bool(parking.paid))
        self.window.guarded_3.setChecked(bool(parking.guarded))
        self.window.pr_3.setChecked(bool(parking.p_and_r))
        self.window.underground_3.setChecked(bool(parking.underground))
        self.window.disabled_3.setChecked(bool(parking.disabled))
        self.window.lots_3.setText(str(parking.free_lots))




if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec())

# loader = QUiLoader()
#
# window = loader.load("InputWindow.ui", None)
# window.show()
# app.exec()
