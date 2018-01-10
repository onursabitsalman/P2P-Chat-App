import socket
import time
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
import GUI.messageGUI
import GUI.loginGui2
import GUI.messageGUI
import ClientTcp
import ClientUdp
from threading import Thread

class Ui_Search(object):
    def __init__(self,user_name=""):
        self.dmC = ClientUdp.ClientUdp(True)
        self.dmC.start()
        self.isOk = ""

        self.user_name = user_name

        #this tread wait for a connection any user
        thread_wait = Thread(target=self.waitChat, args=())
        thread_wait.start()


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 591)

        self.designedLabel = QtWidgets.QLabel(Form)
        self.designedLabel.setGeometry(QtCore.QRect(210, 560, 176, 17))

        self.wn = Form

        font = QtGui.QFont()

        font.setFamily("MV Boli")
        font.setUnderline(True)

        self.designedLabel.setFont(font)


        self.designedLabel.setObjectName("designedLabel")

        self.usernameLabel = QtWidgets.QLabel(Form)
        self.usernameLabel.setGeometry(QtCore.QRect(310, 10, 71, 21))
        self.usernameLabel.setObjectName("usernameLabel")
        self.usernameLabel.setText(self.user_name)

        self.logoutBtn = QtWidgets.QPushButton(Form)
        self.logoutBtn.setGeometry(QtCore.QRect(40, 480, 321, 41))
        self.logoutBtn.setObjectName("logoutBtn")

        #if user click this button than user log out and close program
        self.logoutBtn.clicked.connect(self.logout_button)

        self.searchLE = QtWidgets.QLineEdit(Form)
        self.searchLE.setGeometry(QtCore.QRect(40, 130, 321, 41))
        self.searchLE.setObjectName("searchLE")

        self.searchLabel = QtWidgets.QLabel(Form)
        self.searchLabel.setGeometry(QtCore.QRect(40, 110, 101, 16))
        self.searchLabel.setObjectName("searchLabel")

        self.searchBtn = QtWidgets.QPushButton(Form)
        self.searchBtn.setGeometry(QtCore.QRect(40, 180, 321, 41))
        self.searchBtn.setObjectName("searchBtn")

        #this button search user for online users then chat with user
        self.searchBtn.clicked.connect(self.search_button)

        self.acceptBtn = QtWidgets.QPushButton(Form)
        self.acceptBtn.setGeometry(QtCore.QRect(40, 380, 151, 28))
        self.acceptBtn.setObjectName("acceptBtn")
        self.acceptBtn.hide()

        #if user want chat click this button
        self.acceptBtn.clicked.connect(self.accept_request)

        self.declineBtn = QtWidgets.QPushButton(Form)
        self.declineBtn.setGeometry(QtCore.QRect(212, 380, 151, 28))
        self.declineBtn.setObjectName("declineBtn")
        self.declineBtn.hide()

        #if user dont want chat click this button
        self.declineBtn.clicked.connect(self.declineRequest)

        self.requestLabel = QtWidgets.QLabel(Form)
        self.requestLabel.setGeometry(QtCore.QRect(40, 339, 191, 31))

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)

        self.requestLabel.setFont(font)
        self.requestLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.requestLabel.setObjectName("requestLabel")
        self.requestLabel.hide()

        self.requestUsername = QtWidgets.QLabel(Form)
        self.requestUsername.setGeometry(QtCore.QRect(230, 340, 131, 31))

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.requestUsername.setFont(font)
        self.requestUsername.setAlignment(QtCore.Qt.AlignCenter)
        self.requestUsername.setObjectName("requestUsername")
        self.requestUsername.hide()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.designedLabel.setText(_translate("Form", "Designed by YUSUF & ONUR"))
        self.logoutBtn.setText(_translate("Form", "LOGOUT"))
        self.searchLabel.setText(_translate("Form", "Username"))
        self.searchBtn.setText(_translate("Form", "SEARCH AND START CHAT"))
        self.acceptBtn.setText(_translate("Form", "ACCEPT"))
        self.declineBtn.setText(_translate("Form", "DECLINE"))
        self.requestLabel.setText(_translate("Form", "Chat Request From:"))
        self.requestUsername.setText(_translate("Form", "Username"))

    #this function close program
    def logout_button(self):
        client = ClientTcp.ClientTcp("4")
        client.start()
        self.dmC.logout = False
        self.wn.close()

    #this function search function
    def search_button(self):
        username = self.searchLE.text()
        client = ClientTcp.ClientTcp("3", str(username))
        client.start()
        client.join()
        address = str(client.feedback)
        print(client.feedback)
        if address != "not sign":

            self.x = False
            time.sleep(1)
            host = str(address)
            port = 5003

            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((host, port))

            message = self.user_name
            print("name ",message)
            client_socket.send(message.encode())

            feedback = client_socket.recv(1024).decode()

            print("burda la " , feedback)

            #if other user accept than open chat gui
            if(feedback == "Ok"):
                self.Form = QtWidgets.QWidget()
                self.ui = GUI.messageGUI.Ui_Message(str(address),str(self.user_name),str(self.searchLE.text()))
                self.ui.setupUi(self.Form)
                self.wn.hide()
                self.Form.show()

    #this function wait than other user
    def waitChat(self):

        self.x = True

        host = socket.gethostbyname(socket.gethostname())
        port = 5003

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            s.bind((host, port))
            s.listen(1)
            conn, address = s.accept()
        except:
            sys.exit(1)



        print("This address want to chat: " + str(address))

        while (self.x):
            if (str(address) != ""):
                self.acceptBtn.show()
                self.declineBtn.show()
                self.requestLabel.show()
                self.requestUsername.show()
                connName = conn.recv(1024).decode()
                if (connName != ""):
                    self.adrr = address
                    self.requestUsername.setText(connName)
                    self.x = False
                    isOkTF = True
                    while(isOkTF):
                        #user send other user ok message and open page
                        if(self.isOk == "Ok"):
                            conn.send("Ok".encode())
                            isOkTF = False
                            self.x = False
                            s.close()
                        #user not accept and go on searchGUI
                        elif (self.isOk == "OkNo"):
                            conn.send("OkNo".encode())
                            isOkTF = False
                            self.x = False
                            s.close()

        s.close()

    #than open messageGUI and talk other user
    def accept_request(self):
        self.isOk = "Ok"
        self.x = True
        self.Form = QtWidgets.QWidget()
        self.adrr = str(self.adrr).split('\'')[1]
        self.ui = GUI.messageGUI.Ui_Message(str(self.adrr),str(self.user_name),str(self.requestUsername.text()))
        self.ui.setupUi(self.Form)
        self.wn.hide()
        self.Form.show()

    #dont accept other user and go on searchGUI
    def declineRequest(self):
        self.isOk = "OkNo"
        self.x = True
        self.acceptBtn.hide()
        self.declineBtn.hide()
        self.requestLabel.hide()
        self.requestUsername.hide()
        thread_wait = Thread(target=self.waitChat, args=())
        thread_wait.start()

