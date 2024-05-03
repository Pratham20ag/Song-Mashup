
# os.system('pip install google-api-python-client')
# os.system('pip install pytube')
# os.system('pip install moviepy')
# os.system('pip install pydub')





import os
from googleapiclient.discovery import build
from pytube import YouTube
from moviepy.editor import VideoFileClip,concatenate_videoclips

def download_videos(response, output_path):
    for item in response['items']:
        video_id = item['id']['videoId']
        video_title = item['snippet']['title']
        print(f"Downloading {video_title}...")
        yt = YouTube(f'https://www.youtube.com/watch?v={video_id}')
        stream = yt.streams.first()
        stream.download(output_path=output_path, filename=f"{video_title}.mp3")
        print(f"{video_title} downloaded successfully!")

def mashup(response,output_path,clip_seconds):
        video_clips = []
        for item in response['items']:   
            video_title = item['snippet']['title']    
            video_file = f"{output_path}/{video_title}.mp3"
            clip = VideoFileClip(video_file).subclip(0, clip_seconds)
            video_clips.append(clip)
        final_clip = concatenate_videoclips(video_clips)
        final_clip.write_videofile(f"{output_path}/mashup.mp3")


if __name__ == "__main__":
    api_key = 'AIzaSyAAdHMXDrTnUxDYhrBw5zkuV_3UiQgEFcg'
    artist_name = 'Bruno Mars'

    youtube = build('youtube', 'v3', developerKey=api_key)

    request = youtube.search().list(
        q=artist_name,
        part='snippet',
        type='video',
        videoCategoryId='10',  # Music category
        maxResults=10
    )

    response = request.execute()
    output_path = "C:/Users/Pratham/Desktop/Sem6/Predictive Analysis/Assignment5"
    download_videos(response,output_path)
    mashup(response,output_path,20)


    # Print the titles of the retrieved videos
    for item in response['items']:
        video_title = item['snippet']['title']
        print(f"Title: {video_title}")
