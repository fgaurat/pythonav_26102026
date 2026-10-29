from pprint import pprint

def mult2(i):
    return i*2


def main():
    l = [10,20,30,40,50]

    l2 = list(map(lambda i:i*2,l))

    print(l2)

    # l2 = [20,40,60,80,100] 


    l2 = []
    for i in l:
        if i>30:
            l2.append(i*2)

    l2 = [i*2 for i in l if i >30 ]




if __name__=='__main__':
    main()
