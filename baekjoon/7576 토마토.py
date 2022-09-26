#dfs bfs
from collections import deque
import sys
input = sys.stdin.readline
#전날과 상태가 같으면서 0이 존재하면 -1 출력
#날짜도 고려해줘야함
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int,input().rstrip().split())
graph = []
for _ in range(m):
    graph.append(list(map(int,input().rstrip().split())))
start = []
def first():
    for i,g in enumerate(graph):
        for idx,_ in enumerate(g):
            if _ == 1:
                start.append([i,idx,1])

def bfs(start):
    dq = deque()
    cnt = 0
    for s in start:
        dq.append(s)
    while dq:
        node = dq.popleft()
        for i in range(4):
            nx = node[0] + dx[i]
            ny = node[1] + dy[i]
            if nx>=0 and ny >=0 and nx <m and ny <n and graph[nx][ny] ==0:
                graph[nx][ny] = 1
                dq.append([nx,ny,node[2]+1])
        cnt = node[2]
    for g in graph:
        for _ in g:
            if _ == 0:
                print(-1)
                return
    print(cnt-1)

first()
bfs(start)

