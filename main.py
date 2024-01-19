from http.server import HTTPServer ,BaseHTTPRequestHandler ,SimpleHTTPRequestHandler,ThreadingHTTPServer
import time
HOST = "192.168.29.147"#Your IP address "INTERNAL" not Public
PORT = 1024 #"Your Desired Port "
class HTTP(BaseHTTPRequestHandler):

        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-type","text/html")
            self.end_headers()
            webpage="<html><body><h1>Hello SERVER THIS IS ME YOUR BOSS NOW GIVE ME THAT DAMN MONEY</h1></body></html>"
            self.wfile.write(bytes(webpage,"utf-8"))


        def do_POST(self):
            self.send_response(200)
            self.send_header("Content-type","application/json")
            self.end_headers()

            date=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
            self.wfile.write(bytes('{"time": "' + date + '"}' ,"utf-8"))

server = HTTPServer((HOST, PORT), HTTP)
print("server is loading files for you u want to have some coffee ?")
server.server_activate()
try:
    while True:
        user_input = input("Enter 'c' to close the server: ")
        if user_input.lower() == 'c':
            break
except KeyboardInterrupt:
    pass

print("Closing the server.")
server.server_close()
