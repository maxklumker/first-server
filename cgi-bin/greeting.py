#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()
form = cgi.FieldStorage()
user_input = form.getvalue("fname")

print("""
<h1></h1>
""")
print("<br> <br> <br> <br> <br><hr>")
print("<h1>{}</h1>".format(user_input))



#No need for html configuration
"""
print("<html>")
print("<body>")
print("<h1>Hello {}</h1>".format(user_input))
print("</body>")
print("</html>")
"""
