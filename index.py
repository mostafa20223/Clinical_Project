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

        self.cur.execute(''' SELECT * FROM users ''')
        data = self.cur.fetchall()
        for row in data:
            if username == row[1] and password == row[3]:
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

        self.show_cmms()
        self.show_category_combobox()
        self.show_engineer_combobox()
        self.show_vendor_combobox()

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
        self.view_cat_btn.clicked.connect(self.show_category)
        self.edit_cat_btn.clicked.connect(self.Edit_category)
        self.dark_orange.clicked.connect(self.Dark_orange_theme)
        self.dark_blue.clicked.connect(self.Dark_blue_Theme)
        self.dark_grey.clicked.connect(self.Dark_gray_theme)
        self.dark.clicked.connect(self.qdark_theme)
        self.add_user_btn.clicked.connect(self.Add_new_user)
        self.user_login_btn.clicked.connect(self.login)
        self.edit_user_btn.clicked.connect(self.Edit_user)
        self.add_equip_btn.clicked.connect(self.Add_equipment)
        self.view_equip_btn.clicked.connect(self.show_equipment)
        self.del_equip_btn.clicked.connect(self.delete_equipment)
        self.add_eng_btn.clicked.connect(self.Add_engineer)
        self.view_eng_btn.clicked.connect(self.show_engineer)
        self.edit_eng_btn.clicked.connect(self.Edit_engineer)
        self.add_vendor_btn.clicked.connect(self.Add_vendor)
        self.view_vendor_btn.clicked.connect(self.show_vendor)
        #self.edit_vendor_btn.clicked.connect(self.Edit_vendor)

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
                self.EditUser.setEnabled(True)
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

    # cmms
    def show_cmms(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()
        self.cur.execute(''' SELECT serial_number, equipment_name, equipment_code, work_time, insurance, maintenance, price, cat_name, ssn, eng_name, eng_phone, eng_email
        FROM equipment
        INNER JOIN category ON cat_name = name
        INNER JOIN engineer ON equip_sn = serial_number ''')
        data = self.cur.fetchall()
        #print(data)

        if data:
            self.cmms_table.setRowCount(0)
            self.cmms_table.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.cmms_table.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1
                row_position = self.cmms_table.rowCount()
                self.cmms_table.insertRow(row_position)    

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
        self.show_category()

    def show_category(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()
        self.cur.execute(''' SELECT * FROM category ''')
        data = self.cur.fetchall()

        if data:
            self.category_table.setRowCount(0)
            self.category_table.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.category_table.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1
                row_position = self.category_table.rowCount()
                self.category_table.insertRow(row_position)

    def Edit_category(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()
        current_cat_name = self.cat_name0.text()
        current_cat_floor = self.cat_floor0.text()
        new_cat_name = self.cat_name1.text()
        new_cat_floor = self.cat_floor1.text()
        self.cur.execute(''' UPDATE category SET name = %s, floor = %s WHERE name = %s '''
                             , (new_cat_name, new_cat_floor, current_cat_name))
        self.db.commit()
        self.statusBar().showMessage('Category updated successfully')
        self.show_category()

    # Show Category in UI
    def show_category_combobox(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()
        self.cur.execute(''' SELECT name FROM category ''')
        data = self.cur.fetchall()
        for category in data:
            self.category_combo.addItem(category[0])

    # Equipment
    def Add_equipment(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()
        sn = self.equip_sn.text()
        equip_name = self.equip_name.text()
        equip_code = self.equip_code.text()
        equip_wt = self.equip_wt.text()
        equip_ins = self.equip_ins.text()
        equip_main = self.equip_main.text()
        equip_price = self.equip_price.text()
        equip_category = self.equip_catname.text()
        self.cur.execute(''' INSERT INTO equipment (serial_number, equip name, eng phone, eng email) VALUES (%s, %s, %s, %s) '''
                         , (ssn, eng_name, eng_phone, eng_email))
        self.db.commit()
        self.statusBar().showMessage('New Equipment Added')
        self.show_equipment()

    def show_equipment(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()
        self.cur.execute(''' SELECT * FROM equipment ''')
        data = self.cur.fetchall()

        if data:
            self.equipment_table.setRowCount(0)
            self.equipment_table.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.equipment_table.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1
                row_position = self.equipment_table.rowCount()
                self.equipment_table.insertRow(row_position)

    def delete_equipment(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()
        equipment_code = self.equip_code0.text()
        self.cur.execute(''' DELETE FROM equipment WHERE equipment_code = %s '''
                         , equipment_code)
        self.db.commit()
        self.show_equipment()

    # Engineer
    def Add_engineer(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()
        ssn = self.eng_ssn.text()
        eng_name = self.eng_name.text()
        eng_phone = self.eng_phone.text()
        eng_email = self.eng_mail.text()

        self.cur.execute(''' INSERT INTO engineer (ssn, eng_name, eng_phone, eng_email) VALUES (%s, %s, %s, %s) '''
                         , (ssn, eng_name, eng_phone, eng_email))
        self.db.commit()
        self.statusBar().showMessage('New Engineer Added')
        self.show_engineer()

    def show_engineer(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()
        self.cur.execute(''' SELECT * FROM engineer ''')
        data = self.cur.fetchall()

        if data:
            self.eng_table.setRowCount(0)
            self.eng_table.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.eng_table.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1
                row_position = self.eng_table.rowCount()
                self.eng_table.insertRow(row_position)

    def Edit_engineer(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()
        current_name = self.eng_name0.text()
        current_ssn = self.eng_ssn0.text()
        current_phone = self.eng_phone0.text()
        current_email = self.eng_mail0.text()
        new_name = self.eng_name1.text()
        new_ssn = self.eng_ssn1.text()
        new_phone = self.eng_phone1.text()
        new_email = self.eng_mail1.text()
        self.cur.execute(''' UPDATE engineer SET ssn = %s, eng_name = %s, eng_phone = %s, eng_email = %s WHERE ssn = %s '''
                             , (new_ssn, new_name, new_phone, new_email, current_ssn))
        self.db.commit()
        self.statusBar().showMessage('Engineer updated successfully')
        self.show_engineer()
        
    def show_engineer_combobox(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()
        self.cur.execute(''' SELECT ssn FROM engineer ''')
        data = self.cur.fetchall()
        for engineer in data:
            self.eng_combo.addItem(engineer[0])

    # Vendor
    def Add_vendor(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()
        vendor_name = self.vendor_name.text()
        vendor_ssn = self.vendor_ssn.text()
        vendor_phone = self.vendor_phone.text()
        vendor_email = self.vendor_mail.text()
        self.cur.execute(''' INSERT INTO vendor (vendor_ssn, vendor_name, vendor_phone, vendor_email) VALUES (%s, %s, %s, %s) '''
                         , (vendor_ssn, vendor_name, vendor_phone, vendor_email))
        self.db.commit()
        self.statusBar().showMessage('New Vendor Added')
        self.show_vendor()

    def show_vendor(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()
        self.cur.execute(''' SELECT * FROM vendor ''')
        data = self.cur.fetchall()

        if data:
            self.vendor_table.setRowCount(0)
            self.vendor_table.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.vendor_table.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1
                row_position = self.vendor_table.rowCount()
                self.vendor_table.insertRow(row_position)

    def show_vendor_combobox(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()
        self.cur.execute(''' SELECT vendor_ssn FROM vendor ''')
        data = self.cur.fetchall()
        for vendor in data:
            self.vendor_combo.addItem(vendor[0])

    # UI Themes
    def Dark_blue_Theme(self):
        style = open('themes/darkblue.css', 'r')
        style = style.read()
        self.setStyleSheet(style)
    def Dark_gray_theme(self):
        style = open('themes/darkgray.css', 'r')
        style = style.read()
        self.setStyleSheet(style)
    def Dark_orange_theme(self):
        style = open('themes/darkorange.css', 'r')
        style = style.read()
        self.setStyleSheet(style)
    def qdark_theme(self):
        style = open('themes/qdark.css', 'r')
        style = style.read()
        self.setStyleSheet(style)

def main():
    app = QApplication(sys.argv)
    window = login()
    window.show()
    app.exec_()
if __name__=='__main__':
    main()

#INSERT INTO cmms.equipment
#(serial_number, equipment_name, equipment_code, work_time, insurance, maintenance, price, cat_name)
#VALUES
#("E2", "Monitor", "0001", "2020-03-23", "2020-06-20", "2020-04-20", "1500", "ICU");

#SELECT serial_number, equipment_name, equipment_code, work_time, insurance, maintenance, price, cat_name
#FROM cmms.equipment
#INNER JOIN cmms.category ON cat_name = name;

#DELETE FROM table_name WHERE condition;