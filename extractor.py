import json
import os
import json
import youtube_dl


def extract_format_data(format_data):
    extension = format_data["ext"]
    format_name = format_data["format"]
    url = format_data["url"]
    return {
        "extension": extension,
        "format_name": format_name,
        "url": url
    }


   

def extract_video_data_from_url(url):
    ydl_opts = {
        'no_playlist': True,
        'quiet': True,
        'no_warnings': True,
        'outtmpl': '%(id)s'
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        video_data = ydl.extract_info(url, download=False)

    title = video_data["title"]
    formats = video_data["formats"]
    thumbnail = video_data["thumbnail"]
    formats = [extract_format_data(format_data) for format_data in formats]
    return {
        "title": title,
        "formats": formats,
        "thumbnail": thumbnail
    }
