from doctest import master

import mysql.connector

print("Hi")
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="P!OP2432DSA(&^$"
)

print("mydb")
master.shutdown