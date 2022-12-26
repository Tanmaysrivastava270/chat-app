#!c://python37/python.exe
print("content-type:text/html\r\n\r\n")

import cgi,cgitb


import mysql.connector

my=mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="batch3db"
)

mycursor=my.cursor()

sel="select * from chat"
mycursor.execute(sel)
data=mycursor.fetchall()



print("""
<html>
<head></head>

<body>
<h1>User chats</h1>
<table border="1">
                <tr>
                    <td>id</td>
                    <td>Messages</td>
                    </tr>""")
for x in data:
  print("""
                    <tr>
                    <td>%s</td>
                    <td>%s</td>
                    
  </tr>"""%(x[0],x[1]))
print("""</body>
</html>""")