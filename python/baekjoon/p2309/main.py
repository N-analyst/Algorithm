# 2309번: 일곱 난쟁이
import sys
from itertools import combinations

inputs = [int(sys.stdin.readline()) for _ in range(9)]


for case in combinations(inputs, 7):
    if sum(case) == 100:
        for i in sorted(case):
            print(i)
        break