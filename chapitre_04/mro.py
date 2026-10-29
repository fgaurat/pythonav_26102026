from pprint import pprint


class A:

    def show(self):
        print("A")

class B(A):

    def show(self):
        print("B")

class C(A):

    def show(self):
        print("C")

class D(B,C):

    def show(self):
        super(D,self).show()
        super(B,self).show()
        super(C,self).show()
        # print(super(A,self).__str__())

        print("D")



def main():
    print(D.mro())
    # [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
    # [<class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
    d = D()
    d.show()

if __name__=='__main__':
    main()
