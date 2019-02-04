import sys  # sys нужен для передачи argv в QApplication
import os
from PyQt5 import QtCore, QtWidgets, QtGui

# UI files
import designMain
import designLogin
import error
import designSelect
import d_find


import vk_api
import random
import time
import threading
import asyncio
import json



class ListsSelect(QtWidgets.QMainWindow, designSelect.Ui_ListsSelect):

    def __init__(self, mainform ,parent=None):
        super(ListsSelect, self).__init__(parent)
        self.setupUi(self)
        self.mainform = mainform
        self.closeButton.clicked.connect(self.close)
        self.pushButton.clicked.connect(self.addList)


        allLists = os.listdir(path=".") 
        self.numOfLists = 0

        for b_list in range(len(allLists)):
            if allLists[b_list].find(".json") != -1 and allLists[b_list].find("vk_config.v2") == -1:
                self.myList = allLists[b_list].replace(".json","")
                self.listWidget.addItem(self.myList)
                self.numOfLists = self.numOfLists + 1
    
    def addList(self,mainform):
        add = self.listWidget.currentItem()
        add_text = add.text() + ".json"
        with open(add_text, "r") as read_file:
            data = json.load(read_file)

        for chat in range(len(data)):
            bufferListItem = QtWidgets.QListWidgetItem()    
            bufferListItem.setText(data[chat][0])
            bufferListItem.setStatusTip(data[chat][1])
            self.mainform.sendListWidget.addItem(bufferListItem)

        self.close()

 
    def mousePressEvent(self, event):
        self.offset = event.pos()
    def mouseMoveEvent(self, event):
        x=event.globalX()
        y=event.globalY()
        x_w = self.offset.x()
        y_w = self.offset.y()
        self.move(x-x_w, y-y_w)

class ErrorMsg(QtWidgets.QMainWindow, error.Ui_Error):

    def __init__(self, mainform ,parent=None):
        super(ErrorMsg, self).__init__(parent)
        self.setupUi(self)
        self.closeButton.clicked.connect(self.close)
 
    def mousePressEvent(self, event):
        self.offset = event.pos()
    def mouseMoveEvent(self, event):
        x=event.globalX()
        y=event.globalY()
        x_w = self.offset.x()
        y_w = self.offset.y()
        self.move(x-x_w, y-y_w)

class Find(QtWidgets.QMainWindow, d_find.Ui_Find):

    def __init__(self, mainform ,parent=None):
        super(Find, self).__init__(parent)
        self.mainform = mainform
        self.setupUi(self)

        #self.pushButton.clicked.connect(self.chkLogin)
        self.closeButton.clicked.connect(self.close)
        self.pushButton.clicked.connect(self.find)
 
    def find(self):
        self.mainform.req = self.lineEdit.text()
        self.close()
        t = threading.Thread(target=self.mainform.findGrp())
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

class Login(QtWidgets.QMainWindow, designLogin.Ui_Login):

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

            try:
                self.mainform = Main(vk)
                QtWidgets.QApplication.restoreOverrideCursor()
                self.mainform.setWindowFlags(QtCore.Qt.FramelessWindowHint)
                self.mainform.show()
                self.hide()
            except:
                print("form error")
        except:
            self.autherr = ErrorMsg(self)  
            self.autherr.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.autherr.show()
            print("auth error")
        QtWidgets.QApplication.restoreOverrideCursor()

        
        
     

class Main(QtWidgets.QMainWindow, designMain.Ui_MainWindow):
    
    def __init__(self, vk, parent=None):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super(Main,self).__init__(parent)
        self.req = "all"
        self.vk = vk
        self.chat_list = []
    

        try:
            self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        except:
            print("UI problems")

        #self.findButton.clicked.connect(self.findItem)

        self.sendButton.clicked.connect(self.sendMsg)
        self.findButton.clicked.connect(self.findItem)
        self.closeButton.clicked.connect(self.close)
        self.rollButton.clicked.connect(self.showMinimized)
        self.selectAllButton.clicked.connect(self.selectAll)
        self.addListButton.clicked.connect(self.addListMenu)
        self.loadListsButton.clicked.connect(self.loadListsMenu)
        self.listWidget.itemDoubleClicked.connect(self.add)
        self.sendListWidget.itemDoubleClicked.connect(self.delitem)
        #self.textEdit.textChanged.connect(self.textToUTF8)

        

        t = threading.Thread(target=self.firstfindGrp)
        t.daemon = True
        t.start()

    #def textToUTF8(self):
        #i don't know how to fix this problem yet
        #self.textEdit.setText(self.textEdit.toPlainText().encode("utf-8").decode('cp1252'))
        #convert to unicode
        #teststring = self.textEdit.toPlainText().encode("unicode_escape")
        #teststring = self.textEdit.toHtml()
        #teststring = QtGui.QTextDocumentFragment.fromHtml(teststring)
        #encode it with string escape
        #teststring = teststring.encode('unicode_escape')
        #print(teststring)


    def loadListsMenu(self):
        self.loadList = ListsSelect(self)  
        self.loadList.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.loadList.show()

    def addListMenu(self):

        self.addWidget = Find(self) 
        self.addWidget.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.addWidget.label.setText("Имя нового списка")
        self.addWidget.pushButton.setText("Добавить")
        self.addWidget.pushButton.clicked.disconnect()
        self.addWidget.pushButton.clicked.connect(self.addList)
        self.addWidget.pushButton.clicked.connect(self.addWidget.close)
        self.addWidget.show()

    def addList(self):
        
        jsonItems = []

        currentItem = 0

        saveList = self.sendListWidget

        print(saveList.count())
        while currentItem < saveList.count():
                jsonItems.append([saveList.item(currentItem).text(), saveList.item(currentItem).statusTip()])
                print(saveList.item(currentItem).text())
                print(saveList.item(currentItem).statusTip())
                currentItem = currentItem + 1           
        
        savename = self.addWidget.lineEdit.text()+'.json'

        with open(savename, 'w') as file:
               json.dump(jsonItems, file, indent=2)

        self.sendListWidget.clear()


        #USING ErrorMsg to show OK window
        self.done_msg = ErrorMsg(self)  
        self.done_msg.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.done_msg.label.setText("Готово")
        self.done_msg.closeButton.setStyleSheet("QPushButton{background-color:#3f4d63;color:white;}QPushButton:hover{background-color:#1dba9b;}")
        self.done_msg.show()


        
    def findItem(self):    
        self.findWidget = Find(self) 
        self.findWidget.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.findWidget.show()

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
        
        self.sendListWidget.insertItem(0,add.text())
        self.sendListWidget.item(0).setStatusTip(add.statusTip())
    
    def delitem(self):
        SelectedItem = self.sendListWidget.currentItem()
        self.sendListWidget.takeItem(self.sendListWidget.row(SelectedItem))
  
    def firstfindGrp(self):
        self.listWidget.clear()
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        
        vk_get_api = self.vk.get_api() 
        allConversations = vk_get_api.messages.getConversations()
        #API has limit for requests equals to 20 
        #so we calculate num of iterations and check all dialogs what we need
        numOfConv = allConversations["count"]

        lim = numOfConv//20 + 1
        j = 0
        i = 0
    
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
                        
                        bufferListItem = QtWidgets.QListWidgetItem()    
                        bufferListItem.setText(allConversations["items"][i]["conversation"]["chat_settings"]["title"])
                        bufferListItem.setStatusTip(str(allConversations["items"][i]["conversation"]["peer"]["local_id"]))

                        self.listWidget.addItem(bufferListItem)
                        self.chat_list.append([bufferListItem.text(),bufferListItem.statusTip()])
                        
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
        QtWidgets.QApplication.restoreOverrideCursor()
        
        self.listWidget.addItem("Всего "+str(counter))   

    def findGrp(self):
        counter = 0
        self.sendListWidget.clear()
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        
        for i in range(len(self.chat_list)):

            if self.chat_list[i][0].find(self.req) != -1:
                bufferListItem = QtWidgets.QListWidgetItem()    
                bufferListItem.setText(self.chat_list[i][0])
                bufferListItem.setStatusTip(self.chat_list[i][1])
                self.sendListWidget.addItem(bufferListItem)

                counter = counter + 1

        QtWidgets.QApplication.restoreOverrideCursor()

        if counter == 0:
            self.autherr = ErrorMsg(self)  
            self.autherr.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.autherr.label.setText("Не найдено")
            self.autherr.show()

    def selectAll(self):
        self.sendListWidget.clear()
        for i in range(len(self.chat_list)):           
            bufferListItem = QtWidgets.QListWidgetItem()    
            bufferListItem.setText(self.chat_list[i][0])
            bufferListItem.setStatusTip(self.chat_list[i][1])
            self.sendListWidget.addItem(bufferListItem)
        


    def sendMsg(self):
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor) 
        rand_id = random.randint(0,14341324)
        
        vk_get_api = self.vk.get_api() 

        text = self.textEdit.toHtml()
        #print(text)
        text = text.replace('<img src="https://vk.com/emoji/e/f09f988e.png" />','&#128526;')
        text = text.replace('<img src="https://vk.com/emoji/e/f09f91b9.png" />','👹')
        text = text.replace('<img src="https://vk.com/emoji/e/f09f91ba.png" />','&#128122;')
        #text = text.replace('%F0%9F%98%8E','&#128526;')
        #<img class="emoji" src="/emoji/e/f09f91b9.png" alt="👹">
        
        self.textEdit.clear()
        self.textEdit.insertHtml(text)
        text = self.textEdit.toPlainText()

        numOfConv = self.sendListWidget.count()

        
        j = 0

        while j < numOfConv:
            time.sleep(.200)
            try:
                id = 2000000000+int(self.sendListWidget.item(j).statusTip())
                #This is catch for message.send() limits of api
                #if msg is not send we wait for 1 second and try again
                try:
                    vk_get_api.messages.send(random_id=rand_id,peer_id=id,message=text)
                    rand_id = rand_id + 5
                    print(self.sendListWidget.item(j).statusTip())
                    print(rand_id)
                except:
                    time.sleep(1) 
            except:
                time.sleep(1)   
            j = j + 1
        self.sendListWidget.clear()

        #USING ErrorMsg to show OK window
        self.done_msg = ErrorMsg(self)  
        self.done_msg.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.done_msg.label.setText("Готово")
        self.done_msg.closeButton.setStyleSheet("QPushButton{background-color:#3f4d63;color:white;}QPushButton:hover{background-color:#1dba9b;}")
        self.done_msg.show()

        QtWidgets.QApplication.restoreOverrideCursor()

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication

    window = Login()  # Создаём объект класса Login
    window.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    effect = QtWidgets.QGraphicsDropShadowEffect(blurRadius=5, xOffset=3, yOffset=3)
    window.setGraphicsEffect(effect)
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()