import requests
from bs4 import BeautifulSoup
import os
from pathlib import Path
import time
import asyncio
import httpx


# region test
async def download_and_save(url,log_file,download_dir):
    url_file=f"{url}/{log_file}"
    r = requests.get(url_file)
    dest = download_dir / log_file
    with open(dest,'w') as f:
        f.write(r.text)

async def async_requests_download_and_save(url,log_file,download_dir):
    url_log_file = f"{url}/{log_file}"
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, requests.get, url_log_file)
    
    dest = download_dir / log_file
    with open(dest,'w') as f:
        f.write(response.text)

# endregion

async def httpx_download_and_save(url,log_file,download_dir,client):
    url_file=f"{url}/{log_file}"
    
    r = await client.get(url_file)
    dest = download_dir / log_file
    with open(dest,'w') as f:
        f.write(r.text)



async def main():
    start = time.perf_counter()
    url = "https://logs.eolem.com"

    download_dir = Path("download")
    download_dir.mkdir(exist_ok=True)

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_a =  [a['href'] for a in soup.find_all('a') if a['href'].endswith(".log")]

    all_coroutines = []
    async with httpx.AsyncClient() as client:
        for a in all_a:
            all_coroutines.append(httpx_download_and_save(url,a,download_dir,client))

        r = await asyncio.gather(*all_coroutines)


    end = time.perf_counter()
    print(f"{end-start:.3}s")

if __name__ == "__main__":
    asyncio.run(main())
