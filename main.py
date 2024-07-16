from dotenv import load_dotenv
from requests import post,get
import os
import base64
import json

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}

    response = post(url, headers=headers, data=data)
    json_result = response.json()
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def search_for_playlist(token, playlist_id):
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    headers = get_auth_header(token)
    params = {"limit": 100}
    tracks = []

    while url:
        response = get(url, headers=headers, params=params)
        
        if response.status_code != 200:
            print(f"Error fetching playlist data: {response.status_code} - {response.text}")
            return []

        json_result = response.json()
        items = json_result.get("items", [])
        for item in items:
            track = item.get("track")
            if track is not None:  
                nameoftrack = track.get("name", "Unknown")
                tracks.append(nameoftrack)
            else:
                continue

        url = json_result.get("next")

    return tracks

def save_tracks_to_file(tracks, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for track in tracks:
            f.write(track + '\n')

token = get_token()
print(f"Access Token: {token}") 
playlist_tracks = search_for_playlist(token, "YOUR_PLAYLIST_ID_GOES_HERE")

save_tracks_to_file(playlist_tracks, 'playlist_tracks.txt')
print("Tracks saved to playlist_tracks.txt")