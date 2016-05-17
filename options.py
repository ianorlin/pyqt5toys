#!/usr/bin/env python3
#copyright 2015 

from PyQt5.QtWidgets import *
import sys

class Dialog(QWidget):
    def __init__(self):
        super(Dialog, self).__init__()

        layout=QGridLayout()
        self.setLayout(layout)

        label=QLabel ("This dialog button will wear out your mouse for no purpose")

        buttonbox=QDialogButtonBox(QDialogButtonBox.Ok|QDialogButtonBox.Cancel)
        layout.addWidget(buttonbox)        

app=QApplication (sys.argv)
screen=Dialog()

screen.show()

sys.exit(app.exec())       
