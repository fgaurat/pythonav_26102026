from pprint import pprint

def make_incrementor(i):

    def f(j):
        return i+j

    return f


def main():
    do_inc = make_incrementor(10)

    r = do_inc(2)

    print(r) # 12

if __name__=='__main__':
    main()
