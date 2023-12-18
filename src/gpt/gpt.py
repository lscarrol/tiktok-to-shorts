from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

youtube = build('youtube', 'v3', developerKey='YOUR_DEVELOPER_KEY')

request = youtube.videos().insert(
   part="snippet,status",
   body={
       "snippet": {
           "title": "My video title",
           "description": "My video description",
           "tags": ["tag1", "tag2"],
           "categoryId": "22"
       },
       "status": {
           "privacyStatus": "private"
       }
   },
   media_body=MediaFileUpload("path_to_video.mp4")
)

response = request.execute()