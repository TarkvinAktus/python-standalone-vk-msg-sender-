import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtCore, QtWidgets
import design  # Это наш конвертированный файл дизайна
import vk_api
import random
import time
import threading
import asyncio

class Find(QtWidgets.QMainWindow, design.Ui_Find):

    def __init__(self, parent=None):
        super(Find, self).__init__(parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.findDialogs)
        self.closeButton.clicked.connect(self.close)
    
    def mousePressEvent(self, event):
        self.offset = event.pos()
    def mouseMoveEvent(self, event):
        x=event.globalX()
        y=event.globalY()
        x_w = self.offset.x()
        y_w = self.offset.y()
        self.move(x-x_w, y-y_w)


    def findDialogs(self):
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

class Login(QtWidgets.QMainWindow, design.Ui_Login):

    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.chkLogin)
        self.closeButton.clicked.connect(self.close)
    
    def mousePressEvent(self, event):
        self.offset = event.pos()
    def mouseMoveEvent(self, event):
        x=event.globalX()
        y=event.globalY()
        x_w = self.offset.x()
        y_w = self.offset.y()
        self.move(x-x_w, y-y_w)


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
            QtWidgets.QApplication.restoreOverrideCursor()
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
        self.req = "all"
        self.vk = vk

 
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна


        self.findButton.clicked.connect(self.findGrp)
        self.sendButton.clicked.connect(self.sendMsg)
        #self.findButton.clicked.connect(self.sendMsg)
        self.closeButton.clicked.connect(self.close)
        self.listWidget.itemDoubleClicked.connect(self.add)
        self.listWidget_2.itemDoubleClicked.connect(self.delitem)

        t = threading.Thread(target=self.findGrp)
        t.daemon = True
        t.start()
        
        


    def mousePressEvent(self, event):
        self.offset = event.pos()
    def mouseMoveEvent(self, event):
        x=event.globalX()
        y=event.globalY()
        x_w = self.offset.x()
        y_w = self.offset.y()
        self.move(x-x_w, y-y_w)

    def add(self):
        add = self.listWidget.currentItem()
        
        self.listWidget_2.insertItem(0,add.text())
        self.listWidget_2.item(0).setStatusTip(add.statusTip())
    
    def delitem(self):
        SelectedItem = self.listWidget_2.currentItem()
        self.listWidget_2.takeItem(self.listWidget_2.row(SelectedItem))

    def sendMsgtest(self): 

        rand_id = 0

        vk_get_api = self.vk.get_api() 

        vk_get_api.messages.send(
            random_id=rand_id,
            user_id=35109961,
            message=str(self.textEdit.toPlainText())
            )
        rand_id = rand_id + 1


    
    def findGrp(self):
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        rand_id = 0
        
        vk_get_api = self.vk.get_api() 

        allConversations = vk_get_api.messages.getConversations()
       

        #API has limit for requests equals to 20 
        #so we calculate num of iterations and check all dialogs what we need

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
                        
                        if self.req == "all":
                            bufferListItem = QtWidgets.QListWidgetItem()    
                            bufferListItem.setText(allConversations["items"][i]["conversation"]["chat_settings"]["title"])
                            bufferListItem.setStatusTip(str(allConversations["items"][i]["conversation"]["peer"]["local_id"]))
                            self.listWidget.addItem(bufferListItem)
                            print(str(bufferListItem.text()))
                            print(str(bufferListItem.statusTip()))
                        else: 
                            if dialogTitle.find(req) != -1:
                                bufferListItem = QtWidgets.QListWidgetItem()    
                                bufferListItem.setText(allConversations["items"][i]["conversation"]["chat_settings"]["title"])
                                bufferListItem.setStatusTip(str(allConversations["items"][i]["conversation"]["peer"]["local_id"]))
                                self.listWidget.addItem(bufferListItem)
                                print(str(bufferListItem.text()))
                                print(str(bufferListItem.statusTip()))
                            else:
                                i = i + 1
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
        #print("Найдено "+str(counter))

        QtWidgets.QApplication.restoreOverrideCursor()
        





    def sendMsg(self):
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor) 
        rand_id = random.randint(0,14341324)
        
        vk_get_api = self.vk.get_api() 

        allConversations = vk_get_api.messages.getConversations()
       

        #API has limit for requests equals to 20 
        #so we calculate num of iterations and check all dialogs what we need 

        
        text = str(self.textEdit.toPlainText())

        print(text)
        

        numOfConv = self.listWidget_2.count()

        
        j = 0
        i = 0
        n = 0
        msgForce = 1
        randIdForMsg = 0

        print(numOfConv)
        print(j)

        counter=0

        while j < numOfConv:
            time.sleep(.100)
            try:
                id = 2000000000+int(self.listWidget_2.item(j).statusTip())
                #This is catch for message.send() limits of api
                #if msg is not send we wait for 1 second and try again
                try:
                    vk_get_api.messages.send(random_id=rand_id,peer_id=id,message=text)
                    rand_id = rand_id + 5
                    print(self.listWidget_2.item(j).statusTip())
                    print(rand_id)
                except:
                    time.sleep(1) 
            except:
                time.sleep(1)   
            j = j + 1
        QtWidgets.QApplication.restoreOverrideCursor()


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
