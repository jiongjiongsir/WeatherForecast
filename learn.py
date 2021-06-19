'''
setAlignment():设置文本的对齐方式
setIndent(): 设置文本缩进
text(): 获取文本内容
setBuddy(): 设置伙伴关系
setText():设置文本内容
selectText():返回所选择的字符
setWordWrap():设置是否允许换行
QLabel常用的信号（事件）：
1.当鼠标滑过QLabel控件时触发：linkHovered
2.当鼠标单击QLabel控件时触发：linkActivated
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPalette, QPixmap
from PyQt5.QtCore import Qt


class QLabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建label
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        nameLable=QLabel('城市名称',self)
        nameLineEdit=QLineEdit(self)
        nameLineEdit.setFixedSize(200,30)
        self.submitBtn=QPushButton('Submit')
        self.submitBtn.setFixedSize(50,50)
        label1.setText("这是一串文本")
        label1.setAutoFillBackground(True)  # 背景自动填充
        # palette = QPalette()  # 填充
        # palette.setColor(QPalette.Window, Qt.blue)  # 设置label背景颜色
        # label1.setPalette(palette)  # 调试板
        label1.setAlignment(Qt.AlignCenter)  # 设置文字的对齐方式，文本居中对齐

        label2.setText("<a href= '#'>欢迎使用Python （label2）</a>")
        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip("这是一个图片标签（label2）")
        label3.setPixmap(QPixmap("./images/4.jpg"))
        # label4，要么触发单击事件，要么链接，只能二者选其一
        # 如果设为True用浏览器打开网页，如果设为False，调用槽函数
        label4.setOpenExternalLinks(True)
        label4.setText("<a href= 'https://www.baidu.com/'> 感谢使用百度（label4） </a>")
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip("这是一个超级链接")

        # 垂直布局
        vbox = QVBoxLayout()
        vbox.addWidget(nameLable)
        vbox.addWidget(nameLineEdit)
        vbox.addWidget(self.submitBtn)
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        # 将linkHovered信号绑定到self.linkHovered槽函数上
        label2.linkHovered.connect(self.linkHovered)  # 滑过事件

        label4.linkActivated.connect(self.linkClicked)  # 单击事件
        self.setLayout(vbox)  # 设置布局
        self.setWindowTitle("QLabel控件演示")

    def linkHovered(self):
        print("当鼠标滑过label2标签时，触发条件")

    def linkClicked(self):
        print("当鼠标滑过label4标签时，触发条件")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./images/t10.ico'))
    main = QLabelDemo()
    main.show()
    sys.exit(app.exec_())