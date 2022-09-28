import asyncio
import time

# async indicates a coroutine
async def test1():
    print("hello")
    # wait util another coroutine complete
    await asyncio.sleep(1)
    print("world")


async def test2_1():
    """
    only one couroutine at a time

    cost 2 second
    """
    async def say_after():
        await asyncio.sleep(1)
        print("hello")
    print(f"start at {time.strftime('%X')}")
    await say_after()
    await say_after()
    print(f"end at {time.strftime('%X')}")


async def test2_2():
    """
    many couroutine at a time

    cost 1 second
    """
    async def say_after():
        await asyncio.sleep(1)
        print("hello")
    
    task1 = asyncio.create_task(say_after())
    task2 = asyncio.create_task(say_after())
    print(f"start at {time.strftime('%X')}")
    await task1
    await task2
    print(f"end at {time.strftime('%X')}")


if __name__ == "__main__":
    asyncio.run(test2_2())