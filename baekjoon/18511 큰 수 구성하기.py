import sys
input = sys.stdin.readline

# n,k = map(int,input().split())
# num = list(map(int,input().split()))
# n_str = str(n)
# num.sort(reverse=True)
# answer = '0'
# flag = 0

# # #1번째 숫자보다 작거나 같은 숫자가 없으면 2번째 숫자에선 전부 큰 수로
# for i in range(len(n_str)):
#     if i==1:
#         if answer=='0':
#            flag=1

#     if flag==0:
#         check = 0
#         for n in num:
#             if int(n_str[i])==n:
#                 answer += str(n)
#                 check = 1
#                 break
#             elif int(n_str[i])>n:
#                 answer += str(n)
#                 flag =1
#                 check = 1
#                 break
#     else:
#         answer += str(num[0])

# print(int(answer))

#아마 back-tracking문제 같다


# n,k = map(int,input().split())
# num = list(map(int,input().split()))
# answer =''
# def dfs(n,k):
#     if len(answer)==len(n) and int(answer)<int(n):
#         return
    
#     for i in range(n):

#답은 중복순열이다
from itertools import product

n,k = map(int,input().split())
k_list = list(input().split())

i =0
check = 0
while True:
    result = list(product(k_list,repeat=len(str(n))-i))
    answer_list = []
    for res in result:
        tmp = ''
        for r in res:
            tmp += r
        answer_list.append(int(tmp))
    answer_list.sort(reverse=True)
    for answer in answer_list:
        if(answer<=n):
            print(answer)
            check=1
            break
    if check==0:
        i+=1
    else:
        break