#!usr/bin/python
import sys

import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class ClickableLineEdit(QLineEdit):
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton: self.clicked.emit()
        else: super().mousePressEvent(event)

