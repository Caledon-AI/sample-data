import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type')
        return super(CORSRequestHandler, self).end_headers()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))  # Use the PORT environment variable
    httpd = HTTPServer(('0.0.0.0', port), CORSRequestHandler)  # Bind to all interfaces
    print(f"Serving on port {port}")
    httpd.serve_forever()