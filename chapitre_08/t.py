

import requests
import truststore
from bs4 import BeautifulSoup
import os
from pathlib import Path
import time
import asyncio
import httpx


async def download(queue_download: asyncio.Queue, queue_save: asyncio.Queue):
    while True:
        url, log_file, download_dir, client = await queue_download.get()
        url_file = f"{url}/{log_file}"
        r = await client.get(url_file)

        params = log_file, download_dir, r.text
        queue_save.put_nowait(params)

        queue_download.task_done()


async def save(queue_save):
    while True:
        log_file, download_dir, content = await queue_save.get()
        dest = download_dir / log_file
        with open(dest, "w") as f:
            f.write(content)

        queue_save.task_done()




async def main():

    start = time.perf_counter()

    queue_download = asyncio.Queue()
    queue_save = asyncio.Queue()

    nb_download_workers = 10
    nb_save_workers = 5

    tasks = []
    for i in range (nb_download_workers):
        t = asyncio.create_task(download(queue_download, queue_save))
        tasks.append(t)

    for i in range (nb_save_workers):
        t = asyncio.create_task(save(queue_save))
        tasks.append(t)



    url = 'https://logs.eolem.com/'
    # truststore.inject_into_ssl()            #permet de ne plus avoir à mettre un verify=False dans requests.get

    download_dir = Path("./download")
    download_dir.mkdir(exist_ok=True)



    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')   #https://beautiful-soup-4.readthedocs.io/en/latest/
    all_a = [a['href'] for a in soup.find_all('a') if a['href'].endswith('.log')]


    async with httpx.AsyncClient() as client:
        for a in all_a:
            params = url, a, download_dir, client
            queue_download.put_nowait(params)

        await queue_download.join()
        await queue_save.join()


    [t.cancel() for t in tasks]

    end = time.perf_counter()
    print(f"{end-start:.2}")

if __name__ == "__main__":
    asyncio.run(main())
