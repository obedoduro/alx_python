#!/usr/bin/python3
from add_0 import add
#function to add a and b
def add(a, b):
    return a + b

#main function to start from
def main():
    a = 1
    b = 2
    result = add(a, b)
    print('{} + {} = {}'.format(a, b, result))

if __name__ == "__main__":
    main()
