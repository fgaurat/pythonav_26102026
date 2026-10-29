



from pprint import pprint
import sys


def main():
    a = 1
    print(hex(id(a)))
    
    b = 2
    print(hex(id(b)))

    print(sys.getrefcount(53463546743623))
    e = 53463546743623
    print(sys.getrefcount(53463546743623))


    s = "toto"
    # s[0]="J"


    b =2
    s = "toto"+str(b)
    s = "toto"*b
    
    print(50*"-")

if __name__=='__main__':
    main()
