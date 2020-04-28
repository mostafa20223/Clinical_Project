from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType
import mysql.connector as sql
# import MySQLdb

ui,_ = loadUiType('design.ui')
login,_ = loadUiType('login.ui')

class login(QWidget, login):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Handel_login)

    def Handel_login(self):
        self.db = sql.connect(host = 'localhost', user = 'root', password = 'MUSTAFA!', db = 'mydatabase')
        self.cur = self.db.cursor()
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        sql = ''' SELECT * FROM users'''
        #for info in self.cur.execute(sql):
         #   print(info)
        self.cur.execute(sql)
        data = self.cur.fetchall()
        for row in data:
            if username == row[1] and password == row[3]:
                print('user match')
                self.window2 = MainApp()
                self.close()
                self.window2.show()
            else:
                self.label.setText('Make sure you entered your username and password correctly')


class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.Handel_UI_changes()
        self.Handel_buttons()
        self.Dark_orange_theme()

        self.show_category()
        

        self.show_category_combobox()
        

    def Handel_UI_changes(self):
        self.Hiding_Themes()
        self.tabWidget.tabBar().setVisible(False)
    
    
    def Handel_buttons(self):
        self.pushButton_5.clicked.connect(self.Show_Themes)
        self.pushButton_21.clicked.connect(self.Hiding_Themes)
        self.pushButton.clicked.connect(self.open_day_to_day_tab)
        self.pushButton_2.clicked.connect(self.open_books_tab)
        self.pushButton_3.clicked.connect(self.open_users_tab)
        self.pushButton_4.clicked.connect(self.open_settings_tab)

        self.pushButton_8.clicked.connect(self.Add_new_book)

        self.pushButton_14.clicked.connect(self.Add_category)
        

    

        self.pushButton_17.clicked.connect(self.Dark_orange_theme)
        self.pushButton_18.clicked.connect(self.Dark_blue_Theme)
        self.pushButton_20.clicked.connect(self.Dark_gray_theme)
        self.pushButton_19.clicked.connect(self.qdark_theme)

        self.pushButton_11.clicked.connect(self.Add_new_user)
        self.pushButton_12.clicked.connect(self.login)
        self.pushButton_13.clicked.connect(self.Edit_user)



    def Show_Themes(self):
        self.groupBox_4.show()

    def Hiding_Themes(self):
        self.groupBox_4.hide()

    ####################################################################
    ###################OPENING TABS####################################

    def open_day_to_day_tab(self):
        self.tabWidget.setCurrentIndex(0)
    
    
    def open_books_tab(self):
        self.tabWidget.setCurrentIndex(1)


    def open_users_tab(self):
        self.tabWidget.setCurrentIndex(2)
    
    
    def open_settings_tab(self):
        self.tabWidget.setCurrentIndex(3)

    ####################################################################
    ###################Books####################################
    def Add_new_book(self):
        
        self.db = sql.connect(host ='localhost' , user ='root' , password ='MUSTAFA!' ,db='mydatabase' )
        self.cur = self.db.cursor()
        
        book_title = self.lineEdit_8.text()
        book_code = self.lineEdit_7.text()
        book_category = self.comboBox_8.currentText()
        book_author = self.comboBox_7.currentText()
        book_publisher =self.comboBox_6.currentText()
        book_price = self.lineEdit_6.text()


    def Search_books(self):
        pass

    def Edit_boks(self):
        pass

    def Delete_books(self):
        pass

    ####################################################################
    ###################Users####################################
    def Add_new_user(self):
        self.db = sql.connect(host='localhost' , user='root' , password='****', db='mydatabase')
        self.cur = self.db.cursor()
        username = self.lineEdit_9.text()
        email=self.lineEdit_10.text()
        password = self.lineEdit_11.text()
        password2 = self.lineEdit_12.text()

        if password == password2:
            self.cur.execute('''
                INSERT INTO users(user_name , user_email ,user_password)
                VALUES(%s,%s,%s,%s)
            ''',(username,email,password))

            self.db.commit()
            self.statusBar().showMessage('New User Added')

        else:
            self.label_30.setText('Please add a valid password twice' )

    def login(self):
        self.db = sql.connect(host='localhost' , user='root' , password='****', db='mydatabase')
        self.cur = self.db.cursor()
        username = self.lineEdit_14.text()
        password = self.lineEdit_13.text()

        sql = ''' SELECT * FROM users'''
        #for info in self.cur.execute(sql):
         #   print(info)
        self.cur.execute(sql)
        data = self.cur.fetchall()
        for row in data:
            if username == row[1] and password == row[3]:
                print('user match')
                self.statusBar().showMessage('Valid username & password')
                self.groupBox_5.setEnabled(True)
                self.lineEdit_18.setText(row[1])
                self.lineEdit_16.setText(row[2])
                self.lineEdit_15.setText(row[3])


    def Edit_user(self):
        
        username = self.lineEdit_18.text()
        email=self.lineEdit_16.text()
        password = self.lineEdit_15.text()
        password2 =self.lineEdit_17.text()
        original_name = self.lineEdit_14.text()

        if password == password2:
            self.db = sql.connect(host='localhost' , user='root' , password='****', db='mydatabase')
            self.cur = self.db.cursor()

            self.cur.execute('''
                UPDATE users SET user_name = %s , user_email = %s , user_password = %s WHERE user_name =%s
            ''',(username,email,password, original_name))

            self.db.commit()
            self.statusBar().showMessage ('User data updated successfully')

        else:
            print('make sure you entered you password correctly')

    ####################################################################
    ###################Settings####################################
    def Add_category(self):
        self.db = sql.connect(host ='localhost' , user ='root' , password ='MUSTAFA!' ,db='mydatabase' )
        self.cur = self.db.cursor()

        category_name = self.lineEdit_19.text()

        self.cur.execute('''
            INSERT INTO category(category_name) VALUES (%s)
        ''',(category_name,))

        self.db.commit()
        self.statusBar().showMessage('New Category Added')
        self.lineEdit_19.setText('')
        self.show_category()

    def show_category(self):
        self.db = sql.connect(host ='localhost' , user ='root' , password ='MUSTAFA!' ,db='mydatabase' )
        self.cur = self.db.cursor()

        self.cur.execute('''SELECT category_name FROM category''')
        data = self.cur.fetchall()
        #print(data)

        if data:
            self.tableWidget_2.setRowCount(0)
            self.tableWidget_2.insertRow(0)
            for row , form in enumerate(data):
                for column , item in enumerate(form):
                    self.tableWidget_2.setItem(row,column,QTableWidgetItem(str(item)))
                    column +=1

                row_position = self.tableWidget_2.rowCount()
                self.tableWidget_2.insertRow(row_position)

    ####################################################################
    ###################Show Settings data in UI####################################
    def show_category_combobox(self):
        self.db = sql.connect(host = 'localhost', user = 'root', password = 'MUSTAFA!', db = 'mydatabase')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT category_name FROM category''')
        data = self.cur.fetchall()
        print(data)
        for category in data:
            print(category[0])
            self.comboBox_3.addItem(category[0])
    
    ####################################################################
    ###################UI Themes####################################
    def Dark_blue_Theme(self):
        style = open('themes/darkblue.css', 'r')
        style=style.read()
        self.setStyleSheet(style)

    def Dark_gray_theme(self):
        style = open('themes/darkgray.css', 'r')
        style=style.read()
        self.setStyleSheet(style)

    def Dark_orange_theme(self):
        style = open('themes/darkorange.css', 'r')
        style=style.read()
        self.setStyleSheet(style)

    def qdark_theme(self):
        style = open('themes/qdark.css', 'r')
        style=style.read()
        self.setStyleSheet(style)


def main():
    app=QApplication(sys.argv)
    window=login()
    window.show()
    app.exec_()

if __name__=='__main__':
    main()








