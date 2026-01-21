# 10798번: 세로읽기
import sys

n = [sys.stdin.readline().rstrip() for i in range(5)]

print_str = []
for i in range(15):
    for j in range(5):
        if i < len(n[j]):
            print_str.append(n[j][i])

print(''.join(print_str))