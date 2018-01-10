import clickable as clickable
from PyQt5 import QtCore, QtGui, QtWidgets
import ClientTcp
import  GUI.searchGUI
import GUI.registerGUI

class Ui_Login(object):
    #setupUi for Login page
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(394, 590)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 320, 291, 51))

        #This button is for Login and both Username and Passwor
        #are true then open searchGUI
        self.pushButton.clicked.connect(self.loginPushButton)

        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.designedLabel = QtWidgets.QLabel(self.centralwidget)
        self.designedLabel.setGeometry(QtCore.QRect(204, 560, 176, 17))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setUnderline(True)
        self.designedLabel.setFont(font)
        self.designedLabel.setObjectName("designedLabel")

        self.passwordLabel = QtWidgets.QLabel(self.centralwidget)
        self.passwordLabel.setGeometry(QtCore.QRect(50, 220, 61, 16))
        self.passwordLabel.setObjectName("passwordLabel")

        self.usernameLabel = QtWidgets.QLabel(self.centralwidget)
        self.usernameLabel.setGeometry(QtCore.QRect(50, 130, 61, 16))
        self.usernameLabel.setObjectName("usernameLabel")

        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(50, 40, 291, 51))

        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(20)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)

        self.titleLabel.setFont(font)
        self.titleLabel.setTextFormat(QtCore.Qt.AutoText)
        self.titleLabel.setScaledContents(False)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")

        self.goSingUpLabel = QtWidgets.QLabel(self.centralwidget)
        self.goSingUpLabel.setGeometry(QtCore.QRect(54, 416, 281, 22))

        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(10)

        self.goSingUpLabel.setFont(font)
        self.goSingUpLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.goSingUpLabel.setObjectName("goSingUpLabel")

        #This sentence is for sing up.
        self.goSingUpLabel.mousePressEvent = self.sing_click

        self.username_LE = QtWidgets.QLineEdit(self.centralwidget)
        self.username_LE.setGeometry(QtCore.QRect(50, 151, 291, 41))
        self.username_LE.setInputMask("")
        self.username_LE.setText("")
        self.username_LE.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.username_LE.setObjectName("username_LE")

        self.passwordLE = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordLE.setGeometry(QtCore.QRect(50, 240, 291, 41))
        self.passwordLE.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLE.setObjectName("passwordLE")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #This function open registerGUI
    def sing_click(self,event):
        self.windows = QtWidgets.QWidget()
        self.ui = GUI.registerGUI.Ui_Form()
        self.ui.setupUi(self.windows)
        MainWindow.hide()
        self.windows.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "LOGIN"))
        self.designedLabel.setText(_translate("MainWindow", "Designed by YUSUF & ONUR"))
        self.passwordLabel.setText(_translate("MainWindow", "Password"))
        self.usernameLabel.setText(_translate("MainWindow", "Username"))
        self.titleLabel.setText(_translate("MainWindow", "CHAT APP"))
        self.goSingUpLabel.setText(_translate("MainWindow", "Not a member? Sing Up now."))

    #function for login button
    def loginPushButton(self):
        username = self.username_LE.text()
        password = self.passwordLE.text()

        if (username == '' or password == ''):
            print("Boş bırakma gapcuk")
        else:
            client = ClientTcp.ClientTcp("2", str(username), str(password))
            client.start()
            client.join()
            print("login olabilirmi",client.feedback)
            if client.feedback == "Login":
                self.openWindow()

    #open searchGUI with function
    def openWindow(self):
        self.Form = QtWidgets.QWidget()
        self.ui = GUI.searchGUI.Ui_Search(self.username_LE.text())
        self.ui.setupUi(self.Form)
        MainWindow.hide()
        self.Form.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())