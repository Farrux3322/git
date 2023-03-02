from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def __init__(self, username):
        self.username = username

    def setupUi(self, Form, moveX = 100, moveY = 100):
        Form.setObjectName("Form")
        Form.setGeometry(moveX, moveY, 489, 542)
        self.userNameLabel = QtWidgets.QLabel(Form)
        self.userNameLabel.setGeometry(QtCore.QRect(40, 40, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.userNameLabel.setFont(font)
        self.userNameLabel.setObjectName("userNameLabel")
        self.messagesList = QtWidgets.QListWidget(Form)
        self.messagesList.setGeometry(QtCore.QRect(60, 80, 301, 361))
        self.messagesList.setObjectName("messagesList")
        self.messageInput = QtWidgets.QLineEdit(Form)
        self.messageInput.setGeometry(QtCore.QRect(40, 460, 341, 31))
        self.messageInput.setObjectName("messageInput")
        self.sendBtn = QtWidgets.QPushButton(Form)
        self.sendBtn.setGeometry(QtCore.QRect(390, 460, 75, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sendBtn.setFont(font)
        self.sendBtn.setObjectName("sendBtn")
        self.clearBtn = QtWidgets.QPushButton(Form)
        self.clearBtn.setGeometry(QtCore.QRect(370, 80, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.clearBtn.setFont(font)
        # buttonni bosilmidigan qib qoyish
        # self.clearBtn.setEnabled(False)

        self.clearBtn.setObjectName("clearBtn")
        self.clearBtn_2 = QtWidgets.QPushButton(Form)
        self.clearBtn_2.setGeometry(QtCore.QRect(370, 120, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.clearBtn_2.setFont(font)
        self.clearBtn_2.setObjectName("clearBtn_2")
        self.clearBtn_3 = QtWidgets.QPushButton(Form)
        self.clearBtn_3.setGeometry(QtCore.QRect(370, 160, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.clearBtn_3.setFont(font)
        self.clearBtn_3.setObjectName("clearBtn_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        Form.show()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.userNameLabel.setText(_translate("Form", self.username))
        self.sendBtn.setText(_translate("Form", "Send"))
        self.clearBtn.setText(_translate("Form", "Clear"))
        self.clearBtn_2.setText(_translate("Form", "Delete"))
        self.clearBtn_3.setText(_translate("Form", "Edit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
