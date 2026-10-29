from pprint import pprint


from rectangle import Rectangle
from data_rectangle import DataRectangle

def main():
    r = Rectangle(3,2)
    r1 = Rectangle(3,2)
    r2 = Rectangle.build_from_str('3;4')

    print("cpt class",Rectangle.cpt())
    print("cpt obj",r.cpt())

    # print(r.__dict__)
    # longueur = r.get_longueur()
    # r.set_longueur(12)
    # surface = r.get_surface()

    print(r.longueur)
    print(r.surface)

    s  = str(r)

    print(s)

    # r.longueur = 12


    if r==r1:
        print("ok")
    else:
        print("ko")

    d1 = DataRectangle(3,4)
    print(d1)
if __name__=='__main__':
    main()
