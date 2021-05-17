import asyncio
import time
import requests
import aiohttp
from functools import partial

# 1. 동기적 함수를 동기 방식으로 동작시키는 경우

def sync_sleep(text=None):
    print(f'{text} started')
    time.sleep(1)
    print(f'{text} ended')



def sync_main():
    start = time.time()
    for i in range(10):
        sync_sleep(i)
    print(f'\n Taken time : {time.time() - start}')

sync_main()




# -----------------------------------------------------------------------------------------------------------------




# 2. 비동적 함수를 비동기 방식으로 동작시키는 경우

async def async_sleep(text):
    print(f'{text} started')
    await asyncio.sleep(1)
    print(f'{text} ended')


async def async_main():
    start = time.time()
    tasks = []
    for i in range(10):
        task = asyncio.ensure_future(async_sleep(i))
        tasks.append(task)
    await asyncio.gather(*tasks)
    print(f'\nTaken time : {time.time() - start}')

# asyncio.run(async_main())




# ----------------------------------------------------------------------------------------------------------------




# 3. 동기적 함수를 비동기 방식으로 동작시키는 경우

async def sync_to_async_main():
    start = time.time()
    tasks = []
    loop = asyncio.get_event_loop()
    for i in range(10):
        sleep = partial(sync_sleep, text=i)
        task = loop.run_in_executor(None, sleep)
        tasks.append(task)
    await asyncio.gather(*tasks)
    print(f'\nTaken time : {time.time() - start}')

# asyncio.run(sync_to_async_main())




# ----------------------------------------------------------------------------------------------------------------



#  ****************** !!! 실전 !!! ******************

url_list = ['http://www.google.com','http://www.google.com','http://www.google.com','http://www.google.com',
            'http://www.google.com','http://www.google.com','http://www.google.com','http://www.google.com',
            'http://www.google.com','http://www.google.com','http://www.google.com','http://www.google.com',
            'http://www.google.com','http://www.google.com','http://www.google.com','http://www.google.com',
            'http://www.google.com','http://www.google.com','http://www.google.com','http://www.google.com',
            'http://www.google.com','http://www.google.com','http://www.google.com','http://www.google.com',
            'http://www.google.com','http://www.google.com','http://www.google.com','http://www.google.com',
            'http://www.google.com','http://www.google.com','http://www.google.com','http://www.google.com',
            'http://www.google.com','http://www.google.com','http://www.google.com','http://www.google.com',
            'http://www.google.com','http://www.google.com','http://www.google.com','http://www.google.com']




# 4. 동기 함수(request.get) 동기 방식으로 동작시키는 경우

def sync_get(url):
    print(requests.get(url))

def sync_request(url_list):
    start = time.time()
    for url in url_list:
        sync_get(url)
    print(f'\nTaken time : {time.time() - start}')

# sync_request(url_list)




# ----------------------------------------------------------------------------------------------------------------




# 5. 동기 함수(request.get) 동기 방식으로 동작시키는 경우

async def sync_to_async_request(url_list):
    start = time.time()
    tasks = []
    loop = asyncio.get_event_loop()
    for url in url_list:
        task = loop.run_in_executor(None, sync_get, url)
        tasks.append(task)
    await asyncio.gather(*tasks)
    print(f'\nTaken time : {time.time() - start}')

# asyncio.run(sync_to_async_request(url_list))




# ----------------------------------------------------------------------------------------------------------------




# 6. 비동기 함수(aiohttp.ClientSession.get)를 비동기 방식으로 동작시키는 경우

async def async_get(url):
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        print(response.status)


async def async_request(url_list):
    start = time.time()
    tasks = []
    for url in url_list:
        task = asyncio.ensure_future(async_get(url))
        tasks.append(task)
    await asyncio.gather(*tasks)
    print(f'\nTaken time : {time.time() - start}')


# asyncio.run(async_request(url_list))

