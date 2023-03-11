from pytube import Playlist
py = Playlist("https://www.youtube.com/watch?v=wElMF3vS060&list=PLdo5W4Nhv31aGZY3Wi9mTThGJvWblpQ9g")
print(f"Downloading: {py.title}")
for video in py.videos:
    video.streams.first().download()
