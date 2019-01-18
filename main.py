import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtCore, QtWidgets
import design  # Это наш конвертированный файл дизайна
import vk_api
import random
import time

class myQListWidget(QtWidgets.QListWidget):
    def __init__(self): 
        self.peer_id   


class Login(QtWidgets.QMainWindow, design.Ui_Login):

    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.chkLogin)
        self.closeButton.clicked.connect(self.close)
    

    def chkLogin(self):
        email = str(self.lineEdit.text())
        password = str(self.lineEdit_2.text())

        #self.setFocusPolicy(QtCore.Qt.NoFocus)
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        time.sleep(2)
        try:
            vk = vk_api.VkApi(login = email, password = password) 
            vk.auth()

            self.mainform = Main(vk)
            self.mainform.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.mainform.show()
            self.hide()
        except:
            print("auth error")
        QtWidgets.QApplication.restoreOverrideCursor()
        
     

class Main(QtWidgets.QMainWindow, design.Ui_MainWindow):
    
    def __init__(self, vk, parent=None):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super(Main,self).__init__(parent)

        self.vk = vk
 
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        self.sendButton.clicked.connect(self.sendMsg)
        self.closeButton.clicked.connect(self.close)
        self.listWidget.itemDoubleClicked.connect(self.add)  

    def add(self):
        add = self.listWidget.currentItem()
        self.listWidget_2.addItem(add)

        #self.pushButton.clicked.connect(self.on_pushButton_clicked)
        #self.dialog = Second(self)

    #def on_pushButton_clicked(self):
       # self.dialog.show()

    def sendMsgtest(self): 

        rand_id = 0

        vk_get_api = self.vk.get_api() 

        vk_get_api.messages.send(
            random_id=rand_id,
            user_id=35109961,
            message=str(self.textEdit.toPlainText())
            )
        rand_id = rand_id + 1
    
    def sendMsg(self): 
        rand_id = 0
        
        vk_get_api = self.vk.get_api() 

        allConversations = vk_get_api.messages.getConversations()
       

        #API has limit for requests equals to 20 
        #so we calculate num of iterations and check all dialogs what we need 
        text = str(self.textEdit.toPlainText())

        numOfConv = allConversations["count"]

        lim = numOfConv//20 + 1
        j = 0
        i = 0
        msgForce = 1
        randIdForMsg = 0

        print(numOfConv)
        print(j)

        counter=0
        prev_fail = 0


        myOffset=0
        while j < lim:
            #time.sleep(3)
            allConversations = vk_get_api.messages.getConversations(offset=myOffset)
            i = 0

            while i < 20:
                try:
                    if allConversations["items"][i]["conversation"]["peer"]["type"]=="chat" and allConversations["items"][i]["conversation"]["chat_settings"]["title"][0]!="Э":
                        self.listWidget.addItem(str(allConversations["items"][i]["conversation"]["chat_settings"]["title"]))
                        print(allConversations["items"][i]["conversation"]["chat_settings"]["title"], end = " --- ")        
                        print(allConversations["items"][i]["conversation"]["peer"]["local_id"])
                        #time.sleep(1)
                        id = 2000000000+(allConversations["items"][i]["conversation"]["peer"]["local_id"])
                        #This is catch for message.send() limits of api
                        #if msg is not send we wait for 1 second and try again
                        while msgForce==1:
                            try:
                                #vk_get_api.messages.send(random_id=rand_id,peer_id=id,message=text)
                                #rand_id = rand_id + 1
                                msgForce = 0
                                randIdForMsg = randIdForMsg + 1
                            except:
                                time.sleep(1)
                                msgForce = 1    

                        counter = counter + 1
                        prev_fail = 0
                except:
                    #This segment starts when something goes wrong
                    if prev_fail == 0:
                        print("---")
                    prev_fail = 1
                i = i + 1
            myOffset = myOffset + 20
            j = j + 1
            
        self.listWidget.addItem("Найдено "+str(counter))    
        print("Найдено "+str(counter))


        #single msg
        #vk_get_api.messages.send( 
        #    peer_id=35109961, 
        #    message=str(self.textEdit.toPlainText()), 
        #    random_id = rand_id
        #)

        #rand_id = rand_id + 1

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication

    window = Login()  # Создаём объект класса Login
    window.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
