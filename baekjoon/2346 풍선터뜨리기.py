from collections import deque

n = int(input())
sequence = list(map(int,input().split()))
dq = deque()
for i in range(n):
    dq.append([sequence[i],i+1])
answer = [1]
check = 0
while dq:
    if n == len(answer):
        break
    if check == 0:
        balloon = dq.popleft()[0]
    if balloon >= 0:
        for _ in range(balloon-1):
            dq.append(dq.popleft())
        answer.append(dq[0][1])
        check = 0
    else:
        balloon = balloon*-1
        dq.reverse()
        for _ in range(balloon-1):
            dq.append(dq.popleft())
        answer.append(dq[0][1])
        balloon = dq.popleft()[0]
        dq.reverse()
        check = 1

for i in range(len(answer)):
    print(answer[i],end = ' ')
