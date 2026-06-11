import http.server
import socketserver
import webbrowser
import os

PORT = 5500
os.chdir(os.path.dirname(os.path.abspath(__file__)))
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Servidor rodando em http://localhost:{PORT}")
    webbrowser.open(f"http://localhost:{PORT}/admin.html")
    httpd.serve_forever()
