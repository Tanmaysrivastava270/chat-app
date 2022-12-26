#!c://python37/python.exe
print("content-type:text/html\r\n\r\n")

print("""<html>
    <head>
    </head/>
    <body>
    <h1>Admin login</h1>
    <form action="padminlogincode.py" method="post">
    <div style="float:left;width:70%">
    <br/><br/><br/>

    <input type="email" name="email"placeholder="email"/><br/><br/>
<input type="password" name="pass"placeholder="password"/><br/><br/>
<button>Login</button>
</form>
</div>
</body>
</html""")