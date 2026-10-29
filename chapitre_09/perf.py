from functools import wraps
import time
import timeit

def chrono(func):

    @wraps(func)
    def wrapper(*args,**kwargs):
        start = time.perf_counter()
        r = func(*args,**kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} : {end-start:.2}s")
        return r
    return wrapper




def bench(number=1000):

    def decorator(func):

        @wraps(func)
        def wrapper(*args,**kwargs):

            t = timeit.repeat(lambda: func(*args,**kwargs),number = number)
            print(f"{func.__name__} : {sum(t)/number:.2} s")
            r = func(*args,**kwargs)
            
            return r
            

        return wrapper
    return decorator