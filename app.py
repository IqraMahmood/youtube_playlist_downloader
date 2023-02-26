import streamlit as st
from pytube import Playlist
from PIL import Image
# Set up Streamlit page
image = Image.open('app.png')
st.image(image, use_column_width=True)
st.title("YouTube Playlist Downloader")
st.write("## This app is created Using Streamlit")

playlist_url = st.text_input("Enter the URL of the YouTube playlist you want to download:")

download_button = st.button("Download Playlist")

# Download the playlist when the download button is clicked
if download_button:
    try:
        # Create a Playlist object from the given URL
        playlist = Playlist(playlist_url)

        # Iterate over each video in the playlist and download it
        for video in playlist.videos:
            st.write(f"Downloading {video.title}...")
            video.streams.get_highest_resolution().download()
            st.write(f"Downloaded {video.title}")

        st.success("Playlist downloaded successfully!")
    except Exception as e:
        st.error(f"An error occurred: {e}")
