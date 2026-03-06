import asyncio
import httpx
from src.geocoder import ResilientGeocoder
from src.indexer.py import WealthIndexer # In GitHub, ensure paths match

async def main():
    addresses = ["Via Roma 1, Milano", "Corso Buenos Aires, 10, Milano"]
    geocoder = ResilientGeocoder()
    
    async with httpx.AsyncClient() as client:
        for addr in addresses:
            coords, conf = await geocoder.get_coordinates(client, addr)
            # Mocking ISTAT Data for the PoC
            # In production, this pulls from Step 3 & 4
            mwi = WealthIndexer.calculate_mwi(0.8, 0.7, 0.9)
            
            print(f"Address: {addr} | Confidence: {conf} | MWI: {mwi}")

if __name__ == "__main__":
    asyncio.run(main())
