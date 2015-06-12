#!/usr/bin/env python3

#COpyright 2015 Brendan Perrine

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys 


class Window (QWidget):
     def __init__(self):
        super(Window, self).__init__()
         
        layout =QGridLayout()
        self.setLayout(layout)

          
     menubar=QMenuBar()   
     layout.addWidget(menubar, 0,0)

     actionFile=menubar.addMenu("File")
app = QApplication(sys.argv)

screen = Window()
screen.show()

sys.exit(app.exec_())

