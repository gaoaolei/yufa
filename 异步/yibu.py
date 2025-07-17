import aiohttp
import asyncio


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(response.status)


async def main():
    tasks = [fetch("https://example.com") for _ in range(10)]
    await asyncio.gather(*tasks)


asyncio.run(main())
