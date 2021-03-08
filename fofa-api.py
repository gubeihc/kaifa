# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(616, 370)
        self.Email_label = QtWidgets.QLabel(Dialog)
        self.Email_label.setGeometry(QtCore.QRect(13, 40, 61, 21))
        self.Email_label.setObjectName("Email_label")
        self.api_key_label = QtWidgets.QLabel(Dialog)
        self.api_key_label.setGeometry(QtCore.QRect(13, 90, 61, 20))
        self.api_key_label.setObjectName("api_key_label")
        self.Email_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.Email_lineEdit.setGeometry(QtCore.QRect(100, 40, 113, 20))
        self.Email_lineEdit.setObjectName("Email_lineEdit")
        self.api_key_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.api_key_lineEdit.setGeometry(QtCore.QRect(100, 90, 113, 20))
        self.api_key_lineEdit.setObjectName("api_key_lineEdit")
        self.search_label = QtWidgets.QLabel(Dialog)
        self.search_label.setGeometry(QtCore.QRect(250, 40, 54, 12))
        self.search_label.setObjectName("search_label")
        self.search_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.search_lineEdit.setGeometry(QtCore.QRect(340, 40, 113, 20))
        self.search_lineEdit.setObjectName("search_lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(500, 40, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(260, 100, 281, 211))
        self.textBrowser.setObjectName("textBrowser")
        ##直接写入 邮箱和api_key
        # 邮箱
        self.Email_lineEdit.setText('123@qq.com')
        # # api-key
        self.api_key_lineEdit.setText('123')
        def get():
            query = self.search_lineEdit.text()
            url = 'https://fofa.so/api/v1/search/all?'
            basekey = str(base64.b64encode(query.encode('utf-8')), 'utf-8')
            params = {'email': self.Email_lineEdit.text(), 'key': self.api_key_lineEdit.text(), 'qbase64': basekey, 'size': 10000}
            html = requests.get(url, params=params)
            data = json.loads(html.text)
            for url in data['results']:
                #给请求的数据发送到文本框
                self.textBrowser.append(url[0])
        #当我们点击按钮就会执行get 函数，
        self.pushButton.clicked.connect(get)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Email_label.setText(_translate("Dialog", "Email"))
        self.api_key_label.setText(_translate("Dialog", "api-key"))
        self.search_label.setText(_translate("Dialog", "查询语句"))
        self.pushButton.setText(_translate("Dialog", "开始搜索"))

if __name__ == '__main__':
    import  sys
    from PyQt5.QtWidgets import QApplication, QMainWindow
    import  base64
    import requests
    import  json
    #创建QApplication类的实例
    app=QApplication(sys.argv)
    #创建一个窗口
    mainwindow=QMainWindow()
    #实例化刚刚拖拽生成的类
    ui=Ui_Dialog()
    # 调用setupUi在指定窗口(主窗口)中添加控件
    ui.setupUi(mainwindow)
    # 显示窗口
    mainwindow.show()
    # 进入程序的主循环，并通过exit函数确保主循环安全结束
    sys.exit(app.exec_())
