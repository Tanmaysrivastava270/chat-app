#!c://python37/python.exe
print("content-type:text/html\r\n\r\n")

import cgi,cgitb
form=cgi.FieldStorage()

a=form.getvalue("name")
print(a)
b=form.getvalue("email")
print(b)
c=form.getvalue("pass")
print(c)
d=form.getvalue("mob")
print(d)

import mysql.connector
mydb=mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="batch3db"
)

mycursor=mydb.cursor()

ins="insert into usertbp(Name,Email,Password,mobile) values('%s','%s','%s','%s')"%(a,b,c,d)
mycursor.execute(ins)
ins1="insert into usertbr(email,password) values('%s','%s')"%(b,c)
mycursor.execute(ins1)
mydb.commit()
print("<script>window.location.href='project2.py';alert('registration successfull')</script>")