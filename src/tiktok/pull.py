import requests
from dotenv import load_dotenv
import os
import json
import urllib.request


# Load key for api
load_dotenv()
access_key = os.getenv("ACCESS_KEY")



def get_tt(tt_url):
	querystring = {"link": tt_url}
	headers = {
		"X-RapidAPI-Key": access_key,
		"X-RapidAPI-Host": "tiktok89.p.rapidapi.com"
	}
	api_url = "https://tiktok89.p.rapidapi.com/tiktok"
	response = requests.get(api_url, headers=headers, params=querystring)
	json_res = response.json()
	video_links = json_res['video']['play_addr']['url_list']
	grab_link = video_links[0]
	urllib.request.urlretrieve(grab_link, 'tmp.mp4') 


get_tt("https://www.tiktok.com/@kkirstylouise/video/7242500808040877338?is_from_webapp=1&sender_device=pc&web_id=7314050613808793134")