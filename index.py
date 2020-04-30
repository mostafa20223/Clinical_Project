from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType
import mysql.connector
# import MySQLdb

ui,_ = loadUiType('design.ui')
login,_ = loadUiType('login.ui')

class login(QWidget, login):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.login_btn.clicked.connect(self.Handel_login)

    def Handel_login(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()
        username = self.user_enter.text()
        password = self.pass_enter.text()

        sql = ''' SELECT * FROM users '''
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
                self.login_failed.setText('Make sure you entered your username and password correctly')


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
        self.themes_btn.clicked.connect(self.Show_Themes)
        self.hidethemes_btn.clicked.connect(self.Hiding_Themes)
        self.pushButton.clicked.connect(self.open_day_to_day_tab)
        self.pushButton_2.clicked.connect(self.open_books_tab)
        self.user_tab.clicked.connect(self.open_users_tab)
        self.more_info_tab.clicked.connect(self.open_info_tab)
        self.pushButton_8.clicked.connect(self.Add_new_book)
        self.add_cat_btn.clicked.connect(self.Add_category)
        self.pushButton_17.clicked.connect(self.Dark_orange_theme)
        self.pushButton_18.clicked.connect(self.Dark_blue_Theme)
        self.pushButton_20.clicked.connect(self.Dark_gray_theme)
        self.pushButton_19.clicked.connect(self.qdark_theme)
        self.add_user_btn.clicked.connect(self.Add_new_user)
        self.user_login_btn.clicked.connect(self.login)
        self.edit_user_btn.clicked.connect(self.Edit_user)

    def Show_Themes(self):
        self.groupBox_4.show()
    def Hiding_Themes(self):
        self.groupBox_4.hide()

    # TABS
    def open_day_to_day_tab(self):
        self.tabWidget.setCurrentIndex(0)
    def open_books_tab(self):
        self.tabWidget.setCurrentIndex(1)
    def open_users_tab(self):
        self.tabWidget.setCurrentIndex(2)
    def open_info_tab(self):
        self.tabWidget.setCurrentIndex(3)

    # Books
    def Add_new_book(self):        
        self.db = mysql.connector.connect(host ='localhost' , user ='root' , password ='DARSH1999' ,db='cmms' )
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

    # Users
    def Add_new_user(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()
        username = self.add_user.text()
        email = self.add_email.text()
        password = self.add_pass.text()
        password2 = self.readd_pass.text()

        if password == password2:
            self.cur.execute(''' INSERT INTO users (username, email, password) VALUES (%s, %s, %s) '''
                             , (username, email, password))
            self.db.commit()
            self.statusBar().showMessage('New User Added')
        else:
            # self.add_failed.setText('Please add a valid password twice')
            self.statusBar().showMessage('Please add a valid password twice')

    def login(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()
        username = self.access_user.text()
        password = self.access_pass.text()

        sql = ''' SELECT * FROM users '''
        #for info in self.cur.execute(sql):
         #   print(info)
        self.cur.execute(sql)
        data = self.cur.fetchall()
        for row in data:
            if username == row[1] and password == row[3]:
                print('user match')
                self.statusBar().showMessage('Valid username & password')
                self.groupBox_5.setEnabled(True)
                self.edit_user.setText(row[1])
                self.edit_email.setText(row[2])
                self.edit_pass.setText(row[3])

    def Edit_user(self):
        username = self.edit_user.text()
        email = self.edit_email.text()
        password = self.edit_pass.text()
        password2 = self.reedit_pass.text()
        original_name = self.access_user.text()

        if password == password2:
            self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
            self.cur = self.db.cursor()

            self.cur.execute(''' UPDATE users SET username = %s, email = %s, password = %s WHERE username = %s '''
                             , (username, email, password, original_name))
            self.db.commit()
            self.statusBar().showMessage('User data updated successfully')
        else:
            self.statusBar().showMessage('make sure you entered you password correctly')

    # Category
    def Add_category(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()
        category_name = self.cat_name.text()
        category_floor = self.cat_floor.text()

        self.cur.execute(''' INSERT INTO category (name, floor) VALUES (%s, %s) '''
                         , (category_name, category_floor))
        self.db.commit()
        self.statusBar().showMessage('New Category Added')
        self.cat_name.setText(' ')
        self.cat_floor.setText(' ')
        self.show_category()

    def show_category(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()
        self.cur.execute(''' SELECT name FROM category ''')
        data = self.cur.fetchall()
        #print(data)

        if data:
            self.tableWidget_2.setRowCount(0)
            self.tableWidget_2.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_2.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1
                row_position = self.tableWidget_2.rowCount()
                self.tableWidget_2.insertRow(row_position)

    # Show Category in UI
    def show_category_combobox(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT name FROM category ''')
        data = self.cur.fetchall()
        print(data)
        for category in data:
            print(category[0])
            self.comboBox_3.addItem(category[0])

    # Equipment
    def Add_equipment(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()
        ssn = self.cat_name.text()
        eng_name = self.cat_floor.text()
        eng_phone = self.cat_name.text()
        eng_email = self.cat_floor.text()

        self.cur.execute(''' INSERT INTO engineer (ssn, eng name, eng phone, eng email) VALUES (%s, %s, %s, %s) '''
                         , (ssn, eng_name, eng_phone, eng_email))
        self.db.commit()
        self.statusBar().showMessage('New Engineer Added')
        self.cat_name.setText(' ')
        self.cat_floor.setText(' ')
        self.cat_name.setText(' ')
        self.cat_floor.setText(' ')
        self.show_engineer()

    def show_engineer(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()
        self.cur.execute(''' SELECT ssn FROM engineer ''')
        data = self.cur.fetchall()
        #print(data)

        if data:
            self.tableWidget_2.setRowCount(0)
            self.tableWidget_2.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_2.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1
                row_position = self.tableWidget_2.rowCount()
                self.tableWidget_2.insertRow(row_position)

    # Engineer
    def Add_engineer(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()
        ssn = self.cat_name.text()
        eng_name = self.cat_floor.text()
        eng_phone = self.cat_name.text()
        eng_email = self.cat_floor.text()

        self.cur.execute(''' INSERT INTO engineer (ssn, eng name, eng phone, eng email) VALUES (%s, %s, %s, %s) '''
                         , (ssn, eng_name, eng_phone, eng_email))
        self.db.commit()
        self.statusBar().showMessage('New Engineer Added')
        self.cat_name.setText(' ')
        self.cat_floor.setText(' ')
        self.cat_name.setText(' ')
        self.cat_floor.setText(' ')
        self.show_engineer()

    def show_engineer(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()
        self.cur.execute(''' SELECT ssn FROM engineer ''')
        data = self.cur.fetchall()
        #print(data)

        if data:
            self.tableWidget_2.setRowCount(0)
            self.tableWidget_2.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_2.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1
                row_position = self.tableWidget_2.rowCount()
                self.tableWidget_2.insertRow(row_position) 

    # Vendor
    def Add_vendor(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()
        vendor_name = self.cat_name.text()
        vendor_ssn = self.cat_floor.text()
        vendor_phone = self.cat_floor.text()
        vendor_email = self.cat_floor.text()

        self.cur.execute(''' INSERT INTO vendor (vendor ssn, vendor name, vendor phone, vendor email) VALUES (%s, %s, %s, %s) '''
                         , (vendor_ssn, vendor_name, vendor_phone, vendor_email))
        self.db.commit()
        self.statusBar().showMessage('New Vendor Added')
        self.cat_name.setText(' ')
        self.cat_floor.setText(' ')
        self.cat_name.setText(' ')
        self.cat_floor.setText(' ')
        self.show_vendor()

    def show_vendor(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()
        self.cur.execute(''' SELECT vendor ssn FROM vendor ''')
        data = self.cur.fetchall()
        #print(data)

        if data:
            self.tableWidget_2.setRowCount(0)
            self.tableWidget_2.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_2.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1
                row_position = self.tableWidget_2.rowCount()
                self.tableWidget_2.insertRow(row_position)

    # UI Themes
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
    app = QApplication(sys.argv)
    window = login()
    window.show()
    app.exec_()
if __name__=='__main__':
    main()








