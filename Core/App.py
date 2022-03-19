from UI.MainWindow import *
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtCore import QStringListModel
import os
from Core.ConfigOperate.CreateWindow import CreateWindow
from Core.ConfigOperate.ConfigCreate import ConfigCreate
from Core.ConfigOperate.ConfigTableWindow import ConfigTableWindow
from Core.Action.Executor import Executor
from Core.ConfigOperate.ConfigRead import ConfigRead
import pyautogui
import time


class App(QMainWindow, Ui_MainWindow):
    Dir = []
    Selected = 'null'
    NewConfigName = ''
    flag = 0

    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        self.setupUi(self)
        self.readConfigList()
        self.listView.clicked.connect(self.selectConfig)
        self.pushButton.clicked.connect(self.startExecute)
        self.pushButton_2.clicked.connect(self.createConfig)
        self.pushButton_3.clicked.connect(self.Terminate)
        self.pushButton_4.clicked.connect(self.modifyConfig)
        self.pushButton_5.clicked.connect(self.deleteConfig)

    def startExecute(self):
        if self.Selected == 'null':
            QMessageBox.information(self,'提示','未选择文件！')
        else:
            self.p = os.getcwd()+r'\Config''\\'+self.Selected
            self.e = Executor(ConfigRead(self.p).saveConfigAsArray())
            self.e.start()
            self.e.LogText.connect(self.logDisplay)

    # def Execu(self, doc):
    #     # print(doc)
    #     for i in range(0, len(doc.index)):
    #         if self.flag == 1:
    #             return
    #         if doc['type'].loc[i] == '鼠标指向':
    #             # print(doc['method'].loc[i])
    #             self.textBrowser.append('执行动作：' + doc['type'].loc[i])
    #             locate = pyautogui.locateCenterOnScreen(os.getcwd() + r'\Image''\\' + doc['method'].loc[i], confidence=0.8)
    #             pyautogui.moveTo(locate)
    #             print(locate)
    #         elif doc['type'].loc[i] == '鼠标点击':
    #             self.textBrowser.append('执行动作：' + doc['type'].loc[i])
    #             pyautogui.click(clicks=int(doc['method'].loc[i]))
    #         elif doc['type'].loc[i] == '按键':
    #             self.textBrowser.append('执行动作：' + doc['type'].loc[i])
    #             print(doc['method'].loc[i])
    #             pyautogui.press(doc['method'].loc[i])
    #         elif doc['type'].loc[i] == '键盘输入':
    #             self.textBrowser.append('执行动作：' + doc['type'].loc[i])
    #             fre = list(doc['method'].loc[i])
    #             pyautogui.press(fre, interval=0.1)
    #         elif doc['type'].loc[i] == '循环':
    #             self.textBrowser.append('执行动作：' + doc['type'].loc[i])
    #             ForStart = i + 1
    #             ForCount = int(doc['method'].loc[i])
    #         elif doc['type'].loc[i] == '循环结束':
    #             self.textBrowser.append('执行动作：' + doc['type'].loc[i])
    #             ForEnd = i
    #             self.ForDoc = doc.iloc[ForStart:ForEnd]
    #             self.ForDoc.reset_index(drop=True, inplace=True)
    #             for i1 in range(0, ForCount-1):
    #                 if self.flag == 1:
    #                     return
    #                 self.Execu(self.ForDoc)
    #         time.sleep(int(doc['delay'].loc[i]))
    #         self.textBrowser.append('延时：'+doc['delay'].loc[i] + '秒')
    #     self.textBrowser.append('**************执行完毕**************')


    def readConfigList(self):
        self.Dir = os.listdir(os.getcwd() + '/Config')
        slm = QStringListModel(self.Dir)
        self.listView.setModel(slm)

    def Terminate(self):
        self.flag = 1

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

    def logDisplay(self,str):
        self.textBrowser.append(str)

