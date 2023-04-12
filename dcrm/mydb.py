import mysql.connector

dataBase = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'mysql')

cursorObj = dataBase.cursor()
cursorObj.execute("CREATE DATABASE djangoDB")
print("database created successfully :)")


