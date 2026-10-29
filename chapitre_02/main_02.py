from pprint import pprint

from functools import wraps


# def do_log(func):

#     @wraps(func)
#     def wrapper(*args,**kwargs):
#         print("START", args,kwargs)
#         r = func(*args,**kwargs)
#         print("END",r)
#         return r


#     return wrapper

def do_log(log_file):
    def decorator(func):

        @wraps(func)
        def wrapper(*args,**kwargs):
            print(f"START write to {log_file}", args,kwargs)
            r = func(*args,**kwargs)
            print("END",r)
            return r

        return wrapper
    return decorator


def do_secu(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print("START Secu",args,kwargs)
        r = func(*args,**kwargs)
        print("END Secu")
        return r
    
    return wrapper





@do_log('lefichier.log')
@do_secu
def say_hello(name:str)->str:
    """
    Dire bonjour
    """

    return f"Hello {name}"


def main():
    
    r = say_hello('Fred')

    print("dans le main",r)
    print(say_hello.__name__)
    print(say_hello.__doc__)

if __name__=='__main__':
    main()
