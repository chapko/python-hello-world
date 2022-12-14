from http.server import BaseHTTPRequestHandler, HTTPServer
from os import environ

hostName = "0.0.0.0"
serverPort = int(environ.get("PORT", "8080"))

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"GET {self.path}")
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Hello World!</title></head>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes(f"<p>Hello World! (<code>{self.path}</code>)</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Server started http://{hostName}:{serverPort}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
