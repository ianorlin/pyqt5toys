#!/usr/bin/env python3

#Copyright 2015 Brendan Perrine

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys


class Window(QWidget):
     def __init__(self):
          QWidget.__init__(self)
        
          layout=QGridLayout()
          self.setLayout(layout)

          progressbar=QProgressBar()
          progressbar.setMinimum(-10)
          progressbar.setValue(45)
        
          progressbar.setTextVisible(True)
          layout.addWidget(progressbar)

app=QApplication( sys.argv)
screen=Window()
screen.show()

sys.exit(app.exec())
