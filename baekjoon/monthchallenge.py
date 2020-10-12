# 1번
# def solution(n):
#     answer = 0
#     reverse=[]
#     while True :
#         if n<3:
#             reverse.append(n)
#             break
#         reverse.append(n%3)
#         n=n//3
#
#     digit=len(reverse)-1
#
#     for num in reverse:
#         answer+=num*(3**digit)
#         digit-=1
#
#     return answer
#
# print(solution(125))


# 2번
# import numpy as np
#
# def solution(arr):
#     answer = [0,0]
#     S=len(arr)
#     np_arr=np.array(arr)
#     piece=[np_arr]
#     while True:
#         next_piece=[]
#         for P in piece:
#             if np.sum(P) == S*S:
#                 answer[1]+=1
#             elif np.sum(P) == 0:
#                 answer[0]+=1
#             else:
#                 next_piece.append(P[:S//2,:S//2])
#                 next_piece.append(P[S//2:,:S//2])
#                 next_piece.append(P[:S//2,S//2:])
#                 next_piece.append(P[S//2:,S//2:])
#         S=S//2
#         piece=next_piece
#         if S==0:break
#     return answer
#
# print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
# print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))

################ Back_end ######################


# 1번


# 2번
# def solution(p,n):
#     answer = ""
#     AM=0
#     #PM은 기본 12시을 더해야하므로
#     PM=12*60*60
#     time=0
#
#     # 입력 시간 나누기
#     unit=p[0:2]
#     hour,minute,second=map(int,p[3:].split(':'))
#
#     if unit == "PM":
#         if hour!=12:
#             time += PM
#     if unit =="AM" and hour==12:
#         time-=hour*3600
#     time+=(hour*3600)+(minute*60)+second
#
#     # N초 후
#     time+=n
#
#     # 24시간 단위로 변환
#     h=time//3600
#     h=h%24
#     time%=3600
#
#     m=time//60
#     s=time%60
#
#     return '{0:02d}:{1:02d}:{2:02d}'.format(h,m,s)
#
# print(solution("PM 12:59:59",60))
# print(solution("AM 12:49:59",60))
# print(solution("PM 01:00:00", 10))

# 3번
def solution(n, groups):
    answer = 0
    print(sorted(groups,key=lambda x:(x[1],-(x[1]-x[0]))))

    return answer

solution(10,[[1, 5],[2, 7],[4, 8],[3, 6]])


# 4번
# import collections
# def solution(votes, k):
#     answer = ''
#     rank=list(collections.Counter(votes).items())
#     rank=sorted(rank,key=lambda x:(-x[1],x[0]))
#
#     sum_k=0
#
#     for i in range(k):
#         sum_k+=rank[i][1]
#
#     revers_sum=0
#     for i in range(len(rank)-1,-1,-1):
#         revers_sum+=rank[i][1]
#         if revers_sum>=sum_k:
#             return rank[i+1][0]
#
#
# print(solution(["AVANT", "PRIDO", "SONATE", "RAIN", "MONSTER", "GRAND", "SONATE", "AVANT", "SONATE", "RAIN", "MONSTER", "GRAND", "SONATE", "SOULFUL", "AVANT", "SANTA"], 2))
# print(solution(["AAD", "AAA", "AAC", "AAB"],4))