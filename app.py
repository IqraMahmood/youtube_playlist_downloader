import streamlit as st
from pytube import Playlist
from PIL import Image
# # Set up Streamlit page
image = Image.open('app.png')
st.title("YouTube Playlist Downloader")
playlist_url = st.text_input("Enter the URL of the YouTube playlist you want to download:")
download_button = st.button("Download Playlist")

# Download the playlist when the download button is clicked
if download_button:
    try:
        # Create a Playlist object from the given URL
        playlist = Playlist(playlist_url)

        # Create a download link for each video in the playlist
        for video in playlist.videos:
            st.write(f"Generating download link for {video.title}...")
            video_url = video.streams.get_highest_resolution().url
            st.markdown(f'<a href="{video_url}" download="{video.title}.mp4">Download {video.title}</a>', unsafe_allow_html=True)
            st.write(f"Download link for {video.title} generated!")

        st.success("Playlist download links generated successfully!")
    except Exception as e:
        st.error(f"An error occurred: {e}")
