import asyncio
import time


async def fun():
    print("fun")
    await asyncio.sleep(2)
    print("hello, async world!")


async def do_other_thing():
    print("starting other thing")
    await asyncio.sleep(1)
    print("end other thing")


async def main():
    await asyncio.gather(fun(),do_other_thing(),)  # 为什么这里没有创建任务


asyncio.run(main())
