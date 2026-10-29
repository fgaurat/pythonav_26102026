import requests
from bs4 import BeautifulSoup
import os
from pathlib import Path
import time
import threading
import concurrent.futures



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
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        executor.map(download_and_save,[url]*len(all_a),all_a,[download_dir]*len(all_a))



    # download_and_save("https://logs.eolem.com","apache_logs_01.log","./downloads")    
    # download_and_save("https://logs.eolem.com","apache_logs_02.log","./downloads")    
    # download_and_save("https://logs.eolem.com","apache_logs_03.log","./downloads")    
    # download_and_save("https://logs.eolem.com","apache_logs_04.log","./downloads")    
    
    end = time.perf_counter()
    print(f"{end-start:.3}s")

if __name__ == "__main__":
    main() # 0.61
