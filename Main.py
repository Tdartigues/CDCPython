# This Python file uses the following encoding: utf-8
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui.InterfaceInit import InerfaceInit
from Ui.Utils import *

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = InerfaceInit()
ui.setupUi(MainWindow)
ui.BtnConnect()
MainWindow.show()
sys.exit(app.exec_())


