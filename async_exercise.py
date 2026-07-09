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

print('-------------asyncio create task exercise----------------')
async def load_users():
    await asyncio.sleep(2)
    print("Users loaded")

async def load_orders():
    await asyncio.sleep(3)
    print("Orders loaded")

async def load_dashboard():
    users = asyncio.create_task(load_users())
    orders = asyncio.create_task(load_orders())

    print('Preparing dashboard...')
    await users
    await orders


asyncio.run(load_dashboard())