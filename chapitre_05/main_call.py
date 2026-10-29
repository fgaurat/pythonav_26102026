from pprint import pprint
from typing import Any

class Test:


    def __init__(self):
        self.name="Fred"


    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print("__call__",self.name)
    

def main():
    t = Test()
    t()



if __name__=='__main__':
    main()
