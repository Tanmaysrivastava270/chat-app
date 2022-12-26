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
sel="select * from admin where email='%s'"%(a)
mycursor.execute(sel)
data=mycursor.fetchone()
#print("<script>window.location.href='admindashboard.py?idd=%s';alert('login successfull')</script>"%(a))
if data[1]==a:
  if data[2]==b:
    print("<script>window.location.href='admindashboard.py?idd=%s';alert('login successfull')</script>")
  else:
    print("password not match")
else:
  print("email id not match")    
