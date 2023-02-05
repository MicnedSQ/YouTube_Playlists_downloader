from pytube import Playlist

url = input("Enter Playlist url: ")

yt_playlist = Playlist(url)

for video in yt_playlist.videos:
    video.streams.get_highest_resolution().download(r"C:\Users\Micne\Desktop\YouTube_downloader\Downloads")
    print('Video downloaded: ', video.title)

print("\nAll videos are downloaded")
