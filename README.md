# SpotifyPlaylistExporter
This Project uses [Spotify Web API](https://developer.spotify.com/documentation/web-api) to get all the songs from a *Spotify Playlist* and format their Names into a plain `.txt` file 
---
## 🚀 Installation
### 📦 Prerequisite
- Spotify Account
- **Python** installed
- `requests` and `dotenv` python modules installed
### ♨️ How to Use
- Get the **CLIENT_ID** and **CLIENT_SECRET** by creating an Application on your Spotify Web Api dashboard
- Clone this repositery using `git clone`. After doing so, paste the **CLIENT_ID** and **CLIENT_SECRET** into the `.env` file          ![Screenshot-20240717-023230-1.png](https://i.postimg.cc/1tqbV8kG/Screenshot-20240717-023230-1.png)
- In the bottom of main.py change the `"YOUR_PLAYLIST_ID_GOES_HERE"` to the Spotify Playlist ID you want to get the tracks from [![Screenshot-20240717-024615.png](https://i.postimg.cc/kMbGywNC/Screenshot-20240717-024615.png)](https://postimg.cc/ThTTdVHN)
- Now run the `main.py` file
- A file named `playlist_tracks.txt` will be made containing the Playlist's Tracks

