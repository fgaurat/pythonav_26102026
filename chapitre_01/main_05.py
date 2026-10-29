from pprint import pprint

def hello(**kwargs):
    print(kwargs['theName'],kwargs['theFirstName'],)


def add(*l)->int:
    """ 
        fonction add
        a: int
        b: int 

    """
    print(l)
    r = sum(l)
    return r


# def f(a,b,/): # pos only
def f(*,a,b): # kw only
                            # def f(p1,p2,/,a,b,*,kw2,kw2): # def
    print(a,b)
    

def main():

    

    # hello("Gaurat","fred")
    # hello(firstName="Fred",name="Gaurat")

    l = [10,20,30,40,50]
    r = add(*l) 
    # r = add(10,20,30,40,50) 

    print(r) # 150

    a,b,*c =0,1,2,3,4,5,6
    print(a,b,c)

    print(*l) # print(10,20,30,40,50)

    hello(theName="GAURAT",theFirstName="Fred")

if __name__=='__main__':
    main()
