from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <head>
        <title>My Profile</title>
    </head>
    <body>
  	<h1>Welcome</h1>	
    <pre>
	Name: <i>Alvina Inayath Sha</i>
	Department: CSE
	College: <b>Saveetha Engineering College</b>	

	hello world ! 
    </pre>
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Client request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my own webserver is running successfully...")
httpd.serve_forever()