from collections import deque

n,k = map(int,(input().split()))
dq = deque()
answer = []
for i in range(1,n+1):
    dq.append(i)
while dq:
    for i in range(k-1):
        dq.append(dq.popleft())
    answer.append(dq.popleft())
print("<",end="")
for i in range(n):
    print(answer[i],end="")
    if i <n-1:
        print(", ",end="")
print(">")