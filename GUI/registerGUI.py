from PyQt5 import QtCore, QtGui, QtWidgets
import ClientTcp
import GUI.loginGui2

class Ui_Form(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Form")
        MainWindow.resize(400, 589)

        self.wn = MainWindow

        self.registerBtn = QtWidgets.QPushButton(MainWindow)
        self.registerBtn.setGeometry(QtCore.QRect(50, 320, 291, 51))
        self.registerBtn.setObjectName("registerBtn")

        #this button sing up into mongoDB for username_LE and self.password_LE
        self.registerBtn.clicked.connect(self.register_click)

        self.usernameLabel = QtWidgets.QLabel(MainWindow)
        self.usernameLabel.setGeometry(QtCore.QRect(50, 130, 61, 16))
        self.usernameLabel.setObjectName("usernameLabel")

        self.goLoginLabel = QtWidgets.QLabel(MainWindow)
        self.goLoginLabel.setGeometry(QtCore.QRect(54, 416, 281, 22))

        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(10)

        self.goLoginLabel.setFont(font)
        self.goLoginLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.goLoginLabel.setObjectName("goLoginLabel")

        #if user is login then user can press this button
        self.goLoginLabel.mousePressEvent = self.openWindow

        self.designedLabel = QtWidgets.QLabel(MainWindow)
        self.designedLabel.setGeometry(QtCore.QRect(204, 560, 176, 17))

        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setUnderline(True)

        self.designedLabel.setFont(font)
        self.designedLabel.setObjectName("designedLabel")

        self.passwordLabel = QtWidgets.QLabel(MainWindow)
        self.passwordLabel.setGeometry(QtCore.QRect(50, 220, 61, 16))
        self.passwordLabel.setObjectName("passwordLabel")

        self.titleLabel = QtWidgets.QLabel(MainWindow)
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

        self.username_LE = QtWidgets.QLineEdit(MainWindow)
        self.username_LE.setGeometry(QtCore.QRect(50, 150, 291, 41))
        self.username_LE.setInputMask("")
        self.username_LE.setText("")
        self.username_LE.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.username_LE.setObjectName("username_LE")

        self.password_LE = QtWidgets.QLineEdit(MainWindow)
        self.password_LE.setGeometry(QtCore.QRect(50, 240, 291, 41))
        self.password_LE.setInputMask("")
        self.password_LE.setText("")
        self.password_LE.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_LE.setObjectName("password_LE")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Form", "Form"))
        self.registerBtn.setText(_translate("Form", "REGISTER"))
        self.usernameLabel.setText(_translate("Form", "Username"))
        self.goLoginLabel.setText(_translate("Form", "Already registered! Login Me."))
        self.designedLabel.setText(_translate("Form", "Designed by YUSUF & ONUR"))
        self.passwordLabel.setText(_translate("Form", "Password"))
        self.titleLabel.setText(_translate("Form", "CHAT APP"))


    #this function sing up username and password
    def register_click(self):
        if (self.username_LE.text() == "") or (self.password_LE.text() == ""):
            print("burayı doldurun",self.username_LE.text(),self.password_LE.text())
        else:
            username = self.username_LE.text()
            password = self.password_LE.text()

            client = ClientTcp.ClientTcp("1", str(username), str(password))
            client.start()
            client.join()
            print("kaydetti",client.feedback)

            self.openWindow()

    #again return loginGUI with this function
    def openWindow(self,event=""):
        self.windows = QtWidgets.QMainWindow()
        self.ui = GUI.loginGui2.Ui_Login()
        self.ui.setupUi(self.windows)
        self.wn.hide()
        self.windows.show()




