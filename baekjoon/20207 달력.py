import sys
input = sys.stdin.readline

##최적화된 수학문제 풀이##

# n = int(input())
# calendar = [0]*366
# for _ in range(n):
#     s,e = map(int,input().split())
#     for i in range(s,e+1):
#         calendar[i]+=1

# row = 0
# col = 0
# answer = 0
# for i in range(1,366):
#     if calendar[i]!=0:
#         col +=1
#         row = max(row,calendar[i])
#     else:
#         answer += row*col
#         row = 0
#         col = 0
# answer += row*col #마지막까지 0이 안나왔을 때 들어가 있는 값들을 처리해 준다.
# print(answer)
##최적화된 수학문제 풀이##

#구현

n = int(input())

calendar = [[0] * 366 for _ in range(n)]
todo = []

for _ in range(n):
    s,e = map(int,input().split())
    term = e-s+1
    todo.append(s,e,term)

todo.sort(key=lambda x:(x[0],-x[2]))

for k in range(n):
    s, e = todo[k][0],todo[k][1]

    for i in range(n):
        if 1 in calendar[i][s:e+1]:
            continue

        for j in range(s,e+1):
            calendar[i][j]=1
        break

row = 0
col = 0
ans = 0
for j in range(1,366):
    flag = False
    for i in range(n):
        if calendar[i][j]==1:
            flag = True
            row = max(row,i+1)
    if flag:
        col +=1
    else:
        ans += row*col
        row = 0
        col = 0
if flag:
    ans += row*col

print(ans)