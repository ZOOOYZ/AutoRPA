from UI.MainWindow import *
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtCore import QStringListModel
import os
from Core.ConfigOperate.CreateWindow import CreateWindow
from Core.ConfigOperate.ConfigCreate import ConfigCreate
from Core.ConfigOperate.ConfigTableWindow import ConfigTableWindow
from Core.Action.Executor import Executor
from Core.ConfigOperate.ConfigRead import ConfigRead


class App(QMainWindow, Ui_MainWindow):
    Dir = []
    Selected = 'null'
    NewConfigName = ''

    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        self.setupUi(self)
        self.readConfigList()
        self.listView.clicked.connect(self.selectConfig)
        self.pushButton.clicked.connect(self.startExecute)
        self.pushButton_2.clicked.connect(self.createConfig)
        # self.pushButton_3.clicked.connect(self.loadConfig)
        self.pushButton_4.clicked.connect(self.modifyConfig)
        self.pushButton_5.clicked.connect(self.deleteConfig)

    def startExecute(self):
        if self.Selected == 'null':
            QMessageBox.information(self,'提示','未选择文件！')
        else:
            self.p = os.getcwd()+r'\Config''\\'+self.Selected
            Executor(ConfigRead(self.p).saveConfigAsArray())

    def readConfigList(self):
        self.Dir = os.listdir(os.getcwd() + '/Config')
        slm = QStringListModel(self.Dir)
        self.listView.setModel(slm)

    def loadConfig(self):
        if self.Selected == 'null':
            QMessageBox.information(self, '警告', '未选择配置文件！')
        else:
            QMessageBox.information(self, '提示', '已加载\n' + self.Selected)

    def createConfig(self):
        self.Dialog = CreateWindow()
        self.Dialog.show()
        self.Dialog.Signal.connect(self.Refresh)

    def selectConfig(self, QModelIndex):
        self.Selected = self.Dir[QModelIndex.row()]

    def Refresh(self, name):
        ConfigCreate(name)
        self.readConfigList()

    def modifyConfig(self):
        if self.Selected == 'null':
            QMessageBox.information(self, '提示', '未选择文件！')
        else:
            self.table = ConfigTableWindow(os.getcwd() + '/Config/' + self.Selected)
            self.table.show()

    def deleteConfig(self):
        if self.Selected == 'null':
            QMessageBox.information(self, '提示', '未选择文件！')
        else:
            r = QMessageBox.question(self, '提示', '是否删除配置文件:\n' + self.Selected, QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
            if r == QMessageBox.Yes:
                os.remove(os.getcwd() + '/Config/' + self.Selected)
                self.readConfigList()
            else:
                self.readConfigList()
