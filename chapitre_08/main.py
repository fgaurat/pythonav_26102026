import requests
from bs4 import BeautifulSoup
import os
from pathlib import Path
import time

def main():
    start = time.perf_counter()
    url = "https://logs.eolem.com"

    # os.makedirs('download',exist_ok=True)
    
    download_dir = Path("download")
    download_dir.mkdir(exist_ok=True)


    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    all_a =  [a['href'] for a in soup.find_all('a') if a['href'].endswith(".log")]
    # for a in all_a:
    #     if a['href'].endswith(".log"):
    #         print(a['href'])

    for a in all_a:
        url_file=f"{url}/{a}"
        r = requests.get(url_file)
        dest = download_dir / a
        with open(dest,'w') as f:
            f.write(r.text)

    end = time.perf_counter()
    print(f"{end-start:.3}s")

if __name__ == "__main__":
    main() # 2.04s
