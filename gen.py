import os
import sys


def my_gen(n:int):
    start = 0
    while start < n:
        yield start
        start += 1



x = my_gen(1000000 )
print(f'the gen take {sys.getsizeof(x)} bytes')

lis = []

for val in x:
    lis.append(val)


print(f'the size of lis is {sys.getsizeof(lis)} bytes')
