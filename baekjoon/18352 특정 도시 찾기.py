from collections import deque
INF = 1e9
n,m,k,x = map(int,input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
distance[x] = 0

dq = deque([x])
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

while dq:
    now = dq.popleft()
    for node in graph[now]:
        if distance[node]>distance[now]+1:
            distance[node] = distance[now]+1
            dq.append(node) 

flag = 0
for i in range(1,n+1):
    if distance[i]==k:
        flag = 1
        print(i)
if(flag==0):
    print(-1)