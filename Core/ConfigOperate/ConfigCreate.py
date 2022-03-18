import os
import xml.dom.minidom


class ConfigCreate:
    def __init__(self, Name):
        Num = 1
        doc = xml.dom.minidom.Document()
        # print(Name)
        root = doc.createElement('流程集')
        # 设置根节点的属性
        root.setAttribute('动作总数', str(Num))
        # 将根节点添加到文档对象中
        doc.appendChild(root)

        for i in range(1, Num + 1):
            nodeAction = doc.createElement('动作')

            nodeNum = doc.createElement('序号')
            nodeNum.appendChild(doc.createTextNode(str(i)))

            nodeType = doc.createElement('类型')
            # 给叶子节点name设置一个文本节点，用于显示文本内容
            nodeType.appendChild(doc.createTextNode('无'))

            nodeMethod = doc.createElement('实现方法')
            nodeMethod.appendChild(doc.createTextNode('无'))

            nodeTime = doc.createElement('延时')
            nodeTime.appendChild(doc.createTextNode('0'))

            nodeAction.appendChild(nodeNum)
            nodeAction.appendChild(nodeType)
            nodeAction.appendChild(nodeMethod)
            nodeAction.appendChild(nodeTime)
            root.appendChild(nodeAction)

        savename = os.getcwd() + '/Config/' + Name + '.xml'
        fp = open(savename, 'w', encoding='utf-8')
        doc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")


