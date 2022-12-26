#!C://python37/python.exe
print("content-type:text/html\r\n\r\n")

import cgi,cgitb
form=cgi.FieldStorage()
sesid=form.getvalue("idd")

import mysql.connector

my=mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="batch3db"
)

mycursor=my.cursor()

sel="select * from usertbp where Email='%s'"%(sesid)
mycursor.execute(sel)
data=mycursor.fetchone()



print("""
<html>
<head>
 
</head>

<body>
<style>
body {
  background: url('dash.jpg')no-repeat;
 }
</style>
<div>
     <h1 style="color:green;"> <font size=30 </font> <b> <center> <em> <strong>DASHBOARD</strong> </em> </b> </center></h1>
    
</div>

Welcome <mark>%s</mark> to Dashboard


<input type="text" name="name" value="%s" readonly/><br/><br/>
Email<input type="email" name="email" value="%s" readonly/><br/><br/>
mobile<input type="number" name="mob" value="%s" readonly/><br/><br/>
<div>
<a href="pchangepassword.py?idd=%s">Change Password</a><br/>
<a href="plogout.py">Logout</a><br/>
<a href="pchat.py">send message</a></br>
<a href="preceiver.py">Receive message</a></br>
</div>
</body>
</html>"""%(data[1],data[1],data[2],data[4],sesid))