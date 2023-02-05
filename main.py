from pytube import Playlist
import os

url = input("Enter Playlist url: ")

yt_playlist = Playlist(url)

os.mkdir(r"C:\Users\Micne\Desktop\YouTube_downloader\Downloads")

for video in yt_playlist.videos:
    video.streams.get_highest_resolution().download(r"C:\Users\Micne\Desktop\YouTube_downloader\Downloads")
    print('Video downloaded: ', video.title)

print("\nAll videos are downloaded")
