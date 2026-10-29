from pprint import pprint
import copy
def main():
    l = [10,20,30,40,50]
    print(len(l))

    print(l[len(l)-1])
    print(l[-1])

    print(l[2:4]) # [2:4[
    print(l[2:])
    print(l[:2])
    print(l[:])

    a = l[2:4]
    print(a)
    a[0]=1000
    print(l)
    print(a)
    l2 = l
    l2 = l[:] # copy
    l2 = l.copy()
    l2 = copy.copy(l)
    l2[0] = 1000
    print(l)
    print(l2)
    
    print(50*'-')
    l = [
        [10,20,30],
        [40,50,60],
        [70,80,90]
    ]
    l2 = copy.deepcopy(l)
    l2[1][1] = 1000
    print(l)
    print(l2)

if __name__=='__main__':
    main()
