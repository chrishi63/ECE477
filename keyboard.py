#!usr/bin/python
import sys

import PyQt5
from PyQt5.QtWidgets import *
from functools import partial

import keyboard_auto as keyboardUi

class Keyboard(QMainWindow, keyboardUi.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.stringToEnter = ''
        self.parent = 0
        self.enter.clicked.connect(self.fillInParentLineEdit)
        self.aKey.clicked.connect(partial(self.appendLetter,'a'))
        self.bKey.clicked.connect(partial(self.appendLetter,'b'))
        self.cKey.clicked.connect(partial(self.appendLetter,'c'))
        self.dKey.clicked.connect(partial(self.appendLetter,'d'))
        self.eKey.clicked.connect(partial(self.appendLetter,'e'))
        self.fKey.clicked.connect(partial(self.appendLetter,'f'))
        self.gKey.clicked.connect(partial(self.appendLetter,'g'))
        self.hKey.clicked.connect(partial(self.appendLetter,'h'))
        self.iKey.clicked.connect(partial(self.appendLetter,'i'))
        self.jKey.clicked.connect(partial(self.appendLetter,'j'))
        self.kKey.clicked.connect(partial(self.appendLetter,'k'))
        self.lKey.clicked.connect(partial(self.appendLetter,'l'))
        self.mKey.clicked.connect(partial(self.appendLetter,'m'))
        self.nKey.clicked.connect(partial(self.appendLetter,'n'))
        self.oKey.clicked.connect(partial(self.appendLetter,'o'))
        self.pKey.clicked.connect(partial(self.appendLetter,'p'))
        self.qKey.clicked.connect(partial(self.appendLetter,'q'))
        self.rKey.clicked.connect(partial(self.appendLetter,'r'))
        self.sKey.clicked.connect(partial(self.appendLetter,'s'))
        self.tKey.clicked.connect(partial(self.appendLetter,'t'))
        self.uKey.clicked.connect(partial(self.appendLetter,'u'))
        self.vKey.clicked.connect(partial(self.appendLetter,'v'))
        self.wKey.clicked.connect(partial(self.appendLetter,'w'))
        self.xKey.clicked.connect(partial(self.appendLetter,'x'))
        self.yKey.clicked.connect(partial(self.appendLetter,'y'))
        self.zKey.clicked.connect(partial(self.appendLetter,'z'))
        self._0Key.clicked.connect(partial(self.appendLetter,'0'))
        self.Key1.clicked.connect(partial(self.appendLetter,'1'))
        self.Key2.clicked.connect(partial(self.appendLetter,'2'))
        self.Key3.clicked.connect(partial(self.appendLetter,'3'))
        self.Key4.clicked.connect(partial(self.appendLetter,'4'))
        self.Key5.clicked.connect(partial(self.appendLetter,'5'))
        self.Key6.clicked.connect(partial(self.appendLetter,'6'))
        self.Key7.clicked.connect(partial(self.appendLetter,'7'))
        self.Key8.clicked.connect(partial(self.appendLetter,'8'))
        self.Key9.clicked.connect(partial(self.appendLetter,'9'))
        self.backspace.clicked.connect(self.deleteLetter)
        
        
    def fillInParentLineEdit(self):
        print("Enter clicked")
        self.hide()
        print(self.stringToEnter)
        self.parent.setText(self.stringToEnter)
    def appendLetter(self,letter):
        if self.caps.isChecked():
            self.stringToEnter = self.stringToEnter + letter.capitalize()
        else:
            self.stringToEnter = self.stringToEnter + letter
        self.lineEdit.setText(self.stringToEnter)
    def deleteLetter(self):
        self.stringToEnter = self.stringToEnter[:-1]
        self.lineEdit.setText(self.stringToEnter)
            
def main():
    app = QApplication(sys.argv)
    form = Keyboard()
    form.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
