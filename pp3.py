#!c://python37/python.exe
print("content-type:text/html\r\n\r\n")

import cgi,cgitb
form=cgi.FieldStorage()

a=form.getvalue("email")

b=form.getvalue("pass")


import mysql.connector
mydb=mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="batch3db"
)
mycursor=mydb.cursor()
sel="select * from usertbr where Email='%s'"%(a)
mycursor.execute(sel)
data=mycursor.fetchone()


if data==None: 
  print("<script>window.location.href='project2.py';alert('email not match')</script>")
else:
  if data[2]==b:
    print("<script>window.location.href='pdashboard.py?idd=%s';alert('login successfull')</script>"%(a))
  else:
    print("<script>window.location.href='project2.py';alert('password not match')</script>")    
