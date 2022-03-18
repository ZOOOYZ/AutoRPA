import os

from PyQt5.QtWidgets import QDialog, QMessageBox
from UI.CreateConfig import *
from Core.ConfigOperate.ConfigTableWindow import ConfigTableWindow


class CreateWindow(QDialog):
    Signal = QtCore.pyqtSignal(str)

    def __init__(self):
        QDialog.__init__(self)
        self.child = Ui_Dialog()  # 子窗口的实例化
        self.child.setupUi(self)
        self.child.pushButton.clicked.connect(self.confirmClicked)
        self.child.pushButton_2.clicked.connect(self.cancelClicked)

    def confirmClicked(self):
        if self.child.lineEdit.text() != '':
            self.Signal.emit(self.child.lineEdit.text())
            self.close()
            self.table = ConfigTableWindow(os.getcwd()+'/Config/'+self.child.lineEdit.text()+'.xml')
            self.table.show()
        else:
            QMessageBox.information(self, '提示', '请输入流程名！')

    def cancelClicked(self):
        self.close()
