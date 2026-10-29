from pprint import pprint
import time
import threading
import multiprocessing


def count():
    x = 0
    for _ in range(100_000_000):
        x+=1


def run_seq():
    start = time.perf_counter()
    count()
    count()
    end = time.perf_counter()
    print(f"{end-start:.2}")



def run_thread():
    start = time.perf_counter()
    th1 = threading.Thread(target=count)
    th2 = threading.Thread(target=count)
    th1.start()
    th2.start()
    th1.join()
    th2.join()
    end = time.perf_counter()
    print(f"{end-start:.3}s")


def run_process():
    start = time.perf_counter()
    p1 = multiprocessing.Process(target=count)
    p2 = multiprocessing.Process(target=count)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time.perf_counter()
    print(f"{end-start:.3}s")



def main():
    print("run_seq")
    # run_seq() # 2.8
    
    print("run_thread")
    run_thread()

    print("run_process")
    run_process()
if __name__=='__main__':
    main()
