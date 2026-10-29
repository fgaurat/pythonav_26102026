from pprint import pprint
import requests
from bs4 import BeautifulSoup

from celery import Celery,signature,group,chain

def main():
    app = Celery('tasks', 
             broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/1'
             )

    result = app.send_task("celery_tasks.add",args=[2,3])
    print(result.get())

    url = "https://logs.eolem.com/"
    response = requests.get(url,verify=False)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_a = [url+a['href'] for a in soup.find_all('a') if a['href'].endswith('.log')]

    # # Download
    # download_tasks = [signature("celery_tasks.download",args=[url]) for url in all_a]
    # download_group = group(download_tasks)
    # result_download = download_group()

    # # Save
    # save_tasks = [signature("celery_tasks.save",args=[to_save]) for to_save in result_download.get()]
    # save_group = group(save_tasks)
    # result = save_group()


    for url in all_a:
        the_chain = chain(
            signature("celery_tasks.download",args=[url]),
            signature("celery_tasks.save")
        )
        the_chain()



if __name__=='__main__':
    main()
