from pprint import pprint
import timeit
from perf import chrono,bench


@chrono
def init_loop():
    r = []
    for i in range(100):
        r.append(i)

@bench()
def init_map():
    r = list(map(lambda i:i,range(100)))

def init_comp():
    r = [i for i in range(100)]

def main():
    # t1 = timeit.timeit(init_loop)
    # print(t1)
    # t2 = timeit.timeit(init_map)
    # print(t2)
    # t3 = timeit.timeit(init_comp)
    # print(t3)
    init_loop()
    init_map()

if __name__=='__main__':
    main()
