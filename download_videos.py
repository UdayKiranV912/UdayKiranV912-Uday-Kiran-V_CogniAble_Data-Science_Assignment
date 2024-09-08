import yt_dlp

video_urls = [
    "https://www.youtube.com/watch?v=V9YDDpo9LWg",
    "https://www.youtube.com/watch?v=JBoc3w5EKfI",
    "https://www.youtube.com/watch?v=aWV7UUMddCU",
    "https://www.youtube.com/watch?v=f6wqlpG9rd0",
    "https://www.youtube.com/watch?v=GNVTuLHdeSo",
    "https://www.youtube.com/watch?v=SWtmkjd45so",
    "https://www.youtube.com/watch?v=RzI6Ar5mu2Q",
    "https://www.youtube.com/watch?v=aulLej6Z6W8",
    "https://www.youtube.com/watch?v=7pN6ydLE4EQ",
    "https://www.youtube.com/watch?v=fEEelCgBkWA",
    "https://www.youtube.com/watch?v=ckZQbQwM3oU",
    "https://www.youtube.com/watch?v=E8Wgwg3F4X0",
    "https://www.youtube.com/watch?v=rvIPH4ccfpI",
    "https://www.youtube.com/watch?v=F6iqlW6ovZc",
    "https://www.youtube.com/watch?v=9qjk-Sq415s",
    "https://www.youtube.com/watch?v=DI25kGJis0w",
    "https://www.youtube.com/watch?v=rrLhFZG6iQY",
    "https://www.youtube.com/watch?v=RKOZbT0ftL4",
    "https://www.youtube.com/watch?v=N7TBbWHB01E",
    "https://www.youtube.com/watch?v=1YqVEVbXQ1c",
]

output_dir = "test_videos"

ydl_opts = {
    'outtmpl': f'{output_dir}/%(title)s.%(ext)s',
    'format': 'bestvideo+bestaudio/best',
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(video_urls)
