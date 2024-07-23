# Spotify Playlist Downloader

This project utilizes the [Spotify Web API](https://developer.spotify.com/documentation/web-api) and [YouTube Data API](https://developers.google.com/youtube/v3/getting-started) to fetch songs from a Spotify playlist and download them in MP3 format.

## 🚀 Installation

### 📦 Prerequisites

- **Spotify Account**: Required for accessing Spotify Web API.
- **Google Account**: Required for obtaining YouTube API Key.
- **Python**: Ensure Python is installed on your system.
- **Python Packages**: Install the required Python packages using the following command:
```sh
  pip install requests yt-dlp google-api-python-client
```

### 🛠️ Setup

1. **Clone the Repository**
```sb
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
```

2. **Obtain API Credentials**

   - **Spotify**:
     - Create an application on the [Spotify Web API Dashboard](https://developer.spotify.com/dashboard/applications) to get your `CLIENT_ID` and `CLIENT_SECRET`.
   - **YouTube**:
     - Get your API Key from the [Google Developers Console](https://console.cloud.google.com/apis/dashboard).

3. **Configure Environment Variables**

   - Run the script and provide the following information when prompted:
     - **Spotify CLIENT_ID**: Your Spotify application client ID.
     - **Spotify CLIENT_SECRET**: Your Spotify application client secret.
     - **YouTube API Key**: Your YouTube Data API key.
     - **Playlist URL**: The URL of the Spotify playlist you want to download.
     - **Download Path**: The directory where you want the MP3 files to be saved.

4. **Run the Script**
```sh
   python main.py
```
## 🔧 Change Log

- **7/24/24**: Updated script to download MP3 files directly. Removed `.txt` file generation for YouTube links.
- **7/17/24**: Added functionality to store artist names and YouTube links in a `.txt` file.

## 🤝 Contributing

If you want to contribute to this project, please fork the repository and submit a pull request. For any issues or feature requests, please open an issue in the GitHub repository.
