#!c://python37/python.exe
print("content-type:text/html\r\n\r\n")

import cgi,cgitb
form=cgi.FieldStorage()


a=form.getvalue("rcvmsg")

import mysql.connector
mydb=mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="batch3db"
)

mycursor=mydb.cursor()

ins="insert into chat(receivermessage) values('%s')"%(a)
mycursor.execute(ins)
mydb.commit()
print("<script>window.location.href='preceiver.py';alert('send successfull')</script>")