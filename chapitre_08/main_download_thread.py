import requests
from bs4 import BeautifulSoup
import os
from pathlib import Path
import time
import threading

def download_and_save(url,log_file,download_dir):
    url_file=f"{url}/{log_file}"
    r = requests.get(url_file)
    dest = download_dir / log_file
    with open(dest,'w') as f:
        f.write(r.text)


def main():
    start = time.perf_counter()
    url = "https://logs.eolem.com"

    # os.makedirs('download',exist_ok=True)
    
    download_dir = Path("download")
    download_dir.mkdir(exist_ok=True)


    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_a =  [a['href'] for a in soup.find_all('a') if a['href'].endswith(".log")]

    all_threads = []
    for a in all_a:
        th = threading.Thread(target=download_and_save,args=(url,a,download_dir))
        th.start()
        all_threads.append(th)

    [t.join() for t in all_threads]
    
    end = time.perf_counter()
    print(f"{end-start:.3}s")

if __name__ == "__main__":
    main() # 0.61
