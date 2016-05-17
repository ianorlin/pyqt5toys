#!/usr/bin/env python3


from PyQt5.QtCore  import * 
from PyQt5.QtWidgets import *
import sys 


class Window (QWidget):
    def __init__(self): 
        super(Window, self).__init__()
        QWidget.__init__(self)

        self.setWindowTitle("Goodbye")


        layout=QGridLayout()
        self.setLayout(layout)


        label=QLabel("Goodbye Creul World")
        layout.addWidget(label,0,0)

        label.setWordWrap(True)   
        label= QLabel(" This is  a reference to pink floyd I am not suicidial. " )
        layout.addWidget(label,1,0)


app= QApplication(sys.argv)

screen=Window()
screen.show()
    
sys.exit(app.exec())

