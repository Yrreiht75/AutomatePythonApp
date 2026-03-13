# main.py
from config.config_manager import ConfigManager
from auth.spotify_authenticator import SpotifyAuthenticator
from launcher.application_launcher import ApplicationLauncher
from ui.ui_manager import UIManager
from player.spotify_player import SpotifyPlayer

if __name__ == "__main__":
    config = ConfigManager()
    authenticator = SpotifyAuthenticator(config.client_id, config.client_secret, config.redirect_uri)
    launcher = ApplicationLauncher()
    player = SpotifyPlayer("access_token")  # Cela sera remplacé par le token réel
    ui = UIManager(authenticator, launcher, player)
    ui.create_ui()