#!/usr/bin/env python3


from PyQt5.QtCore  import * 
from PyQt5.QtWidgets import *
import sys 


class Window (QWidget):
    def __init__(self): 
        super(Window, self).__init__()
        QWidget.__init__(self)



        layout=QGridLayout()
        self.setLayout(layout)


        label=QLabel(" All your screen, Are belong to us.")
        layout.addWidget(label,0,0)



app= QApplication(sys.argv)

screen=Window()
screen.show()
screen.showFullScreen()   
sys.exit(app.exec())

