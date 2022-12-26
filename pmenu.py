#!C://python37/python.exe
print("content-type:text/html\r\n\r\n")
print("""
<html>
    <head>
      
    <style>
    *
    {
    margin:0px;
    padding:0px;
    }
    ul{
    list-style-type:none;
    }
    ul li{
    height:50px;
    width:218px;
    background: pink;
    float:left;
    text-align:center;
    
    
    }
    ul li a{
    text-decoration:none;
    line-height:50px;
    
    font-size:25px;
    font-weight:bold;
    color:orange;
    }
     ul li a:hover
     {
     background:green;
     color:yellow;
     display:block;
}     
    </style>
    
    
    </head>
    
    
    <body>
    
<ul>
   
    <li><a href="pabout.py">About</a></li>
    <li><a href="pp5.py">Contact</a></li>
    <li><a href="project2.py">Registration</a></li>
    <li><a href="project2.py">Login</a></li>
    <li><a href="pchangepassword.py">Changepassword</a></li>
    </ul>
    <style>
body {
  background-image: url('banner.png');
}
</style>

    <div>
     <h1 style="color:blue;"> <font size=30 </font> <b> <center> <em> <strong>SECRET</strong> </em> </b> </center></h1>
    
    <h2 style="color:green;"> <font size=5 </font> <center>Connect the world globally with our loyal service</center></h2>
   </div>

    
    </body>
    
    </html>""")