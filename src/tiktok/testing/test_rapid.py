import requests

url = "https://tiktok-api6.p.rapidapi.com/search/general/query"

payload = { "query": "mr beast" }
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "a54c9b25ccmsh06f9d5ee69fd8f5p1cc731jsn515c0b1b82b5",
	"X-RapidAPI-Host": "tiktok-api6.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())