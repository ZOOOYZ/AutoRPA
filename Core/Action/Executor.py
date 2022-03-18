import time
import pyautogui
import os


class Executor():
    def __init__(self, name):
        self.Execu(name)

    def Execu(self, doc):
        # print(doc)
        for i in range(0, len(doc.index)):
            if doc['type'].loc[i] == '鼠标指向':
                # print(doc['method'].loc[i])
                locate = pyautogui.locateCenterOnScreen(os.getcwd() + r'\Image''\\' + doc['method'].loc[i], confidence=0.8)
                pyautogui.moveTo(locate)
                print(locate)
            elif doc['type'].loc[i] == '鼠标点击':
                pyautogui.click(clicks=int(doc['method'].loc[i]))
            elif doc['type'].loc[i] == '按键':
                print(doc['method'].loc[i])
                pyautogui.press(doc['method'].loc[i])
            elif doc['type'].loc[i] == '键盘输入':
                fre = list(doc['method'].loc[i])
                pyautogui.press(fre, interval=0.1)
            elif doc['type'].loc[i] == '循环':
                ForStart = i + 1
                ForCount = int(doc['method'].loc[i])
            elif doc['type'].loc[i] == '循环结束':
                ForEnd = i
                self.ForDoc = doc.iloc[ForStart:ForEnd]
                self.ForDoc.reset_index(drop=True, inplace=True)
                for i1 in range(0, ForCount-1):
                    Executor(self.ForDoc)
            time.sleep(int(doc['delay'].loc[i]))



