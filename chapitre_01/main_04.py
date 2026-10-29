from pprint import pprint

from collections import deque


def main():
    l = [10,20,30,40,50]
    l.append(60)
    last_value = l.pop()
    print(l)

    l.insert(0,-10)
    print(l)
    first_value = l.pop(0)
    print(l)

    d = deque(l)

    d.appendleft(-10)
    print(d)

    first_value = d.popleft()
    print(first_value)

if __name__=='__main__':
    main()
