import asyncio
import time


async def hello():
    print("Hello world!")
    time.sleep(1)
    print("Hello again!")


def handle():
    tasks = [asyncio.create_task(hello()) for i in range(2)]
    await asyncio.gather(*tasks)
    print(111)


handle()
print(222)
