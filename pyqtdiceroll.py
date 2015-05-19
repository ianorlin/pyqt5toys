#!/usr/bin/env python3!

from PyQt5.QtWidgets import *
import random
import sys 

random.seed()


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout=QGridLayout()
        self.setLayout(layout)
        # add all of the classic dice from dnd for d4 d6 d8 d10 d20 and percentile
        button = QPushButton("d20")
        button.clicked.connect(self.roll_d20)
        layout.addWidget( button,0,4)
        
        button =QPushButton("d6")
        button.clicked.connect (self.roll_d6)
        layout.addWidget(button,0,1)

        button=QPushButton("d4")
        button.clicked.connect (self.roll_d4)
        layout.addWidget( button,0,0)

        button=QPushButton("d8")
        button.clicked.connect (self.roll_d8)
        layout.addWidget( button,0,2)
   
        button=QPushButton("d10")
        button.clicked.connect (self.roll_d10)
        layout.addWidget (button,0,3 )
    #should add a GUI print function to add text to the rolls as a tally. 
    def roll_d20(self, button):
            print( random.randint(1,20))
    def roll_d6 (self, button):
           print( random.randint(1,6))
    def roll_d4 (self, button):
           print(random.randint(1,4))
    def roll_d8 (self, button):
           print (random.randint(1,8))
    def roll_d10 (self, button):
           print( random.randint(1,10))
app=QApplication (sys.argv)

screen=Window()
screen.show()

sys.exit(app.exec_())
