from requests import post, get
import base64
from googleapiclient.discovery import build
import yt_dlp as youtube_dl

YOUTUBE_API_KEY = input('ENTER THE YOUTUBE API KEY: ')
client_id = input("SPOTIFY APP CLIENT ID: ")
client_secret = input("SPOTIFY APP CLIENT SECRET: ")
path_location = input("ENTER THE PATH LOCATION: ")
playlist_id_input = input("ENTER THE SPOTIFY PLAYLIST LINK: ")
ydl_opts = {
    'outtmpl': path_location + '/%(title)s.%(ext)s'
}

def get_token():
    auth_string = f"{client_id}:{client_secret}"
    auth_base64 = base64.b64encode(auth_string.encode("utf-8")).decode("utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}

    response = post(url, headers=headers, data=data)
    response.raise_for_status()  # Raise an error for HTTP errors
    json_result = response.json()
    return json_result["access_token"]

def get_auth_header(token):
    return {"Authorization": f"Bearer {token}"}

def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"
    response = get(url + query, headers=headers)
    response.raise_for_status()
    return response.json()

def search_videos(query):
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
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
        response.raise_for_status()
        json_result = response.json()
        items = json_result.get("items", [])
        for item in items:
            track = item.get("track")
            if track:
                name_of_track = track.get("name", "Unknown")
                artist_names = ', '.join(artist.get('name', 'Unknown Artist') for artist in track.get("artists", []))
                tracks.append(f"{name_of_track} - {artist_names}")
        url = json_result.get("next")

    return tracks


def get_playlist_id(playlistLink):
    check = 0
    id = ''
    for element in playlistLink:
        if check == 4:
            if element == '?':
                break;
            else:
                id = id + element
        elif element == '/':
            check += 1
    return id


def download_tracks(tracks):
    for track in tracks:
        youtube_url = search_videos(track)
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
def main():
    try:
        token = get_token()
        print(f"Access Token: {token}")  # Debug: print access token
        id1 = get_playlist_id(playlist_id_input)
        playlist_tracks = search_for_playlist(token, id1)
        download_tracks(playlist_tracks)
        print("Tracks downloaded successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
