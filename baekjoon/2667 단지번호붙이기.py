#bfs
import sys
from collections import deque
input = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(start):
    if graph[start[0]][start[1]]==0:
        return
    dq = deque()
    dq.append([start[0],start[1]])
    cnt = 1
    graph[start[0]][start[1]] = 0
    while dq:
        node = dq.popleft()
        for i in range(4):
            nx = node[0] + dx[i]
            ny = node[1] + dy[i]
            if nx >=0 and ny >= 0 and nx <n and ny <n and graph[nx][ny]==1:
                graph[nx][ny] = 0
                cnt += 1
                dq.append([nx,ny])
    answer.append(cnt)

n = int(input().rstrip())
answer = []
graph = []
for i in range(n):
    graph.append(list(map(int,input().rstrip())))
for i in range(n):
    for j in range(n):
        bfs([i,j])

answer.sort()
print(len(answer))
for i in range(len(answer)):
    print(answer[i])