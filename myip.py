import asyncio
from aiohttp import ClientSession
from sys import platform

urls = [
    'http://ipecho.net/plain', 
    'https://api.ipify.org', 
    'https://api.myip.com', 
    'https://ip.seeip.org',
    'http://ip-api.com/json/'
]
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9'
}

async def geo_ip(ip):
    async with session.get(f'http://ip-api.com/json/{ip}') as response:
        return await response.text()

async def get_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def get_all_urls(session, urls):
    task_urls = []
    for url in urls:
        task_urls.append(asyncio.create_task(get_url(session, url)))
    return await asyncio.gather(*task_urls)

async def main():
    async with ClientSession(headers=headers) as session:
        res = await get_all_urls(session, urls)
        print(*res, sep='\n')

if __name__ == "__main__":
    if platform.startswith('win'):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(main())
