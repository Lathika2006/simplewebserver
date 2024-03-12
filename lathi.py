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