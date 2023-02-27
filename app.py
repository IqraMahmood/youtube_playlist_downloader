import streamlit as st
from pytube import Playlist
import zipfile
import os
import base64


# Set up Streamlit page
st.title("YouTube Playlist Downloader")
playlist_url = st.text_input("Enter the URL of the YouTube playlist you want to download:")
download_button = st.button("Download Playlist")

# Download the playlist when the download button is clicked
if download_button:
    try:
        # Create a Playlist object from the given URL
        playlist = Playlist(playlist_url)

        # Create a directory to store the downloaded videos
        dir_path = os.path.join(os.getcwd(), "videos")
        os.makedirs(dir_path, exist_ok=True)

        # Download each video in the playlist to the videos directory
        for i, video in enumerate(playlist.videos):
            st.write(f"Downloading {video.title}...")
            video.streams.get_highest_resolution().download(output_path=dir_path)
            st.write(f"{i+1}/{len(playlist)} videos downloaded!")

        # Create a zip file of the downloaded videos
        zip_file_path = os.path.join(os.getcwd(), "playlist.zip")
        with zipfile.ZipFile(zip_file_path, "w") as zip_file:
            for video_file in os.listdir(dir_path):
                video_file_path = os.path.join(dir_path, video_file)
                zip_file.write(video_file_path, arcname=video_file)
        st.success("Playlist download complete!")
        st.write(f"Download the complete playlist as a zip file: [playlist.zip](data:application/zip;base64,{base64.b64encode(open(zip_file_path, 'rb').read()).decode('utf-8')})")
    except Exception as e:
        st.error(f"An error occurred: {e}")
