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
d=form.getvalue("feedback")
print(d)


import mysql.connector
mydb=mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="batch4"
)
print("ok")
mycursor=mydb.cursor()

ins="insert into usertbc(name,email,mobile,feedback) values('%s','%s','%s','%s')"%(a,b,c,d)
mycursor.execute(ins)
mydb.commit()
print("<script>window.location.href='pp5.py';alert('data save')</script>")