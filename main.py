import sys

from random import randrange 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor

class Rounds(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
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
        qp.setBrush(QColor(255, 255, 0))
        for i in range(randrange(5, 15)):
            size = randrange(50, 150)
            coord1 = randrange(0, 300)
            coord2 = randrange(0, 300)
            qp.drawEllipse(coord1, coord2, size, size)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    round_ex = Rounds() 
    round_ex.show()
    sys.exit(app.exec())