# python_server.py
from http.server import SimpleHTTPRequestHandler, HTTPServer
import signal
import sys
import urllib.parse
import os

def signal_handler(sig, frame):
    print('Deteniendo el servidor...')
    sys.exit(0)

class CalculadoraHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/calculadora'):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            # Construye la ruta completa al archivo calculadora.html
            ruta_calculadora = os.path.join(os.getcwd(), 'calculadora', 'calculadora.html')

            # Lee el contenido de calculadora.html
            with open(ruta_calculadora, 'r') as file:
                contenido_html = file.read()

            self.wfile.write(contenido_html.encode())
        elif self.path.endswith('.css'):
            # Maneja archivos CSS
            self.send_response(200)
            self.send_header('Content-type', 'text/css')
            self.end_headers()

            # Construye la ruta completa al archivo CSS
            ruta_css = os.path.join(os.getcwd(), 'calculadora', self.path[1:])

            # Lee el contenido del archivo CSS
            with open(ruta_css, 'r') as file:
                contenido_css = file.read()

            self.wfile.write(contenido_css.encode())
        else:
            super().do_GET()

# Configura el manejador de señales para manejar Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

# Define el puerto en el que se ejecutará el servidor
puerto = 8000

# Configura el manejador de solicitudes
handler = CalculadoraHandler

# Crea el servidor HTTP
httpd = HTTPServer(('localhost', puerto), handler)

# Imprime la información del servidor
print(f"Servidor Python ejecutándose en http://localhost:{puerto}/")

try:
    # Inicia el servidor
    httpd.serve_forever()
except KeyboardInterrupt:
    # Maneja la interrupción de teclado (Ctrl+C)
    print('Deteniendo el servidor...')
    httpd.shutdown()
    sys.exit(0)
