#!c://python37/python.exe
print("content-type:text/html\r\n\r\n")

print("""<html>
    <head>
        
    </head>
    <body>
    <style>
body {
  background-image: url('reis.jpg');
}
</style>


<div style="float:left;width:75%">
 <center> <h1 style="padding-left:50px"><i><u> <font size="10 color="purple" face ="AlGERIAN"><b>Connect individuals and communities to reduce social isolation</i>&emsp;</u></font></h1></center>
</div>
</div>

<div style="float:left;width:70%">
<br/><br/><br/>
<h1>REGISTRATION</h1>
<form action="pp2.py" method="post">

 name<input type="text" name="name"/><br/><br/>
email<input type="email" name="email"/><br/><br/>
password<input type="password" name="pass"/><br/><br/>
 mobile<input type="number" name="mob"/><br/><br/>
 
 <button>Submit</button>
</div>
</form>
<div style="float:left;width:30%">
<br/><br/><br/>
<h1>LOGIN</h1>
<form action="pp3.py" method="post">
 
email<input type="email" name="email"/><br/><br/>

  password<input type="password" name="pass"/><br/><br/>
 
 <button>LOGIN</button>
</div>
 </body>
 </form>
 <footer style="text-align:center;">
 <div>
 <h2 style="color:blue;"> Web Designed By Tanmay</h2>
 </div>
</footer> 
 </html>""")