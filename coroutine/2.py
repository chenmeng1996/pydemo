import asyncio

@asyncio.coroutine
def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1):
    r = yield from asyncio.sleep(1)
    print("Hello again!")

loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
print(111)
loop.close()