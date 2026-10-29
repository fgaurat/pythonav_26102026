import truststore
truststore.inject_into_ssl()


from celery import Celery
import requests

app = Celery('tasks', 
             broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/1'
             )

@app.task
def add(x, y):
    return x + y


@app.task
def download(url):
    log_file = url.split("/")[-1]
    response = requests.get(url)
    return log_file,response.text


@app.task
def save(args):
    log_file,log_content = args
    with open(log_file,"w") as f:
        f.write(log_content)
