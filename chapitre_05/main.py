from pprint import pprint


from rectangle_singleton import Rectangle as RectangleSingleton
from rectangle import Rectangle as RectangleDeco
from rectangle import Rectangle as RectangleMeta

def main():
    # r1 = RectangleSingleton(1,2)
    # r2 = RectangleSingleton(1,2)
    # print(hex(id(r1)))
    # print(hex(id(r2)))

    # r3 = RectangleDeco(1,2)
    # print(hex(id(r3)))
    # print(r3)
    # r4 = RectangleDeco(5,6)
    # print(hex(id(r4)))
    # print(r4)
    
    r3 = RectangleMeta(1,2)
    print(hex(id(r3)))
    print(r3)
    r4 = RectangleMeta(5,6)
    print(hex(id(r4)))
    print(r4)


    del r3
    print(r4)

    print(50*"-")


    a = 2
    print(type(type(a)))

if __name__=='__main__':
    main()
