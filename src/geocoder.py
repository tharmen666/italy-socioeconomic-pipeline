import asyncio
import backoff
import httpx
from aiolimiter import AsyncLimiter

# 10k/day rate limiter (approx 7req/sec for burst, but we'll stay safe)
limiter = AsyncLimiter(5, 1)

class ResilientGeocoder:
    def __init__(self, user_agent="DeepTech_Challenge_Agent"):
        self.url = "https://nominatim.openstreetmap.org/search"
        self.headers = {"User-Agent": user_agent}

    @backoff.on_exception(backoff.expo, httpx.HTTPStatusError, max_tries=5)
    async def get_coordinates(self, client, address: str):
        """Asynchronous geocoding with exponential backoff."""
        params = {"q": address, "format": "json", "countrycodes": "it", "limit": 1}
        
        async with limiter:
            response = await client.get(self.url, params=params, headers=self.headers)
            response.raise_for_status()
            data = response.json()
            
            if not data:
                return None, 0.0
            
            # Confidence Score logic based on API 'importance'
            # (Essential for the 'Explainable AI' requirement)
            confidence = float(data[0].get("importance", 0.5))
            return {"lat": data[0]["lat"], "lon": data[0]["lon"]}, confidence
