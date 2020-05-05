# import the modules
from pymysql import*
import xlwt
import pandas.io.sql as sql
# connect the mysql with the python
con = connect(user = "root", password = "DARSH1999", host = "localhost", database = "cmms")
# read the data
df = sql.read_sql('SELECT * FROM engineer', con)
# print the data
print(df)
# # export the data into the excel sheet
# df.to_excel('ds.xlsx')