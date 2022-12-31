import sys
INF = int(1e9)
input = sys.stdin.readline

def floyd_washal():
    N,K = map(int,input().split())
    graph = [[INF]*(N+1) for _ in range(N+1)]

    for i in range(1,N+1):
        for j in range(1,N+1):
            if i==j:
                graph[i][j]=0


    for _ in range(K):
        a,b = map(int,input().split())
        graph[a][b]=1
        graph[b][a]=1

    for k in range(1,N+1):
        for i in range(1,N+1):
            for j in range(1,N+1):
                graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])
    for i in range(1,N+1):
        for j in range(1,N+1):
            if graph[i][j]>6:
                print("Big World!")
                return
    return print("Small World!")
    
floyd_washal()
# from collections import deque

# def bfs(node):
#     q = deque()
#     q.append(node)
#     check[node] = 0
#     while q:
#         node = q.popleft()
#         for n in graph[node]:
#             if check[n] == -1:
#                 q.append(n)
#                 check[n] = check[node]+1

# N, K = map(int, input().split())
# graph = [[] for _ in range(N+1)]
# check = [-1]*(N+1)
# for _ in range(K):
#     u, v = map(int, input().split())
#     graph[u].append(v)
#     graph[v].append(u)
# ok = 1
# for i in range(1, N+1):
#     check = [-1]*(N+1)
#     bfs(i)
#     if (max(check) > 6) or (-1 in check[1:]):
#         ok = 0
#         break
# print("Small World!" if ok else "Big World!")