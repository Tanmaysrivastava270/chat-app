#!C://python37/python.exe
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

print("""<html>
    <head>
    
    <style>
    #main{
    border:1px solid;
    height:auto;
    width:300px;
    
    }
     #a{
    margin-top:250;
    border:1px solid;
    height:auto;
    width:300px;
    float:left;
    margin-top:1px;
    
    
    }
   
    
   
    #a1{
    
      height:auto;
      width:100px;
      border-left:1px solid;
      float:right;
      
    }  
#b{
  height:auto;
  width:195px;
  float:left;
}    
    
       </style>
       </head/>
    <body style="background-color:lightblue;">
    <style>
body {
  background: url('sms.jpg')no-repeat;
 }
</style>
    <div>
     <h1 style="color:maroon;"> <em><strong>SENDER</strong> </em> </h1>
    
</div>
   
    
    <div id="main" style="text-align:right">""")
for x in data:
  print("<span style='color:white;float:left;'>"+x[1]+"</span>"+"<br/>")
  print(x[2]+"<br/>")
print("""
    <div id="a">
    
    
    <div id="b">
    <form action="Psendcode.py" method="post">
    <input type="text" name="sendermessage" placeholder="message"/><br/><br/>
    
    </div>
       <div id="a1">
       <button>Send </button>
       </div>
    </div>
    </div>

    </body>
</html>""")
    