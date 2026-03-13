from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

# Variable globale pour stocker le code d'authentification
AUTH_CODE = None

class AuthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global AUTH_CODE
        # Extraire le code de l'URL
        if "code" in self.path:
            AUTH_CODE = self.path.split("code=")[1].split("&")[0]
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Authentification réussie ! Vous pouvez fermer cette fenêtre.")
        else:
            self.send_response(400)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Erreur : Aucun code d'authentification trouvé.")

def run_server():
    server_address = ("", 8888)
    httpd = HTTPServer(server_address, AuthHandler)
    print("Démarrage du serveur sur http://127.0.0.1:8888")
    httpd.serve_forever()

# Démarrer le serveur dans un thread séparé
threading.Thread(target=run_server, daemon=True).start()