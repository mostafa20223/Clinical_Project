from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from pymysql import *
import pandas.io.sql as sql
import sys, xlwt, qdarkstyle, mysql.connector
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
        self.Handel_buttons()
        self.show_cmms()
        self.show_category_combobox()
        self.show_equipmentSN_combobox()
        self.show_equipmentName_combobox()
        self.show_equipmentCode_combobox()
        self.show_vendorSSN_combobox()
        self.show_error_combobox()
    
    def Handel_buttons(self):
        self.tabWidget.tabBar().setVisible(False)
        self.cmms_tab.clicked.connect(self.open_cmms_tab)
        self.equipment_tab.clicked.connect(self.open_equipment_tab)
        self.user_tab.clicked.connect(self.open_users_tab)
        self.more_info_tab.clicked.connect(self.open_info_tab)
        self.tracking_tab.clicked.connect(self.open_tracking_tab)
        self.reports_tab.clicked.connect(self.open_report_tab)

        self.add_cat_btn.clicked.connect(self.Add_category)
        self.view_cat_btn.clicked.connect(self.show_category)
        self.edit_cat_btn.clicked.connect(self.Edit_category)

        self.add_user_btn.clicked.connect(self.Add_new_user)
        self.user_login_btn.clicked.connect(self.login)
        self.edit_user_btn.clicked.connect(self.Edit_user)

        self.add_equip_btn.clicked.connect(self.Add_equipment)
        self.view_equip_btn.clicked.connect(self.show_equipment)
        self.view_equip_btn0.clicked.connect(self.show_equipment)
        self.del_equip_btn.clicked.connect(self.delete_equipment)
        self.edit_equip_btn.clicked.connect(self.Edit_equipment)

        self.add_eng_btn.clicked.connect(self.Add_engineer)
        self.view_eng_btn.clicked.connect(self.show_engineer)
        self.edit_eng_btn.clicked.connect(self.Edit_engineer)

        self.add_vendor_btn.clicked.connect(self.Add_vendor)
        self.view_vendor_btn.clicked.connect(self.show_vendor)
        self.edit_vendor_btn.clicked.connect(self.Edit_vendor)

        self.add_ppm_btn.clicked.connect(self.Add_ppm)
        self.view_ppm_btn0.clicked.connect(self.show_ppm)
        self.category_combo0.currentTextChanged.connect(self.show_ppm_combo)
        self.ppm_save_btn.clicked.connect(self.save_ppm)

        self.add_repair_btn.clicked.connect(self.Add_repair)
        self.view_repair_btn0.clicked.connect(self.show_repair)
        self.category_combo1.currentTextChanged.connect(self.show_repair_combo)
        self.repair_save_btn.clicked.connect(self.save_repair)

        self.add_installation_btn.clicked.connect(self.Add_installation)
        self.view_inst_btn0.clicked.connect(self.show_installation)
        self.category_combo2.currentTextChanged.connect(self.show_installation_combo)
        self.inst_save_btn.clicked.connect(self.save_installation)

    # TABS
    def open_cmms_tab(self):
        self.tabWidget.setCurrentIndex(0)
    def open_equipment_tab(self):
        self.tabWidget.setCurrentIndex(1)
    def open_users_tab(self):
        self.tabWidget.setCurrentIndex(2)
    def open_info_tab(self):
        self.tabWidget.setCurrentIndex(3)
    def open_tracking_tab(self):
        self.tabWidget.setCurrentIndex(4)        
    def open_report_tab(self):
        self.tabWidget.setCurrentIndex(5)

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
            self.statusBar().showMessage('Please add a valid password twice')

    def login(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()
        username = self.access_user.text()
        password = self.access_pass.text()

        self.cur.execute(''' SELECT * FROM users ''')
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
        self.cur.execute(''' SELECT serial_number, equipment_name, equipment_code, portable, work_time, insurance, maintenance, price, cat_name
        FROM equipment
        FULL JOIN category ON cat_name = name
        ORDER BY serial_number ''')
        data = self.cur.fetchall()

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
        self.show_category_combobox()

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
        self.show_category_combobox()

    # Show Category in UI
    def show_category_combobox(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()
        self.cur.execute(''' SELECT name FROM category ''')
        data = self.cur.fetchall()
        for category in data:
            self.category_combo0.addItem(category[0])
            self.category_combo1.addItem(category[0])
            self.category_combo2.addItem(category[0])
            self.category_combo3.addItem(category[0])
            self.category_combo4.addItem(category[0])
            self.category_combo5.addItem(category[0])
            self.category_add.addItem(category[0])
            self.category_edit0.addItem(category[0])

    # Equipment
    def Add_equipment(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()
        sn = self.equip_sn.text()
        equip_name = self.equip_name.text()
        equip_code = self.equip_code.text()
        portable = self.portable_combo.currentText()
        equip_wt = self.equip_wt.text()
        equip_ins = self.equip_ins.text()
        equip_main = self.equip_main.text()
        equip_price = self.equip_price.text()
        equip_category = self.category_add.currentText()
        self.cur.execute(''' INSERT INTO equipment (serial_number, equipment_name, equipment_code, portable, work_time, insurance, maintenance, price, cat_name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) '''
                         , (sn, equip_name, equip_code, portable, equip_wt, equip_ins, equip_main, equip_price, equip_category))
        self.db.commit()
        self.statusBar().showMessage('New Equipment Added')
        self.show_equipment()
        self.show_equipmentSN_combobox()
        self.show_equipmentName_combobox()
        self.show_equipmentCode_combobox()

    def show_equipment(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()
        self.cur.execute(''' SELECT * FROM equipment ''')
        data = self.cur.fetchall()

        if data:
            self.equipment_table.setRowCount(0)
            self.equipment_table.insertRow(0)
            self.equipment_table0.setRowCount(0)
            self.equipment_table0.insertRow(0)            
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.equipment_table.setItem(row, column, QTableWidgetItem(str(item)))
                    self.equipment_table0.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1
                row_position = self.equipment_table.rowCount()
                self.equipment_table.insertRow(row_position)
                row_position0 = self.equipment_table0.rowCount()
                self.equipment_table0.insertRow(row_position0)                

    def delete_equipment(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()
        sql = "DELETE FROM equipment WHERE serial_number = %s"
        adr = (self.equip_sn3.text(), )
        self.cur.execute(sql, adr)
        self.db.commit()
        self.statusBar().showMessage('Equipment Deleted')
        self.show_equipment()
        self.show_equipmentSN_combobox()
        self.show_equipmentName_combobox()
        self.show_equipmentCode_combobox()        

    def Edit_equipment(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()
        current_sn = self.equip_sn0.text()
        new_sn = self.equip_sn1.text()
        new_equip_name = self.equip_name1.text()
        new_equip_code = self.equip_code2.text()
        new_portable = self.portable_combo1.currentText()
        new_equip_wt = self.equip_wt1.text()
        new_equip_ins = self.equip_ins1.text()
        new_equip_main = self.equip_main1.text()
        new_equip_price = self.equip_price1.text()
        new_equip_category = self.category_edit0.currentText()        
        self.cur.execute(''' UPDATE equipment SET serial_number = %s, equipment_name = %s, equipment_code = %s, portable = %s, work_time = %s, insurance = %s, maintenance = %s, price = %s, cat_name = %s WHERE serial_number = %s '''
                             , (new_sn, new_equip_name, new_equip_code, new_portable, new_equip_wt, new_equip_ins, new_equip_main, new_equip_price, new_equip_category, current_sn))
        self.db.commit()
        self.statusBar().showMessage('Equipment updated successfully')
        self.show_equipment()
        self.show_equipmentSN_combobox()
        self.show_equipmentName_combobox()
        self.show_equipmentCode_combobox()        

    # Show Equipment Serial Number in UI
    def show_equipmentSN_combobox(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()
        self.cur.execute(''' SELECT serial_number FROM equipment ''')
        data = self.cur.fetchall()
        for e_sn in data:
            self.equipsn_combo.addItem(e_sn[0])
            self.equipsn_combo0.addItem(e_sn[0])
            self.equipsn_combo1.addItem(e_sn[0])
            self.equipsn_combo2.addItem(e_sn[0])

    # Show Equipment Name in UI
    def show_equipmentName_combobox(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()
        self.cur.execute(''' SELECT equipment_name FROM equipment ''')
        data = self.cur.fetchall()
        for e_sn in data:
            self.equipname_combo.addItem(e_sn[0])
            self.equipname_combo0.addItem(e_sn[0])
            self.equipname_combo1.addItem(e_sn[0])

    # Show Equipment Code in UI
    def show_equipmentCode_combobox(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()
        self.cur.execute(''' SELECT equipment_code FROM equipment ''')
        data = self.cur.fetchall()
        for e_sn in data:
            self.equipcode_combo.addItem(e_sn[0])
            self.equipcode_combo0.addItem(e_sn[0])
            self.equipcode_combo1.addItem(e_sn[0])

    # Engineer
    def Add_engineer(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()
        ssn = self.eng_ssn.text()
        eng_name = self.eng_name.text()
        eng_phone = self.eng_phone.text()
        eng_email = self.eng_mail.text()
        equip_serialnumber = self.equipsn_combo.currentText()
        vendor_ssn = self.vendorssn_combo.currentText()

        self.cur.execute(''' INSERT INTO engineer (ssn, eng_name, eng_phone, eng_email, equip_sn, v_ssn) VALUES (%s, %s, %s, %s, %s, %s) '''
                         , (ssn, eng_name, eng_phone, eng_email, equip_serialnumber, vendor_ssn))
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
        current_ssn = self.eng_ssn0.text()
        new_name = self.eng_name1.text()
        new_ssn = self.eng_ssn1.text()
        new_phone = self.eng_phone1.text()
        new_email = self.eng_mail1.text()
        self.cur.execute(''' UPDATE engineer SET ssn = %s, eng_name = %s, eng_phone = %s, eng_email = %s WHERE ssn = %s '''
                             , (new_ssn, new_name, new_phone, new_email, current_ssn))
        self.db.commit()
        self.statusBar().showMessage('Engineer updated successfully')
        self.show_engineer()

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
        self.show_vendorSSN_combobox()

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

    def Edit_vendor(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()
        current_ssn = self.vendor_ssn0.text()
        new_name = self.vendor_name1.text()
        new_ssn = self.vendor_ssn1.text()
        new_phone = self.vendor_phone1.text()
        new_email = self.vendor_mail1.text()
        self.cur.execute(''' UPDATE vendor SET vendor_ssn = %s, vendor_name = %s, vendor_phone = %s, vendor_email = %s WHERE vendor_ssn = %s '''
                             , (new_ssn, new_name, new_phone, new_email, current_ssn))
        self.db.commit()
        self.statusBar().showMessage('Vendor updated successfully')
        self.show_vendor()
        self.show_vendorSSN_combobox()

    # Show Vendor SSN in UI
    def show_vendorSSN_combobox(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()
        self.cur.execute(''' SELECT vendor_ssn FROM vendor ''')
        data = self.cur.fetchall()
        for v_ssn in data:
            self.vendorssn_combo.addItem(v_ssn[0])

    def Add_ppm(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()
        equip_sn = self.equipsn_combo0.currentText()
        equip_name = self.equipname_combo.currentText()
        equip_code = self.equipcode_combo.currentText()
        category_name = self.category_combo3.currentText()
        tech_name = self.tech_name.text()
        ppm_time = self.ppm_time.text()
        ppm_year = self.ppm_year.text()
        error = self.error_combo.currentText()
        self.cur.execute(''' INSERT INTO equipment_ppm (EQU_SN, EQU_NAME, EQU_CODE, CATEGORY, technician_name, ppm_time, ppm_year, ERROR) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) '''
                         , (equip_sn, equip_name, equip_code, category_name, tech_name, ppm_time, ppm_year, error))
        self.db.commit()
        self.statusBar().showMessage('New PPM Added')
        self.show_ppm()

    def show_ppm(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()
        self.cur.execute(''' SELECT * FROM equipment_ppm ''')
        data = self.cur.fetchall()

        if data:
            self.ppm_table0.setRowCount(0)
            self.ppm_table0.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.ppm_table0.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1
                row_position = self.ppm_table0.rowCount()
                self.ppm_table0.insertRow(row_position)

    def show_ppm_combo(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()
        sql = "SELECT EQU_SN, EQU_Name, EQU_Code, CATEGORY, technician_name, ppm_time, ppm_year, ERROR FROM equipment_ppm JOIN equipment ON CATEGORY = cat_name WHERE CATEGORY = %s GROUP BY EQU_SN;"
        adr = (self.category_combo0.currentText(), )
        self.cur.execute(sql, adr)
        data = self.cur.fetchall()

        if data:
            self.ppm_table.setRowCount(0)
            self.ppm_table.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.ppm_table.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1
                row_position = self.ppm_table.rowCount()
                self.ppm_table.insertRow(row_position)

    def save_ppm(self):
        self.remove_ppm()
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()        
        sql_add = "INSERT INTO ppm_save SELECT EQU_SN, EQU_Name, EQU_Code, CATEGORY, technician_name, ppm_time, ppm_year, ERROR FROM equipment_ppm JOIN equipment ON CATEGORY = cat_name WHERE CATEGORY = %s GROUP BY EQU_SN;"
        adr = (self.category_combo0.currentText(), )
        self.cur.execute(sql_add, adr)
        df = sql.read_sql('SELECT * FROM ppm_save', self.db)
        print(df)
        df.to_excel('F:/Ubuntu/Clinical_Project/Reports/PPM/ppm.xlsx')

    def remove_ppm(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()  
        self.cur.execute(''' TRUNCATE TABLE ppm_save ''')

    def Add_repair(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()
        equip_sn = self.equipsn_combo1.currentText()
        equip_name = self.equipname_combo0.currentText()
        equip_code = self.equipcode_combo0.currentText()
        cat_name = self.category_combo4.currentText()
        tech_name = self.tech_name0.text()
        error = self.error.text()
        fixed = self.fixed_combo.currentText()
        repair_time = self.repair_time.text()
        repair_type = self.repair_type.text()
        cost = self.repair_cost.text()
        self.cur.execute(''' INSERT INTO equipment_repair (equip_serial, equip_name, equip_code, Categ_Name, error, fixed, technician_name, repair_time, repair_type, cost) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) '''
                         , (equip_sn, equip_name, equip_code, cat_name, error, fixed, tech_name, repair_time, repair_type, cost))
        self.db.commit()
        self.statusBar().showMessage('New Repair Added')
        self.show_repair()
        self.show_error_combobox()

    def show_repair(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()
        self.cur.execute(''' SELECT * FROM equipment_repair ''')
        data = self.cur.fetchall()

        if data:
            self.repair_table0.setRowCount(0)
            self.repair_table0.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.repair_table0.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1
                row_position = self.repair_table0.rowCount()
                self.repair_table0.insertRow(row_position)

    def show_repair_combo(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()
        sql = "SELECT equip_serial, equip_name, equip_code, Categ_Name, error, fixed, technician_name, repair_time, repair_type, cost FROM equipment_repair JOIN equipment ON Categ_Name = cat_name WHERE Categ_Name = %s GROUP BY equip_serial;"
        adr = (self.category_combo1.currentText(), )
        self.cur.execute(sql, adr)
        data = self.cur.fetchall()

        if data:
            self.repair_table.setRowCount(0)
            self.repair_table.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.repair_table.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1
                row_position = self.repair_table.rowCount()
                self.repair_table.insertRow(row_position)

    def save_repair(self):
        self.remove_repair()
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()        
        sql_add = "INSERT INTO repair_save SELECT equip_serial, equip_name, equip_code, Categ_Name, error, fixed, technician_name, repair_time, repair_type, cost FROM equipment_repair JOIN equipment ON Categ_Name = cat_name WHERE Categ_Name = %s GROUP BY equip_serial;"
        adr = (self.category_combo1.currentText(), )
        self.cur.execute(sql_add, adr)
        df = sql.read_sql('SELECT * FROM repair_save', self.db)
        print(df)
        df.to_excel('F:/Ubuntu/Clinical_Project/Reports/Repair/repair.xlsx')

    def remove_repair(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()  
        self.cur.execute(''' TRUNCATE TABLE repair_save ''')

    # Show Error in UI
    def show_error_combobox(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()
        self.cur.execute(''' SELECT error FROM equipment_repair ''')
        data = self.cur.fetchall()
        for error in data:
            self.error_combo.addItem(error[0])

    def Add_installation(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()
        equip_sn = self.equipsn_combo2.currentText()
        equip_name = self.equipname_combo1.currentText()
        equip_code = self.equipcode_combo1.currentText()
        cat_name = self.category_combo5.currentText()
        tech_name = self.tech_name1.text()
        inst_time = self.inst_time.text()
        equip_model = self.equip_model.text()
        self.cur.execute(''' INSERT INTO equipment_installation (Equ_SN, Equ_Name, Equ_Code, catName, techName, installation_time, equipment_model) VALUES (%s, %s, %s, %s, %s, %s, %s) '''
                         , (equip_sn, equip_name, equip_code, cat_name, tech_name, inst_time, equip_model))
        self.db.commit()
        self.statusBar().showMessage('New Installation Added')
        self.show_installation()

    def show_installation(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()
        self.cur.execute(''' SELECT * FROM equipment_installation ''')
        data = self.cur.fetchall()

        if data:
            self.inst_table0.setRowCount(0)
            self.inst_table0.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.inst_table0.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1
                row_position = self.inst_table0.rowCount()
                self.inst_table0.insertRow(row_position)

    def show_installation_combo(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()
        sql = "SELECT Equ_SN, Equ_Name, Equ_Code, catName, techName, installation_time, equipment_model FROM equipment_installation JOIN equipment ON catName = cat_name WHERE catName = %s GROUP BY Equ_SN;"
        adr = (self.category_combo2.currentText(), )
        self.cur.execute(sql, adr)
        data = self.cur.fetchall()

        if data:
            self.inst_table.setRowCount(0)
            self.inst_table.insertRow(0)
            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.inst_table.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1
                row_position = self.inst_table.rowCount()
                self.inst_table.insertRow(row_position)

    def save_installation(self):
        self.remove_installation()
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()        
        sql_add = "INSERT INTO installation_save SELECT Equ_SN, Equ_Name, Equ_Code, catName, techName, installation_time, equipment_model FROM equipment_installation JOIN equipment ON catName = cat_name WHERE catName = %s GROUP BY Equ_SN;"
        adr = (self.category_combo2.currentText(), )
        self.cur.execute(sql_add, adr)
        df = sql.read_sql('SELECT * FROM installation_save', self.db)
        print(df)
        df.to_excel('F:/Ubuntu/Clinical_Project/Reports/Installation/installation.xlsx')

    def remove_installation(self):
        self.db = mysql.connector.connect(host = 'localhost', user = 'root', password = 'DARSH1999', db = 'cmms')
        self.cur = self.db.cursor()  
        self.cur.execute(''' TRUNCATE TABLE installation_save ''')

def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    window = login()
    window.show()
    app.exec_()
if __name__ == '__main__':
    main()