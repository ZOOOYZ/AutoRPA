import time
import pyautogui
import os
from PyQt5.QtCore import pyqtSignal, QThread
import threading


class Executor(QThread):
    LogText = pyqtSignal(str)

    def __init__(self, name):
        super(Executor, self).__init__()
        self.d = name

    def run(self):
        # print('线程1')
        self.Execu(self.d)

    def Execu(self, doc):
        # print(doc)
        self.LogText.emit('***********开始执行*************')
        for i in range(0, len(doc.index)):
            if doc['type'].loc[i] == '鼠标指向':
                # print(doc['method'].loc[i])
                self.LogText.emit('执行动作：'+doc['type'].loc[i])
                locate = pyautogui.locateCenterOnScreen(os.getcwd() + r'\Image''\\' + doc['method'].loc[i],
                                                        confidence=0.8)
                pyautogui.moveTo(locate)
                # print(locate)
            elif doc['type'].loc[i] == '鼠标点击':
                self.LogText.emit('执行动作：'+doc['type'].loc[i])
                pyautogui.click(clicks=int(doc['method'].loc[i]))
            elif doc['type'].loc[i] == '按键':
                self.LogText.emit('执行动作：'+doc['type'].loc[i])
                # print(doc['method'].loc[i])
                pyautogui.press(doc['method'].loc[i])
            elif doc['type'].loc[i] == '键盘输入':
                self.LogText.emit('执行动作：'+doc['type'].loc[i])
                fre = list(doc['method'].loc[i])
                pyautogui.press(fre, interval=0.1)
            elif doc['type'].loc[i] == '循环':
                self.LogText.emit('执行动作：'+doc['type'].loc[i])
                ForStart = i + 1
                ForCount = int(doc['method'].loc[i])
            elif doc['type'].loc[i] == '循环结束':
                self.LogText.emit('执行动作：'+doc['type'].loc[i])
                ForEnd = i
                self.ForDoc = doc.iloc[ForStart:ForEnd]
                self.ForDoc.reset_index(drop=True, inplace=True)
                for i1 in range(0, ForCount - 1):
                    Executor(self.ForDoc)
            time.sleep(int(doc['delay'].loc[i]))
            self.LogText.emit('延时：'+doc['delay'].loc[i])
        self.LogText.emit('***********执行完毕*************')
