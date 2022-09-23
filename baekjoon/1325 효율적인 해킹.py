# #메모리 초과

# m,n = map(int,input().split())
# graph =[[] for _ in range(m+1)]
# for i in range(n):
#     a,b = map(int,input().split())
#     graph[a].append(b)
# #트리 형태에서 연결의 중심인 노드에서 가장 말단인 노드를 찾는다
# #visited의 수가 가장 많은것
# visited = [[0]*(m+1) for _ in range(m+1)]
# idx = 0
# for g in graph:
#     for node in g:
#         visited[idx][node] = 1
#         visited[node][idx] = 1
#     idx += 1
# max_count = 0
# max_idx = 0
# for idx2,v in enumerate(visited):
#     cnt = 0
#     for _ in v:
#         if _ == 1:
#             cnt +=1
#     if cnt > max_count:
#         max_idx = idx2
#         max_count = cnt
# for i in graph[max_idx]:
#     print(i,end= ' ')
# import sys
# input = sys.stdin.readline
# from collections import deque
# from collections import defaultdict

# def bfs(start):
#     cnt = 1
#     visited =[0 for _ in range(n+1)]
#     visited[start] = 1
#     dq = deque()
#     while dq:
#         node = dq.popleft()
#         for v in graph[node]:
#             if not visited[v]:
#                 dq.append(v)
#                 visited[v] = 1
#                 cnt += 1
#     return cnt

# n,m = map(int,input().split())
# #deafultdict로 dictionary의 기본 형태를 list로 해주는 것이 좋다
# graph = defaultdict(list)
# for i in range(m):
#     a,b = map(int,input().split())
#     graph[b].append(a)
# print(graph)
# results = []
# max_cnt = 0
# for i in range(1,n+1):
#     cnt = bfs(i)
#     if cnt > max_cnt:
#         max_cnt = cnt
#     results.append([i,cnt])

# for i,cnt in results:
#     if cnt == max_cnt:
#         print(i,end = ' ')


#말단노드부터 시작하는게 핵심.
import sys
import collections

def bfs(start):
    cnt = 1
    visited = [0 for _ in range(n+1)]
    visited[start] = 1
    queue = collections.deque([start])
    while queue:
        u = queue.popleft()
        for v in g[u]:
            if not visited[v]:
                queue.append(v)
                visited[v] = 1
                cnt += 1
    return cnt

n, m = map(int, sys.stdin.readline().split())
g = collections.defaultdict(list)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    g[b].append(a)

results = []
max_cnt = 0
for i in range(1, n+1):
    cnt = bfs(i)
    if cnt > max_cnt:
        max_cnt = cnt
    results.append([i, cnt])

for i, cnt in results:
    if cnt == max_cnt:
        print(i, end = ' ')
