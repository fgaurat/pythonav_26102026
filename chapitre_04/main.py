from pprint import pprint
from carre import Carre
from cercle import Cercle
from i_surface import ISurface

def show_surface(o:ISurface):
    print(o.surface)

def main():
    c = Carre(3)
    print(c.cote) # 3
    print(c.surface)
    c.cote = 12
    print(c.surface)
    print(50*"-")
    ce = Cercle(3)
    print(ce.surface)
    show_surface(c)
    show_surface(ce)
    



if __name__=='__main__':
    main()
