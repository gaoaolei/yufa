import sys

import aiohttp
import asyncio
import time

header = {
    "Cookie": " _ga=GA1.2.1260896999.1647251033; token=eyJhdmF0YXIiOiJodHRwczovL3dwaW1nLndhbGxzdGNuLmNvbS9mNzc4NzM4Yy1lNGY4LTQ4NzAtYjYzNC01NjcwM2I0YWNhZmUuZ2lmIiwidXNlcm5hbWUiOiJnYW9hb2xlaUAxOXBheS5jb20uY24iLCJuYW1lIjoiXHU5YWQ4XHU1MGIyXHU5NmY3IiwidXNlcl9pZCI6IjY4OTEyOTQ0MDU1MDMyNjI3MiJ9:1ntU9o:FyKOjJs58pGFTzsBy3Owyj0tl4OdgUsFKS607r7qyXU"}
url1 = 'http://127.0.0.1:5000/api/work/report/user-demand?start_day=2022-05-01&end_day=2022-11-23&show_type=user'
#
#
# async def fetch_async(url, session):
#     async with session.get(url) as response:
#         print('asd')
#         return await response.text()
#
#
# async def main():
#     async with aiohttp.ClientSession(headers=header) as session:
#         page1 = [asyncio.create_task(fetch_async(url1, session)) for _ in range(1000)]
#         page2 = asyncio.create_task(fetch_async(url2, session))
#         await asyncio.gather(*page1, page2)
#
#
# start_time = time.time()
# asyncio.run(main())
# print(f"Done in {time.time() - start_time} seconds")

import aiohttp
import asyncio


async def fire_and_forget(url, session):
    try:
        print(time.time())
        async with session.get(url,ssl=False,allow_redirects=False) as response:
            # print(await response.json())
            print(time.time())
            print('发出请求')
            pass  # 完全不处理响应
    except:
        pass  # 忽略所有错误


async def main():
    url = url1  # 替换为目标URL
    concurrency = 500  # 并发量

    # 优化连接池配置
    connector = aiohttp.TCPConnector(
        limit=concurrency,
        force_close=False,  # 快速回收连接
        enable_cleanup_closed=True,
        use_dns_cache=True,  # 启用DNS缓存
        ttl_dns_cache=300
    )

    async with aiohttp.ClientSession(connector=connector,headers=header,timeout=aiohttp.ClientTimeout(total=None,connect=3,sock_read=2)) as session:
        while True:  # 持续发送
            tasks = [
                asyncio.create_task(fire_and_forget(url, session))
                for _ in range(concurrency)
            ]
            await asyncio.gather(*tasks)


if __name__ == "__main__":
    # Windows系统需要设置事件循环策略
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(main())