import asyncio

async def greet():
    print("Hello")

asyncio.run(greet())

async def task_a():
    print("A1")
    await asyncio.sleep(1)
    print("A2")


async def task_b():
    print("B1")
    await asyncio.sleep(1)
    print("B2")

asyncio.run(task_a())
asyncio.run(task_b())