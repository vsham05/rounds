import sys

from random import randrange 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from UI import Ui_Form
from PyQt5.QtGui import QPainter, QColor

class Rounds(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)        
        self.clck = False
        self.summon_round_btn.clicked.connect(self.change_clc)
    
    def change_clc(self):
        self.clck = True
        self.repaint()

    def paintEvent(self, event):
        if self.clck:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def draw_flag(self, qp):
        for i in range(randrange(5, 15)):
            qp.setBrush(QColor(randrange(0, 255), randrange(0, 255), randrange(0, 255)))
            size = randrange(50, 150)
            coord1 = randrange(0, 300)
            coord2 = randrange(0, 300)
            qp.drawEllipse(coord1, coord2, size, size)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    round_ex = Rounds() 
    round_ex.show()
    sys.exit(app.exec())