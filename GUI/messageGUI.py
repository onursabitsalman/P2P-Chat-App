import socket
from threading import Thread

import time
from PyQt5 import QtCore, QtGui, QtWidgets
import GUI.searchGUI

class Ui_Message(object):
    def __init__(self,ip_address="",user_name="",chat_name=""):

        self.ip_address = ip_address
        print("ip",self.ip_address)
        self.user_name = user_name
        print("add",self.user_name)
        self.chat_name = chat_name
        print("add chat", self.chat_name)

        ths = open(str(self.chat_name), "a")
        ths.write('\n')
        ths.write("-------------------------------------------------------")
        ths.flush()
        ths.close()

        thread_wait = Thread(target=self.listenChat, args=())
        thread_wait.start()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 590)

        self.msgTB = QtWidgets.QTextBrowser(Form)
        self.msgTB.setGeometry(QtCore.QRect(20, 51, 361, 461))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setStrikeOut(False)
        self.msgTB.setFont(font)
        self.msgTB.setObjectName("msgTB")

        self.wn = Form

        self.msgLE = QtWidgets.QLineEdit(Form)
        self.msgLE.setGeometry(QtCore.QRect(20, 530, 281, 31))
        self.msgLE.setObjectName("msgLE")

        self.sendBtn = QtWidgets.QPushButton(Form)
        self.sendBtn.setGeometry(QtCore.QRect(310, 530, 71, 31))
        self.sendBtn.setObjectName("sendBtn")

        #send user's message other user
        self.sendBtn.clicked.connect(self.sendChat)

        self.backBtn = QtWidgets.QPushButton(Form)
        self.backBtn.setGeometry(QtCore.QRect(20, 10, 93, 28))
        self.backBtn.setObjectName("backBtn")

        #close messageGUE with button
        self.backBtn.clicked.connect(self.back_button)

        self.usernameLabel = QtWidgets.QLabel(Form)
        self.usernameLabel.setGeometry(QtCore.QRect(304, 10, 71, 21))
        self.usernameLabel.setObjectName("usernameLabel")
        self.usernameLabel.setText(self.user_name)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.sendBtn.setText(_translate("Form", "SEND"))
        self.backBtn.setText(_translate("Form", "BACK"))
        self.msgTB.setHtml(_translate("Form",
                                      "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                      "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                      "p, li { white-space: pre-wrap; }\n"
                                      "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                      "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

    def back_button(self):
        self.Form = QtWidgets.QWidget()
        self.ui = GUI.searchGUI.Ui_Search()
        self.ui.setupUi(self.Form)
        self.wn.hide()
        self.Form.show()

    #this function listen message and see message
    def listenChat(self):
        while(True):
            host = socket.gethostbyname(socket.gethostname())
            port = 5007

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((host, port))

            s.listen(1)
            conn, address = s.accept()

            data = conn.recv(1024).decode()
            print(data)

            msgData = self.chat_name + " -> " + data

            ths = open(str(self.chat_name), "a")
            ths.write('\n')
            ths.write(str(msgData))
            ths.flush()
            ths.close()

            self.msgTB.append(msgData)

            conn.close()
            time.sleep(1)

    #this function is for send message
    def sendChat(self):

        host = self.ip_address
        port = 5007

        socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socketTCP.connect((host, port))
        message = self.msgLE.text()
        socketTCP.send(message.encode())

        self.msgLE.setText("")

        msgData = self.user_name + " -> " + message

        ths = open(str(self.chat_name), "a")
        ths.write('\n')
        ths.write(str(msgData))
        ths.flush()
        ths.close()

        self.msgTB.append(msgData)

        socketTCP.close()