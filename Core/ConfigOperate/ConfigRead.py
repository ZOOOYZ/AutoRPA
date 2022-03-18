import xml.dom.minidom
import pandas as pd

class ConfigRead:

    ActionSet = pd.DataFrame([['','',0]],columns=['type','method','delay'])

    def __init__(self, path):
        self.doc = xml.dom.minidom.parse(path)
        self.saveConfigAsArray()

    def saveConfigAsArray(self):
        root = self.doc.documentElement
        ActionSum = int(root.attributes.items()[0][1])

        for i in range(0, ActionSum):
            self.ActionSet.loc[i] = [root.getElementsByTagName('类型')[i].childNodes[0].data,
                                                                 root.getElementsByTagName('实现方法')[i].childNodes[0].data,
                                                                 root.getElementsByTagName('延时')[i].childNodes[0].data]

        return self.ActionSet








