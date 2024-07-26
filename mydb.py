import mysql
import mysql.connector

dataBase = mysql.connector.connect(host = "localhost", user = "root", password = "milu")

#Make a cursor object

cursorObject = dataBase.cursor()

#Create the batabase

cursorObject.execute("CREATE DATABASE my_database")

print("Perfect!")