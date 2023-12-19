
from TikTokApi import TikTokApi
import asyncio
import os


async def trending_videos():
    async with TikTokApi() as api:
        await api.create_sessions(ms_tokens=['TwiMOav4Nynu9NcG68hf8Y1by9Cyb7EhjT7eUtSTn1vp9HoykXethC1hgy3F-z5a2Jm5CiE1PdcdO-diaohvBzdqwWkSzpU44CUwoeQDleC8vbRKbgsxrMOiyMI-Sw--tFOxdBwpzxwoJAM=', 'm_DjsBvPcwAg3xFHiufTsfp2r6lMNysKnWcyhXyXh3oSubNpHI4rp975-jBnH9JrWM36bOtb2STSXQarVHFR4MVEAGbbQkdHSCYdE3jKeRMkqzUlrVLDIV6CCmdtF4ATwgovVtRvdkilap2I='], num_sessions=1, sleep_after=3)
        async for video in api.trending.videos(count=30):
            print(video)
            print(video.as_dict)

if __name__ == "__main__":
    asyncio.run(trending_videos())