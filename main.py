import sys
from ui_file import Ui_MainWindow
from random import choice
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor


SIZE = [i for i in range(250)]
COLOR = [i for i in range(256)]


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        qp.setBrush(QColor(choice(COLOR), choice(COLOR), choice(COLOR)))
        q = choice(SIZE)
        qp.drawEllipse(q, choice(SIZE), q, q)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.setFixedSize(500, 450)
    ex.show()
    sys.exit(app.exec_())