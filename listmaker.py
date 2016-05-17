#!/usr/bin/env python3
# Copyright 2015 Brendan Perrine 



from PyQt5.QtCore  import * 
from PyQt5.QtWidgets import *
import sys 


class Window (QWidget):
    def __init__(self): 
        super(Window, self).__init__()
        QWidget.__init__(self)

        self.setWindowTitle("PyQt5 list maker")

        index=1      
        layout=QGridLayout()
        self.setLayout(layout)
        
        self.listwidget=QListWidget()
        self.listwidget.addItem( "testing")   
        self.listwidget.addItem( "Hugs")
        self.listwidget.addItem( "It works") 

        layout.addWidget(self.listwidget)


app= QApplication(sys.argv)

screen=Window()
screen.show()
    
sys.exit(app.exec())

