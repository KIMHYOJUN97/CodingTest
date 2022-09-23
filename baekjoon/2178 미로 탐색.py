#dfs/bfs
import sys
from collections import deque
input = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(start):
    dq = deque()
    dq.append([start[0],start[1]])
    while dq:
        node = dq.popleft()
        for i in range(4):
            nx = node[1]+dx[i]
            ny = node[0]+dy[i]
            if nx >=0 and ny >=0 and nx<m and ny <n and graph[ny][nx]==1:
                graph[ny][nx] = graph[node[0]][node[1]]+1
                dq.append([ny,nx])

n,m = map(int,input().split())
graph =[]
#ValueError: invalid literal for int() with base 10: '\n'
for i in range(n):
    graph.append(list(map(int,input().rstrip())))
bfs([0,0])
print(graph[n-1][m-1])