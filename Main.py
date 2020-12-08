# This Python file uses the following encoding: utf-8
import sys
from PyQt5.QtWidgets import QApplication, QWidget


class main(QWidget):
    def __init__(self):
        QWidget.__init__(self)


if __name__ == "__main__":
    app = QApplication([])
    window = main()
    window.show()
    sys.exit(app.exec_())
