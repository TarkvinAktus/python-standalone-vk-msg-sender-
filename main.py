#
import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
import design  # Это наш конвертированный файл дизайна
import vk_api
import random

class Second(QtWidgets.QMainWindow, design.Ui_MainWindow):

    def __init__(self, parent=None):
        super(Second, self).__init__(parent)
        self.setupUi(self)
        

class Main(QtWidgets.QMainWindow, design.Ui_MainWindow):
    
    def __init__(self, parent=None):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super(Main,self).__init__(parent)

        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        #self.pushButton.clicked.connect(self.sendMsg)

        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.dialog = Second(self)

    def on_pushButton_clicked(self):
        self.dialog.show()
    
    def sendMsg(self): 
        rand_id = 0
        vk = vk_api.VkApi(login = '', password = '') 
        vk.auth() 
        vk_get_api = vk.get_api() 

        vk_get_api.messages.send( 
            peer_id=, 
            message='', 
            random_id = rand_id
        )

        rand_id = rand_id + 1

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = Main()  # Создаём объект класса Main
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()