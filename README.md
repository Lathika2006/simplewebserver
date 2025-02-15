# EX01 Developing a Simple Webserver
## Date:14/02/2024

## AIM:
To develop a simple webserver to serve html pages.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Serving the HTML pages.

### Step 5:
Testing the webserver.

## PROGRAM:
```
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
<head>
<title>Software Companies</title>
</head>
<body bgcolor="sky blue">
<h1>Top Software Companies</h1>
<table border="5" cellspacing="4" cellpadding="6" height="30" width="50">
<caption>Top Five Revenue Generating Software Companies</caption>
<tr>
<th>Company</th>
<th>Revenue</th>
<th>Rank</th>
</tr>
<tr>
<td>SAP</td>
<td align="right">14232.0</td>
<td align="right">1</td>
</tr>
<tr>
<td>Dassault Systemes</td>
<td align="right">1783.5</td>
<td align="right">2</td>
</tr>
<tr>
<td>Sage</td>
<td align="right">1460.9</td>
<td align="right">3</td>
</tr>
<tr>
<td>Winccor Nixdorf</td>
<td align="right">1169.0</td>
<td align="right">4</td>
</tr>
<tr>
<td>Hexagon</td>
<td align="right">1154.0</td>
<td align="right">5</td>
</tr>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
```

## OUTPUT:
![alt text](<Screenshot 2024-03-12 112934.png>) 
![alt text](<Screenshot 2024-03-12 112836.png>)

## RESULT:
The program for implementing simple webserver is executed successfully.
