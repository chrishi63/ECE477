#!usr/bin/python
import sys

import PyQt5
from PyQt5.QtWidgets import *

import keyboard_auto as keyboardUi

class Keyboard(QMainWindow, keyboardUi.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
            
def main():
    app = QApplication(sys.argv)
    form = Keyboard()
    form.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
