#!C://python37/python.exe
print("content-type:text/html\r\n\r\n")

import cgi,cgitb

form=cgi.FieldStorage()

a=form.getvalue("id")
b=form.getvalue("opass")
c=form.getvalue("npass")
d=form.getvalue("cpass")

import mysql.connector

my=mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="batch3db"  
)


mycursor=my.cursor()

up="update usertbr set password='%s' where Email='%s'"%(c,a)
mycursor.execute(up)
my.commit()
print("<script>window.location.href='project2.py';alert('password changed')</script>")