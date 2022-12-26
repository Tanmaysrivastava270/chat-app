#!C://python37/python.exe
print("content-type:text/html\r\n\r\n")
import cgi,cgitb
form=cgi.FieldStorage()
sesid=form.getvalue("idd")

print("""
<html>
<head></head>
<body>
<style>
body {
  background: url('passw.png')no-repeat;
  
 }
</style>

<h1>Change Password</h1>
<form action="pchangepasscode.py" method="post">
<input type="hidden" name="id" value="%s">
Old Password<input type="password" name="opass"></input><br/><br/>
New Password<input type="password" name="npass"></input><br/><br/>
Confirm Password<input type="password" name="cpass"></input><br/><br/>
<button>Change</button>
</form>
</body>
 <footer style="text-align:center;">
 
</footer> 

</html>"""%(sesid))