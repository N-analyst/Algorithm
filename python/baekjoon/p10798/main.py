# 10798번: 세로읽기
import sys
from itertools import zip_longest

arr = [sys.stdin.readline().rstrip() for _ in range(5)]

print_str=[]
for vertical in zip_longest(*arr, fillvalue=''):
    for char in vertical:
        print_str.append(char)

print(''.join(print_str))
