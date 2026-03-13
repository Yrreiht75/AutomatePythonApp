# ui/ui_manager.py
import tkinter as tk

class UIManager:
    def __init__(self, authenticator, launcher, player):
        self.authenticator = authenticator
        self.launcher = launcher
        self.player = player

    def create_ui(self):
        root = tk.Tk()
        root.title("Automatisation Spotify")
        root.geometry("400x300")

        frame = tk.Frame(root)
        frame.pack(expand=True)

        # Bouton pour ouvrir Spotify
        btn_spotify = tk.Button(
            frame,
            text="Se connecter à Spotify",
            width=25,
            command=self.open_spotify_auth
        )
        btn_spotify.grid(row=0, column=0, pady=10, padx=10)

        # Bouton pour jouer la dernière chanson
        btn_play = tk.Button(
            frame,
            text="Jouer la dernière chanson",
            width=25,
            command=self.play_last_played_song
        )
        btn_play.grid(row=1, column=0, pady=10, padx=10)

        root.mainloop()

    def open_spotify_auth(self):
        auth_url = self.authenticator.get_auth_url()
        self.launcher.open_spotify_auth(auth_url)

    def play_last_played_song(self):
        # Utiliser le code stocké dans le serveur
        from server.auth_server import AUTH_CODE
        if AUTH_CODE:
            access_token = self.authenticator.get_access_token(AUTH_CODE)
            self.player = SpotifyPlayer(access_token)
            status = self.player.play_last_played_song()
            print(f"Status de la lecture : {status}")
        else:
            print("Aucun code d'authentification trouvé.")