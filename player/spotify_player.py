# player/spotify_player.py
import requests

class SpotifyPlayer:
    def __init__(self, access_token):
        self.access_token = access_token

    def play_last_played_song(self, playlist_id=None):
        url = "https://api.spotify.com/v1/me/player/play"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        payload = {
            "context_uri": f"spotify:playlist:{playlist_id}" if playlist_id else None
        }
        response = requests.put(url, json=payload, headers=headers)
        return response.status_code