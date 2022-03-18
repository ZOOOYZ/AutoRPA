import os.path
from PyQt5.QtWidgets import QDialog, QMessageBox, QComboBox, QItemDelegate
from UI.ConfigTable import *
from PyQt5.QtGui import QStandardItemModel
import xml.dom.minidom


class ComboxDelegate(QItemDelegate):
    def __init__(self, parent=None):
        QItemDelegate.__init__(self, parent)

    def createEditor(self, parent, option, index):
        combo = QComboBox(parent)
        ActionSet = ['鼠标指向', '鼠标点击', '键盘输入', '按键', '循环', '循环结束']
        combo.addItems(ActionSet)
        return combo


class ConfigTableWindow(QDialog):

    def __init__(self, path):
        QDialog.__init__(self)
        self.sm = None
        self.tablewindow = Ui_Form()  # 子窗口的实例化
        self.tablewindow.setupUi(self)
        self.InitTable(path)
        self.tablewindow.pushButton.clicked.connect(self.Rewrite)
        self.tablewindow.pushButton_2.clicked.connect(self.Delete)
        self.tablewindow.pushButton_3.clicked.connect(self.Insert)
        self.ActionSum = 0
        self.path = path

    def InitTable(self, p):
        self.path = p
        doc = xml.dom.minidom.parse(self.path)
        root = doc.documentElement
        self.ActionSum = root.attributes.items()[0][1]
        self.tablewindow.lineEdit.setText(os.path.basename(self.path))
        self.sm = QStandardItemModel()


        # 设置数据头栏名称
        self.sm.setHorizontalHeaderItem(0, QtGui.QStandardItem("类型"))
        self.sm.setHorizontalHeaderItem(1, QtGui.QStandardItem("实现方式"))
        self.sm.setHorizontalHeaderItem(2, QtGui.QStandardItem("延时"))

        for i in range(0, int(self.ActionSum)):
            self.sm.setItem(i, 0, QtGui.QStandardItem(root.getElementsByTagName('类型')[i].childNodes[0].data))
            self.sm.setItem(i, 1, QtGui.QStandardItem(root.getElementsByTagName('实现方法')[i].childNodes[0].data))
            self.sm.setItem(i, 2, QtGui.QStandardItem(root.getElementsByTagName('延时')[i].childNodes[0].data))

        # 按照编号排序
        # self.sm.sort(1, QtCore.Qt.DescendingOrder)

        # 将数据模型绑定到QTableView
        self.tablewindow.tableView.setModel(self.sm)
        self.tablewindow.tableView.setItemDelegateForColumn(0, ComboxDelegate(self.tablewindow.tableView))
        self.tablewindow.tableView.horizontalHeader().setStretchLastSection(True)

    def Rewrite(self):
        # print(self.tablewindow.tableView.model().rowCount(), self.ActionSum)
        NewDoc = xml.dom.minidom.Document()
        root = NewDoc.createElement('流程集')
        # 设置根节点的属性
        root.setAttribute('动作总数', str(self.tablewindow.tableView.model().rowCount()))
        # 将根节点添加到文档对象中
        NewDoc.appendChild(root)
        for i in range(0, self.tablewindow.tableView.model().rowCount()):
            nodeAction = NewDoc.createElement('动作')

            nodeNum = NewDoc.createElement('序号')
            nodeNum.appendChild(NewDoc.createTextNode(str(i + 1)))

            nodeType = NewDoc.createElement('类型')
            # 给叶子节点name设置一个文本节点，用于显示文本内容
            nodeType.appendChild(NewDoc.createTextNode(self.tablewindow.tableView.model().index(i, 0).data()))

            nodeMethod = NewDoc.createElement('实现方法')
            nodeMethod.appendChild(NewDoc.createTextNode(self.tablewindow.tableView.model().index(i, 1).data()))

            nodeTime = NewDoc.createElement('延时')
            nodeTime.appendChild(NewDoc.createTextNode(self.tablewindow.tableView.model().index(i, 2).data()))

            nodeAction.appendChild(nodeNum)
            nodeAction.appendChild(nodeType)
            nodeAction.appendChild(nodeMethod)
            nodeAction.appendChild(nodeTime)
            root.appendChild(nodeAction)

        savename = self.path
        fp = open(savename, 'w', encoding='utf-8')
        NewDoc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")
        QMessageBox.information(self, '提示', '保存成功！')

    def Insert(self):
        self.sm.appendRow([
            QtGui.QStandardItem('无'),
            QtGui.QStandardItem('无'),
            QtGui.QStandardItem('0')
        ])
        self.tablewindow.tableView.setModel(self.sm)
        print("insert")

    def Delete(self):
        self.sm.removeRow(self.tablewindow.tableView.currentIndex().row())
        print("delete")
