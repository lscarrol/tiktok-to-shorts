from TikTokApi import TikTokApi

api = TikTokApi.get_instance()
trending_videos = api.trending(count=10) # get 10 trending videos

for i in range(len(trending_videos)):
   data = api.get_Video_By_TikTok(trending_videos[i]) # bytes of the video
   with open("downloads/{}.mp4".format(str(i)), 'wb') as output:
       output.write(data) # saves data to the mp4 file
