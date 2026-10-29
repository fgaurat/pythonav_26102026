from pprint import pprint


import traceback



class DivBy12Exception(Exception):

    def __init__(self) -> None:
        super().__init__("Division par 12 !")



def div(a,b):
    if b ==12:
        raise DivBy12Exception()
    return a/b



def call_div(a,b):
    try:
        print("OPEN LOG FILE")
        r = div(a,b)
    except DivBy12Exception as e:
        raise Exception('Un message') from e
    finally:

        print("CLOSE LOG FILE")
    
    return r




def main():
    try:
        a=2
        b=12
        c=call_div(a,b)
    except DivBy12Exception as e:
        traceback.print_exc()
        
        print(e)
    except ZeroDivisionError as e:
        print(e)
    except TypeError as e:
        print(e)
    except Exception as e:
        print(e)
        print(e.__cause__)
    
    print("La suite du code ...")
    # a=2
    # b=12
    # c=call_div(a,b)
if __name__=='__main__':
    main()
