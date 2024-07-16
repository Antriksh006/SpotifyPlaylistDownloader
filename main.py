from dotenv import load_dotenv
from requests import post, get
import os
import base64
from googleapiclient.discovery import build
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

def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"

    query_url = url + query
    response = get(query_url, headers=headers)
    json_result = response.json()
    print(json_result)

def search_videos(query):
    youtube = build('youtube', 'v3', developerKey='YOUR_YOUTUBE_API_KEY_GOES_HERE')
    request = youtube.search().list(part='id', type='video', q=query, maxResults=1)
    response = request.execute()
    video_id = response['items'][0]['id']['videoId']
    return f"https://www.youtube.com/watch?v={video_id}"

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
                name_of_track = track.get("name", "Unknown")
                artists = track.get("artists", [])
                artist_names = ', '.join([artist.get('name', 'Unknown Artist') for artist in artists])
                tracks.append(f"{name_of_track} - {artist_names}")
            else:
                continue

        url = json_result.get("next")

    return tracks


def save_tracks_to_file(tracks, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for track in tracks:
            f.write(f"{track}\n")
            youtube_url = search_videos(track)
            f.write(f"YouTube: {youtube_url}\n\n")

token = get_token()
print(f"Access Token: {token}")  # Debug: print access token
playlist_tracks = search_for_playlist(token, "YOUR_PLAYLIST_ID_GOES_HERE")

save_tracks_to_file(playlist_tracks, 'playlist_tracks.txt')
print("Tracks saved to playlist_tracks.txt")
