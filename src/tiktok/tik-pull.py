import asyncio
from douyin_tiktok_scraper.scraper import Scraper

api = Scraper()

async def hybrid_parsing(url: str) -> dict:
    # Hybrid parsing(Douyin/TikTok URL)
    result = await api.hybrid_parsing(url)
    print(f"The hybrid parsing result:\n {result}")
    return result

asyncio.run(hybrid_parsing(url=input("Paste Douyin/TikTok share URL here: ")))