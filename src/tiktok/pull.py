import requests
from dotenv import load_dotenv
import os

# Load access jey fir pvleopard
load_dotenv()
access_key = os.getenv("ACCESS_KEY")

url = "https://tiktok89.p.rapidapi.com/tiktok"

querystring = {"link":"https://www.tiktok.com/@kkirstylouise/video/7242500808040877338?is_from_webapp=1&sender_device=pc&web_id=7314050613808793134"}

headers = {
	"X-RapidAPI-Key": access_key,
	"X-RapidAPI-Host": "tiktok89.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())