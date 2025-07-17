import aiohttp
import asyncio
import uvloop
import time
import sys
from typing import List

# 安装uvloop并设置为默认事件循环
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


class PressureTester:
    def __init__(self, target_url: str, concurrency: int = 1000):
        self.target_url = target_url
        self.concurrency = concurrency
        self.request_count = 0
        self.start_time = time.monotonic()

        # 优化后的连接池配置
        self.connector = aiohttp.TCPConnector(
            limit=0,  # 不限制总连接数
            limit_per_host=200,  # 每个目标主机最大连接数
            force_close=False,  # 启用Keep-Alive
            enable_cleanup_closed=True,
            use_dns_cache=True,  # 启用DNS缓存
            ttl_dns_cache=300  # DNS缓存5分钟
        )

        # 客户端超时设置
        self.timeout = aiohttp.ClientTimeout(
            total=None,  # 无总超时
            connect=3,  # 连接超时3秒
            sock_read=2  # 读取超时2秒
        )

    async def fire_request(self, session: aiohttp.ClientSession) -> None:
        """发送单个请求(不处理响应)"""
        try:
            async with session.get(
                self.target_url,
                ssl=False,  # 关闭SSL验证
                allow_redirects=False,  # 禁用重定向
                headers={"Connection": "keep-alive"}  # 强制保持连接
            ) as _:
                pass
        except Exception:
            pass
        finally:
            self.request_count += 1

    async def run_requests(self, session: aiohttp.ClientSession) -> None:
        """持续发送请求"""
        while True:
            tasks: List[asyncio.Task] = []
            for _ in range(self.concurrency):
                task = asyncio.create_task(self.fire_request(session))
                tasks.append(task)
            await asyncio.gather(*tasks)

    async def print_stats(self) -> None:
        """打印实时统计信息"""
        last_count = 0
        last_time = self.start_time

        while True:
            await asyncio.sleep(5)  # 每5秒打印一次
            now = time.monotonic()
            elapsed = now - last_time
            current_qps = (self.request_count - last_count) / elapsed

            print(
                f"总请求数: {self.request_count} | "
                f"当前QPS: {current_qps:.0f} | "
                f"运行时间: {now - self.start_time:.1f}s"
            )

            last_count = self.request_count
            last_time = now

    async def run(self) -> None:
        """启动压测"""
        # 启动统计协程
        stats_task = asyncio.create_task(self.print_stats())

        # 启动压测
        async with aiohttp.ClientSession(
            connector=self.connector,
            timeout=self.timeout
        ) as session:
            try:
                await self.run_requests(session)
            except asyncio.CancelledError:
                pass
            finally:
                stats_task.cancel()
                await stats_task


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python pressure_test.py <target_url> [concurrency]")
        sys.exit(1)

    target_url = sys.argv[1]
    concurrency = int(sys.argv[2]) if len(sys.argv) > 2 else 1000

    # 提高文件描述符限制(Linux/macOS)
    try:
        import resource

        soft, hard = resource.getrlimit(resource.RLIMIT_NOFILE)
        resource.setrlimit(resource.RLIMIT_NOFILE, (hard, hard))
        print(f"文件描述符限制已设置为: {hard}")
    except (ImportError, ValueError):
        pass

    # 运行压测
    tester = PressureTester(target_url, concurrency)
    try:
        asyncio.run(tester.run())
    except KeyboardInterrupt:
        print("\n压测已停止")