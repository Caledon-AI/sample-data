from http.server import HTTPServer, SimpleHTTPRequestHandler

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type')
        return super(CORSRequestHandler, self).end_headers()

if __name__ == '__main__':
    httpd = HTTPServer(('localhost', 8000), CORSRequestHandler)
    print("Serving on port 8000")
    httpd.serve_forever()