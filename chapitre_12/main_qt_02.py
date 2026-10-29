from pprint import pprint
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

from main_window import Ui_MainWindow


class MainWindowApp(Ui_MainWindow, QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.click)

    def click(self):
        print('click')


def main():

    app = QApplication([])

    window = MainWindowApp()
    window.show()

    app.exec()


if __name__ == '__main__':
    main()
