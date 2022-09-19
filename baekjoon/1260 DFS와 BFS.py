from collections import deque

n,m,v = map(int,input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1
visited = [0] *(n+1)

def dfs(start):
    print(start,end = ' ')
    visited[start] = 1
    for i in range(1,n+1):
        if(visited[i]== 0 and graph[start][i] == 1):
            dfs(i)

def bfs(start):
    visited[start] = 1
    dq = deque()
    dq.append(start)
    while dq:
        node = dq.popleft()
        print(node,end = ' ')
        for i in range(1,n+1):
            if graph[node][i]==1 and visited[i]==0:
                visited[i] = 1
                dq.append(i)
dfs(v)
print()
visited = [0] *(n+1)
bfs(v)