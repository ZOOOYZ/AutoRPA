from PyQt5 import QtWidgets, QtCore
import sys
from Core.App import App

if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    mainWin = App()
    mainWin.show()
    sys.exit(app.exec_())

