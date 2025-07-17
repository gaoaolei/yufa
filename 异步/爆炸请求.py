import asyncio

import aiohttp


async def burst_requests(url, data, rate_per_second,header):
    semaphore = asyncio.Semaphore(rate_per_second)

    async def send_request():
        async with semaphore:
            async with aiohttp.ClientSession() as session:
                try:
                    async with session.post(url, json=data,headers=header):
                        pass
                except Exception as e:
                    print(f"Error: {e}")

    while True:
        await asyncio.gather(*[send_request() for _ in range(rate_per_second)])
        await asyncio.sleep(1)  # 每秒发送rate_per_second个请求


asyncio.run(burst_requests("https://dxkfaiapi-dev.iyoudui.com/v1/chat/completions", {"maxTokens": 10240, "messages": [{"content": "角色", "role": "user"}], "model": "deepseek-v3", "stream": True,
        "temperature": 0.1}, 20,{"Content-Type": "application/json", "Accept": "text/event-stream"}))