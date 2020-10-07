# 2606번(바이러스)
# import sys
# from collections import deque
#
# N=int(input())
# M=int(input())
#
# computer=[0 for _ in range(N+1)]
# Network=[[] for _ in range(N+1)]
#
# for _ in range(M):
#     a,b=map(int,sys.stdin.readline().rstrip().split())
#     Network[a].append(b)
#     Network[b].append(a)
#
# start=1
# deq=deque()
# deq.appendleft(start)
# computer[start]=1
#
# while len(deq) != 0:
#     current=deq.pop()
#
#     for num in Network[current]:
#         if computer[num] != 1:
#             deq.appendleft(num)
#             computer[num]=1
#
# # 1번 컴퓨터는 제외
# print(sum(computer)-1)

