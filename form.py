#!C://python37/python.exe
print("content-type:text/html\r\n\r\n")



print("""
<html>
<head></head>
<body>
<h1>Form</h1>

<form action="formcode.py" method="post">

name<input type="text" name="name"/><br/><br/>
email<input type="email" name="email"/><br/><br/>
mobile<input type="number" name="mob"/><br/><br/>

<button>Submit</button>



</form>

</body>
 
</html>""")