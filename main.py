import sys, random
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from ui import Ui_Form


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = False

    def paintEvent(self, event):

        if self.do_paint:
            im = QPainter()
            im.begin(self)
            self.draw_square(im)
            im.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_square(self, im):
        try:
            rad = random.randint(10, 150)
            im.setPen(QColor(random.randint(0, 256), random.randint(0, 256), random.randint(0, 256)))

            im.drawEllipse(20, 20, 2 * rad, 2 * rad)
        except Exception as el:
            print(el)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
