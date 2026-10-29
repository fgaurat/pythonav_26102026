import lib as l
import lib

import le_package.une_autre_lib

from lib import hello as h

from pprint import pprint


def hello(name):
    print("Local Hello ",name)

def main():
    
    lib.hello("fred")
    
    l.hello("fred")

    le_package.une_autre_lib.hello("fred")
    hello("fred")
    h("fred")

if __name__=='__main__':
    main()
