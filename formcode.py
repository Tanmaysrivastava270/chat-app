#!c://python37/python.exe
print("content-type:text/html\r\n\r\n")

import cgi,cgitb
form=cgi.FieldStorage()

a=form.getvalue("name")
print(a)
b=form.getvalue("email")
print(b)
c=form.getvalue("mob")
print(c)

import mysql.connector
mydb=mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="batch2db"
)
print("ok")
mycursor=mydb.cursor()

ins="insert into usertbt(name,email,mobile) values('%s','%s','%s')"%(a,b,c)
mycursor.execute(ins)
mydb.commit()
print("<script>window.location.href='form.py';alert('data save')</script>")