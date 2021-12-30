# Goals:
# Create a guessing game
# Run a web server and host a web page - UI
# Accept a user name and user's guess - server
# Generate a random number - server
# Show the result - UI

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import random

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def _html(self, args):
      content = "<html><body>"
      #content = "<html><body><h1>Hello A.K.</h1></html></body>"
      F = open("008.html", "r")
      
      #declaring a new 'content' and we will add the content = "<html><body>" and concatenate with F.read()
      content = content + F.read()

      F.close()
      if len(args) == 2:
         guess = int(args["guess"][0])
         r = random.randint(1, 100)
         if r is range(guess-5, guess+5):
           content = content + "<h2>"+args["name"][0] + " " + str(guess) + " " + str(r) + " " + "WIN!</h2>"
         else:
           content = content + "<h2>"+args["name"][0] + " " + str(guess) + " " + str(r) + " " + "LOOSE!</h2>"
      content = content + "</body></html>"
      return content.encode("utf8")

    def do_GET(self):
        self._set_headers()
        args = parse_qs(urlparse(self.path).query)
        self.wfile.write(self._html(args))

#Copied and pasted from internet - python library.
#Defining the function 'run'
#THIS will RUN The HTTP Server service
def run(server_class=HTTPServer, handler_class=S, addr="localhost", port=8000):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)

    print(f"Starting httpd server on {addr}:{port}")
    httpd.serve_forever()

#Call the function run() to start the function
run()

