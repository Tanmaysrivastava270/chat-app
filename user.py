#!C://python37/python.exe
print("content-type:text/html\r\n\r\n")

print("""
<html>
<head>

</head>

<body>
<h1>user registration</h1>
<form action="usercode.py" method ="post">
name<input type="text" name="name"/><br/>
email<input type="email" name="email"/><br/>
password<input type="password" name="password"/><br/>
<button>submit</button>
</form>
</body>
</html>
""")