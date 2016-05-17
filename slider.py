#!/usr/bin/env python3

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout=QGridLayout()
        self.setLayout(layout)

        slider= QSlider(Qt.Horizontal)
        slider.setValue(42)
        layout.addWidget(slider, 0,0 )

        slider2= QSlider(Qt.Horizontal)
        slider2.setValue(15)
        layout.addWidget(slider2, 1,0)
          
app= QApplication (sys.argv)

screen = Window()
screen.show()

sys.exit(app.exec_())
