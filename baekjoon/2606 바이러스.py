# n = int(input())
# m = int(input())
# visited = [0] * n
# visited[0] = 1
# graph = [[0] * n] * n
# for i in range(n):
#     graph[i][i] = 1
# for _ in range(m):
#     c1,c2 = map(int,input().split())
#     graph[c1-1][c2-1] = graph[c2-1][c1-1] = 1
#     # graph[c2-1][c1-1] = 1
# def bfs(start):
#     visited[start] = 1
#     q = []
#     q.append(start)
#     while q:
#         node = q.pop(0)
#         for i in range(n):
#             if graph[i][node] == 1 and visited[i]==0:#visited[i]를 넣어주는 까닭은 이미 계산된 연산을 제거하기 위함?
#                 visited[i]=1
#                 q.append(i)

# bfs(0)
# print(sum(visited)-1)

from collections import deque

n = int(input())
m = int(input())
graph = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1

visited = [0]*(n+1)

def bfs(v):
    visited[v] = 1
    queue = deque()
    queue.append(v)
    while queue:
        node = queue.popleft()
        for i in range(n+1):
            if graph[i][node] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = 1
bfs(1)

print(sum(visited)-1)

n = int(input())
m = int(input())
graph = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1

visited = [0]*(n+1)

def dfs(v):
    visited[v] = 1
    for i in range(n+1):
        if graph[i][v] == 1 and visited[i] == 0:
            dfs(i)
dfs(1)

print(sum(visited)-1)