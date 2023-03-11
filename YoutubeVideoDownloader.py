from pytube import YouTube

link = "https://www.youtube.com/watch?v=jqOx32Cv-XI"

youtube = YouTube(link)
print(youtube.title)  #To get title of your video
print(youtube.thumbnail_url) # to get thumbnail of your video

video =youtube.streams.all()   #it will save all the streaming quality of your video in video variable

# to get only audio, do this--

audio = youtube.streams.filter(only_audio=True)     # rest Code is as it is... just replace video with audio

vid= list(enumerate(video))  #vid will store all stream quality in form of list

for i in vid:
    print(i)     #it will print( all the stream quality of our video)

strm = int(input("Enter :  "))
video[strm].download()     #it will download your video
print("Download Successful")
