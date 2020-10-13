# s="54321"
# num=int("321")
# return0=map(int,s)
# print(return0)
# for t in return0:
#     print(t)
# print(return0)
# print(list(return0))

# s="abcdaseeaasssdvdwez"
#
# # 모든 문자들 인덱스를 볼려면
# index_dic={str(i):[] for i in set(s)}
# for i,alpha in enumerate(s):
#     index_dic[alpha].append(i)
# print(index_dic)
#
# # 딱 두번쨰 문자의 인덱스를 볼고 싶을경우(2번째가 없는 경우는 -1반환)
# print(s.find('e',s.find('e')+1))



# 10172번(개)
# 방법1
# print("|\_/|")
# print("|q p|   /}")
# print('( 0 )"""\\')
# print('|"^"`    |')
# print('||_/=\\\\__|')

# 방법2
# print('''|\_/|
# |q p|   /}
# ( 0 )"""\\
# |"^"`    |
# ||_/=\\\\__|''')

# 2884번(알람 시계)
# H,M=map(int,input().split())
# total=H*60+M
# total=total-45
# if total<0:
#     total=24*60+total
# H=total//60
# M=total%60
# print(H,M)

# 11720번(숫자의 합)
# 방법 1
# N=input()
# num=input()
#
# sum=0
# for n in num:
#     sum+=int(n)
#
# print(sum)

# 방법 2(map에서 sum함수 이용하기)
# N=input()
# s=input()
# print(sum(map(lambda x: int(x),s)))
# print(sum(map(int,s)))

### list에서도 sum함수 이용가능 ###
# l=[1,2,3,4]
# print(sum(l),max(l),min(l))

# 10809번(알파벳 찾기)
# 방법1
# S=input()
# alpha_set=set(S)
#
# alpha_list=[-1 for _ in range(26)]
# for alpha in alpha_set:
#     index=ord(alpha)-ord('a')
#     alpha_list[index]=S.find(alpha)
# print(*alpha_list)

# 방법2
# S=input()
# print(*[S.find(chr(i+97)) for i in range(26)])

# 방법3
# alpha_list=[chr(i+97) for i in range(26)]
# alpha="abcdefghijklmnopqrstuvwxyz"
# S=input()
#
# for i in alpha:
#     print(S.find(i),end=' ')

# 1157번(단어 공부)
# 방법 1
# S=input().upper()
# alpha=[0 for _ in range(26)]
# for s in S:
#     alpha[ord(s)-ord('A')]+=1
#
# max_cnt=max(alpha)
# M=0
# for i,cnt in enumerate(alpha):
#     if max_cnt == cnt :
#         M+=1
#         max_alpha=chr(i+65)
#
# if M >=2 : print("?")
# else: print(max_alpha)

# 방법 2
# S=input().upper()
# alpha=[]
# for i in range(65,91):
#     alpha.append(S.count(chr(i)))
# print('?' if alpha.count(max(alpha)) > 1 else chr(alpha.index(max(alpha))+65))

# 1152번(단어의 개수)
# word=input().strip().split()
# print(len(word))

# 2675번(문자열 반복)
# T=int(input())
# for _ in range(T):
#     N, word=input().split()
#     print(*map(lambda x: x*int(N),word),sep="")

# 10872번(팩토리얼)
# def factorial(N):
#
#     if N<=1:
#         return 1
#
#     return N*factorial(N-1)
#
# N=int(input())
# print(factorial(N))

# 10870번(피보나치 수 5)
# def Fibonacci(N):
#     if N==0:
#         return 0
#     if N==1:
#         return 1
#
#     return Fibonacci(N-1)+Fibonacci(N-2)
#
# n=int(input())
# print(Fibonacci(n))

# 2231번(분해합)
# 방법 1
# def digit_sum(num):
#     sum=0
#     while True:
#         sum+=num%10
#         num=num//10
#         if num==0: break
#     return sum
#
# N=int(input())
# flag=False
# for i in range(1,N):
#     if N==i+digit_sum(i):
#         print(i)
#         flag=True
#         break
# if not flag: print(0)

# 방법 2
# N=int(input())
# start = max(N - 9*len(str(N)),0)
# for i in range(start,N):
#     if N== i+sum(list(map(int,str(i)))):
#         print(i)
#         exit(0)
# print(0)

# 1436번(영화감독 숌)
# 방법1(완전 생각 그대로 풀기)
# end_world=665
# N=int(input())
#
# M=0
# while True:
#     end_world+=1
#     flag=False
#     cnt=0
#     for num in str(end_world):
#         if num == '6':
#             if flag == True:
#                 cnt+=1
#                 if cnt>=2:
#                     M+=1
#                     break
#             flag=True
#         else :
#             cnt=0
#             flag=False
#     if N==M:
#         print(end_world)
#         break

# 방법2(파이썬 문법 이용)
# N=int(input())
# end_world=665
# M=0
#
# while True:
#     end_world+=1
#     if '666' in str(end_world):
#         M+=1
#
#     if M==N:
#         print(end_world)
#         break

# 2751번(수 정렬하기 2)
# import sys
#
# N=int(input())
# num_sort=[]
# for _ in range(N):
#     num=sys.stdin.readline().rstrip()
#     num_sort.append(int(num))
#
# num_sort.sort()
# for n in num_sort:
#     print(n)

# 2108번(통계학)
# from collections import Counter
# import sys
# N=int(input())
#
# values=[]
# for _ in range(N):
#     num=int(sys.stdin.readline().rstrip())
#     values.append(num)
# values.sort()
# cnt=Counter(values)
#
# print(round(sum(values)/N))
# print(values[(N-1)//2])
# most_cnt=cnt.most_common(2)
# print(most_cnt)
# if len(most_cnt) == 2:
#     if most_cnt[0][1] == most_cnt[1][1]:
#         print(most_cnt[1][0])
#     else:
#         print(most_cnt[0][0])
# else:
#     print(most_cnt[0][0])
# print(values[-1]-values[0])

# 10814번(나이순 정렬)
# 방법1(stable sort)
# from operator import itemgetter
# import sys
# N=int(input())
#
# member=[]
# for _ in range(N):
#     age, name=sys.stdin.readline().rsplit()
#     member.append((int(age),name))
#
# for age, name in sorted(member,key=itemgetter(0)):
#     print(age,name)

# 15649번(N과 M(1))
# from itertools import permutations
# N,M= map(int,input().split())
# items=[i for i in range(1,N+1)]
# for item in list(permutations(items,M)):
#     print(*item)

# 1427번(소트인사이드)
# N=input()
# str_list=list(N)
# str_list.sort(reverse=True)
# print(*str_list,sep="")

# 1316번(그룹 단어 체커)
# 방법 1
# N=int(input())
# cnt=N
# for _ in range(N):
#     S=input()
#     alpha_check=[False for _ in range(26)]
#     pre=''
#     for s in S:
#         if pre == '':
#             alpha_check[ord(s)-97]=True
#             pre=s
#
#         else :
#             if s==pre:
#                 continue
#             else:
#                 if alpha_check[ord(s)-97] == True:
#                     cnt-=1
#                     break
#                 else:
#                     pre=s
#                     alpha_check[ord(s) - 97] = True
# print(cnt)

# 방법2
# N=int(input())
# result=0
# for _ in range(N):
#     word=input()
#     if list(word)==sorted(word,key=word.find):
#         result+=1
# print(result)

# 2748번(피보나치 수2)
# N=int(input())
#
# Fibonacci=[0 for _ in range(N+1)]
# Fibonacci[0]=0
# Fibonacci[1]=1
#
# for i in range(2,N+1):
#     Fibonacci[i]=Fibonacci[i-1]+Fibonacci[i-2]
#
# print(Fibonacci[N])

# 2447번(별 찍기-10)
# def star(n):
#     star_list=['' for _ in range(n)]
#     if n==3:
#         star_list[0]+="***"
#         star_list[1]+="* *"
#         star_list[2]+="***"
#         return star_list
#
#     for r in range(3):
#         for c in range(3):
#             if r==1 and c==1:
#                 for i in range(r*(n//3),(r+1)*(n//3)):
#                     star_list[i] += ' '*(n//3)
#             else:
#                 for i,s in zip(range(r*(n//3),(r+1)*(n//3)),star(n//3)):
#                     star_list[i]+=s
#     return star_list
#
# N=int(input())
# print(*star(N),sep='\n')

# 7568번(덩치)
# N=int(input())
#
# bulk=[]
# for _ in range(N):
#     weight,height=map(int,input().split())
#     bulk.append((weight,height))
#
# # i는 비교 기준대상
# for i in range(len(bulk)):
#     k=0
#     # i와 비교할 친구들
#     for j in range(len(bulk)):
#         if i == j: continue
#         else:
#             if bulk[i][0]<bulk[j][0] and bulk[i][1]<bulk[j][1]:
#                 k+=1
#
#     print(k+1,end=" ")

# 1181번(단어 정렬)
# import sys
# N=int(input())
#
# # 중복제거를 위해서
# word=set()
# for _ in range(N):
#     word.add(sys.stdin.readline().rstrip())
#
# word=list(word)
#
# for s in sorted(word,key=lambda x:(len(x),x)):
#     print(s)

# 10828번(스택)  // 입력을 빠르게 받아야함 입력개수 1만개임...
# import sys
# def mystack(command,stack_list,num=None):
#     if command=="push":
#         stack_list.append(num)
#     elif command == 'pop':
#         return -1 if len(stack_list)==0 else stack_list.pop()
#     elif command=="size":
#         return len(stack_list)
#     elif command=="empty":
#         return 1 if len(stack_list)==0 else 0
#     elif command=='top':
#         return -1 if len(stack_list)==0 else stack_list[-1]
#
# N=int(input())
#
# stack_list=[]
# for _ in range(N):
#     cmd=sys.stdin.readline().rstrip().split()
#     if len(cmd)==1:
#         print(mystack(cmd[0],stack_list))
#     else:
#         mystack(cmd[0],stack_list,cmd[1])

# 11650번(좌표 정렬하기)
# import sys
# N=int(input())
# point=[]
# for _ in range(N):
#     p=tuple(map(int,sys.stdin.readline().rstrip().split()))
#     point.append(p)
#
# # 출력 방법1
# # for x,y in sorted(point):
# #     print(x,y)
#
# # 출력 방법2
# print("\n".join(f"{n[0]} {n[1]}" for n in sorted(point)))

# 11651번(좌표 정렬하기2)
# import sys
# N=int(input())
#
# point=[]
# for _ in range(N):
#     x,y=map(int,sys.stdin.readline().rstrip().split())
#     point.append((x,y))
#
# print("\n".join("{0} {1}".format(*n) for n in sorted(point, key= lambda x: (x[1],x[0]))))

# 2156번(포도주 시식)
# import sys
# n=int(input())
# dp=[0 for _ in range(10001)]
# wine=[0]
#
# for _ in range(n):
#     wine.append(int(sys.stdin.readline().rstrip()))
#
# dp[1]=wine[1]
# if n>=2: dp[2]=wine[1]+wine[2]
#
# for i in range(3,n+1):
#     dp[i]=max(dp[i-3]+wine[i-1]+wine[i],dp[i-1],dp[i-2]+wine[i])
#
# print(dp[n])

# 9461번(파도반 수열)
# T=int(input())
# dp=[0 for _ in range(101)]
# for _ in range(T):
#     N=int(input())
#     dp[1]=1
#     dp[2]=1
#     dp[3]=1
#     for i in range(4,N+1):
#         dp[i]=dp[i-2]+dp[i-3]
#     print(dp[N])


# 1149번(RGB거리) //미완성
# N=int(input())
#
# dp=[[0,0,0] for _ in range(N+1)]
# RGB=[0]
# for _ in range(N):
#     RGB.append(list(map(int,input().split())))
#
# dp[1][1]=RGB[1][1]
# dp[1][2]=RGB[1][2]
# dp[1][3]=RGB[1][3]
#
# print(RGB)


# 9012번(괄호)
# def VPS(vps_str):
#     vps_list=list(vps_str)
#     right=0
#     while vps_list:
#         comp=vps_list.pop()
#         if comp == '(':
#             right-=1
#         else:
#             right+=1
#
#         if right<0: return False
#
#     return True if right==0 else False
#
# N=int(input())
# for _ in range(N):
#     vps_str=input()
#     print('YES' if VPS(vps_str) else 'NO')

# 10773번(제로)
# import sys
#
# K=int(input())
# account_book=[]
# for _ in range(K):
#     N=int(sys.stdin.readline().rstrip())
#     account_book.append(N) if N !=0 else account_book.pop()
#
# print(sum(account_book))

# 18258번(큐2)
# 제공하는 패키지 이용하기(방법 1)
# from collections import deque
# import sys
#
# N=int(input())
# dq=deque()
#
# for _ in range(N):
#     cmd=sys.stdin.readline().rstrip().split()
#
#     if cmd[0]=='push':
#         dq.appendleft(cmd[1])
#     elif cmd[0]=='pop':
#         print(dq.pop() if dq else -1)
#     elif cmd[0] == 'size':
#         print(len(dq))
#     elif cmd[0] == 'empty':
#         print(0 if dq else 1)
#     elif cmd[0] == 'front':
#         print(dq[-1] if dq else -1)
#     elif cmd[0] == 'back':
#         print(dq[0] if dq else -1)

# Node를 이용한 queue만들기(방법 2)
# import sys
#
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#
#     def __str__(self):
#         return str(self.data)
#
# class Queue:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#         self.len=0
#
#     def empty(self):
#         if self.head==None:
#             return 1
#         else:
#             return 0
#
#     def push(self,data):
#         new_node = Node(data)
#         if self.head==None:
#             self.head=new_node
#             self.tail=new_node
#         else:
#             self.tail.next=new_node
#             self.tail=self.tail.next
#         self.len+=1
#
#     def pop(self):
#         if self.empty():
#             return -1
#
#         v=self.head.data
#         self.head=self.head.next
#
#         if self.head==None:
#             self.tail=None
#         self.len-=1
#         return v
#
#     def size(self):
#         return self.len
#
#     def front(self):
#         if self.head != None:
#             return self.head
#         else:
#             return -1
#     def back(self):
#         if self.tail !=None:
#             return self.tail
#         else:
#             return -1
#
# N=int(input())
# q=Queue()
# for _ in range(N):
#     cmd=sys.stdin.readline().rstrip().split()
#     if cmd[0]=='push':
#         q.push(cmd[1])
#     elif cmd[0]=='pop':
#         print(q.pop())
#     elif cmd[0] == 'size':
#         print(q.size())
#     elif cmd[0] == 'empty':
#         print(q.empty())
#     elif cmd[0] == 'front':
#         print(q.front())
#     elif cmd[0] == 'back':
#         print(q.back())

# 5430번(AC)   // (eval함수에 대한 시간 복잡도 생각할 수있는 코드)
# deque를 이용하여 풀기(방법1)
# from collections import deque
# import sys
#
# def solution(func,dq,reverse_dq):
#     # dir가 Ture이면 정방향, False이면 역방향을 의미
#     dir=True
#
#     for f in func:
#         # R함수 일때
#         if f == 'R':
#             # 방향 바꾸기
#             dir = not dir
#         # D함수 일때
#         else:
#             # 배열이 비어있는 경우 루프 탈출
#             if not dq:
#                 return 'error'
#
#             if dir==True:
#                 dq.popleft()
#                 reverse_dq.pop()
#             else:
#                 dq.pop()
#                 reverse_dq.popleft()
#
#     return list(dq) if dir else list(reverse_dq)
#
# T=int(input())
# for _ in range(T):
#     func=sys.stdin.readline().rstrip().replace('RR','')
#     arr_len=int(input())
#     arr=input()[1:-1]
#     if arr=='': arr=[]
#     else: arr=arr.split(',')
#
#     #편하지만 시간이 많이 소요됨
#     #arr=eval(arr)
#
#     # 정방향과 역방향의 deque 만들기
#     dq=deque(arr)
#     reverse_dq=deque(reversed(arr))
#
#     result=solution(func,dq,reverse_dq)
#     if type(result) == str:
#         print(result)
#     else:
#         print('['+','.join(result)+']')


# deque처럼 생각해서 인덱스를 조작하여 풀기 (방법2)
# def solution(func,arr,arr_len):
#     #방향을 나타냄 True 정방향, False 역방향
#     dir=True
#     left,right=0,0
#     func=func.replace('RR','')
#     for f in func:
#         if f=='R':
#             dir = not dir
#         else:
#             if dir:
#                 left+=1
#             else:
#                 right+=1
#
#     if left+right<=arr_len:
#         result=arr[left:arr_len-right]
#         if dir:
#             return '['+','.join(result)+']'
#         else:
#             return '['+','.join(reversed(result))+']'
#
#     else:
#         return 'error'
#
#
# T=int(input())
# for _ in range(T):
#     func=input()
#     arr_len=int(input())
#     arr = input()[1:-1].split(',')
#
#     print(solution(func,arr,arr_len))

# 1021번(회전하는 큐)
# from collections import deque
#
# N,M=map(int,input().split())
# q=deque([i for i in range(1,N+1)])
# extract=map(int,input().split())
# ans=0
# for num in extract:
#     if q[0]!=num:
#         find_idx=q.index(num)
#         size=len(q)
#
#         front=find_idx
#         back=size-find_idx
#         if front<=back:
#             for _ in range(front):
#                 q.append(q.popleft())
#                 ans+=1
#         else:
#             for _ in range(back):
#                 q.appendleft(q.pop())
#                 ans+=1
#
#     #가장 앞 번호 빼기
#     q.popleft()
# print(ans)


# 11286번(절댓값 힙)
# import heapq
# import sys
#
# heap=[]
# N=int(input())
# for _ in range(N):
#     num=int(sys.stdin.readline().rstrip())
#     if num!=0:
#         # 우선 순위를 튜플로 저장하여 넣는다.
#         heapq.heappush(heap,(abs(num),num))
#     else:
#         # 두번째 있는 원소가 본래의 값
#         print( heapq.heappop(heap)[1] if heap else 0)

# 7569번(토마토)
# //파이썬에서 클래스를 만들어서 문제를 풀면 시간이 많이 드는지 확인해보기(그냥 튜플로하면 더 빠르긴 함)
# from collections import deque
# import sys
# 
# class Point:
#     def __init__(self,k,i,j,day):
#         self.i=i
#         self.j=j
#         self.k=k
#         self.day=day
# 
# def bfs(tomato,ripe_tomato,zero_cnt,M,N,H):
#     dir=[(0,1,0),(0,-1,0),(0,0,1),(0,0,-1),(1,0,0),(-1,0,0)]
#     dq=deque()
#     for (k,i,j) in ripe_tomato:
#         dq.appendleft(Point(k,i,j,0))
# 
#     complete_day=0
#     ripe_cnt=0
# 
#     while dq:
#         P=dq.pop()
#         day=P.day
# 
#         if complete_day<day: complete_day=day
# 
#         for d in dir:
#             nk=P.k+d[0]
#             ni=P.i+d[1]
#             nj=P.j+d[2]
#             if 0<=nk<H and 0<=ni<N and 0<=nj<M:
#                 if tomato[nk][ni][nj]==0:
#                     dq.appendleft(Point(nk,ni,nj,day+1))
#                     tomato[nk][ni][nj]=1
#                     ripe_cnt+=1
# 
#     return complete_day if zero_cnt-ripe_cnt==0 else -1
# 
# 
# 
# M,N,H=map(int,input().split())
# # N행, M 열 , H 깊이
# tomato=[[[] for i in range(N)] for k in range(H)]
# 
# for k in range(H):
#     for i in range(N):
#         tomato_input=map(int,sys.stdin.readline().rstrip().split())
#         tomato[k][i].extend(tomato_input)
# 
# # 인덱스 순서는 [깊이][행][열] 순. [H][N][M]
# ripe_tomato=[]
# 
# zero_cnt=0
# for k,k_v in enumerate(tomato):
#     for i,i_v in enumerate(k_v):
#         for j,j_v in enumerate(i_v):
#             if j_v==1:
#                 ripe_tomato.append((k,i,j))
#             elif j_v==0:
#                 zero_cnt+=1
# 
# if zero_cnt==0:
#     print(0)
#     exit(0)
# 
# print(bfs(tomato,ripe_tomato,zero_cnt,M,N,H))

# 11279번(최대 힙)
# import heapq
# import sys
#
# N=int(input())
# pq=[]
#
# for _ in range(N):
#     num=int(sys.stdin.readline().rstrip())
#
#     if num==0:
#         if pq:
#             print(-heapq.heappop(pq))
#         else:
#             print(0)
#     else:
#         heapq.heappush(pq,(-num))

# 1927번(최소 힙)
# import heapq
# import sys
#
# N=int(input())
# pq=[]
#
# for _ in range(N):
#     num=int(sys.stdin.readline().rstrip())
#
#     if num==0:
#         if pq:
#             print(heapq.heappop(pq))
#         else:
#             print(0)
#     else:
#         heapq.heappush(pq,num)

# 1655번(가운데를 말해요)
# import heapq,sys
#
# N=int(input())
# left,right=[],[]
#
# for _ in range(N):
#     num=int(sys.stdin.readline().rstrip())
#
#     # 배열의 길이가 짝수이면 최대힙에서 꺼낸다.
#     if len(left)==len(right):
#         # max_heap
#         heapq.heappush(left,(-num,num))
#     else:
#         # min_heap
#         heapq.heappush(right,(num,num))
#
#
#     # 오른쪽 값이 존재하고 왼쪽 값이 오른쪽 값보다 큰경우
#     if right and left[0][1]>right[0][1]:
#         left_v=heapq.heappop(left)[1]
#         right_v=heapq.heappop(right)[1]
#         heapq.heappush(right,(left_v,left_v))
#         heapq.heappush(left,(-right_v,right_v))
#
#     print(left[0][1])

# 1260번(DFS와 BFS)
# from collections import deque
#
# N,M,V=map(int,input().split())
# node=[[] for _ in range(N+1)]
# visited=[0 for _ in range(N+1)]
#
# for _ in range(M):
#     a,b=map(int,input().split())
#     node[a].append(b)
#     node[b].append(a)
#
# for i in range(1,N+1):
#     node[i].sort()
#
#
# def dfs(i):
#     visited[i]=1
#     print(i,end=' ')
#
#     for next_node in node[i]:
#         if visited[next_node]==0:
#             dfs(next_node)
#
#
# def bfs(i):
#     visited=[0 for _ in range(N+1)]
#     q=deque()
#     q.appendleft(i)
#     visited[i]=1
#
#     while q:
#         cur=q.pop()
#         print(cur,end=' ')
#
#         for next_node in node[cur]:
#             if visited[next_node]==0:
#                 q.appendleft(next_node)
#                 visited[next_node]=1
#
# dfs(V)
# print()
# bfs(V)







