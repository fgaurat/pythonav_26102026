import asyncio
import time
async def hello():
    print("hello")

async def add(a,b):
    await asyncio.sleep(1)
    return a+b


async def main():
    start = time.perf_counter()
    # print('Hello ...')
    # await asyncio.sleep(1)
    # await hello()
    # print('... World!')

    # r = await add(1,2)
    # r1 =await add(1,2)
    # print(r)
    # print(r1)

    c = [add(1,2),add(1,2),add(1,2),add(1,2)]
    r = await asyncio.gather(*c)

    end = time.perf_counter()

    print(f"{end-start:.2}")




asyncio.run(main())




