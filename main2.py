import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QListWidgetItem
from chatWindow import Ui_Form

class Chat:
  def __init__(self, user1: Ui_Form, user2: Ui_Form):
    user1.sendBtn.clicked.connect(lambda: self.sendMessage(user1, user2))
    user2.sendBtn.clicked.connect(lambda: self.sendMessage(user2, user1))
    user1.clearBtn.clicked.connect(lambda: self.clearMessagesList(user1, user2))
    user2.clearBtn.clicked.connect(lambda: self.clearMessagesList(user1, user2))


  def sendMessage(self, from_user: Ui_Form, to_user: Ui_Form):
    txt = from_user.messageInput.text().strip()
    from_user.messageInput.clear()
    if not len(txt):
      return
    
    edited_text = f"{from_user.username}:\n{self.formatText(txt)}"

    item = QListWidgetItem()
    item.setText(edited_text)
    item.setTextAlignment(Qt.AlignRight)

    from_user.messagesList.addItem(item)
    to_user.messagesList.addItem(edited_text)
  
  def clearMessagesList(self, user1: Ui_Form, user2: Ui_Form):
    user1.messagesList.clear()
    user2.messagesList.clear()

  @staticmethod
  def formatText(txt):
    s, count = '', 0
    txt = txt.split()
    for soz in txt:
      if count + len(soz) < 30:
        s += " " + soz
        count += len(soz)
      else:
        s += "\n" + soz
        count = len(soz)
    return s


app = QtWidgets.QApplication(sys.argv)
Form1 = QtWidgets.QWidget()
Form2 = QtWidgets.QWidget()

user1 = Ui_Form("Eshmat Toshmatov")
user2 = Ui_Form("Toshmat Eshmatov")

user1.setupUi(Form1)
user2.setupUi(Form2, 700, 100)


chat = Chat(user1, user2)


sys.exit(app.exec_())