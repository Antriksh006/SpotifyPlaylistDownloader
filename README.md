# Spotify Playlist Downloader - Script
This Project uses [Spotify Web API](https://developer.spotify.com/documentation/web-api) and [Youtube API](https://developers.google.com/youtube/v3/getting-started) to get all the songs from a *Spotify Playlist* and DOWNLOAD them in a `mp3` format.
---
## 🚀 Installation
### 📦 Prerequisite
- Spotify Account
- Google Account
- **Python** installed
- `requests`, `yt-dlp`, `google-api-python-client` python modules installed
### ♨️ How to Use
- Clone this repositery using `git clone`.
- Get the **CLIENT_ID** and **CLIENT_SECRET** by creating an Application on your [Spotify Web API](https://developer.spotify.com/documentation/web-api) Dashboard.
- Get the **Youtube API Key** from the [Google Developers Console](https://console.cloud.google.com/apis/dashboard)
- Get the **PLAYLIST LINK** you want to download.
- Get the **PATH LOCATION** of the folder you want to download the MP3 files to.
- Now run the `main.py` file
- Paste the Environment Variables as they are asked.
- The Downloads will start.
### 🔧 ChangeLogs
- 7/24/24
> It no mores makes a `.txt` files with the youtube links, instead downlaods the songs directly.
> No more requires `dotenv` for getting the environment variables.
- 7/17/24
> Now the `.txt` also stores the artist's name and the youtube link for the track

