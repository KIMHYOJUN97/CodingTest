#dfs bfs
from collections import deque
import sys
input = sys.stdin.readline
#점화식을 쓸까 3차원 배열로 함수를 만들어줄까
#점화식 => +m으로 처리
#선을 넘을 때 그 위의것까지 영향가지 않게
#3차원이 가독성 좋아보이긴 함.

dy = [0,0,-1,1,0,0]

n,m,h = map(int,input().rstrip().split())
dx = [-1,1,0,0,-1*m,m]
graph = []
for _ in range(m*h):
    graph.append(list(map(int,input().rstrip().split())))

start = []
def first(start):
    for i,g in enumerate(graph):
        for idx,_ in enumerate(g):
            if _ == 1:
                start.append([i,idx,0])

def bfs():
    dq = deque()
    day = 0
    for s in start:
        dq.append(s)
    while dq:
        node = dq.popleft()
        for i in range(6):
            nx = node[0] + dx[i]
            ny = node[1] + dy[i]
            if nx >=0 and ny >=0 and nx <m*h and ny <n and graph[nx][ny]==0:
                if node[0] % m == 0:
                    if nx == node[0]-1 and ny == node[1]:
                        continue
                if node[0]%m ==m-1:
                    if nx == node[0]+1 and ny == node[1]:
                        continue
                graph[nx][ny]=1
                dq.append([nx,ny,node[2]+1])
        day = node[2]

    for g in graph:
        for _ in g:
            if _ == 0:
                print(-1)
                return
    print(day)
first(start)
bfs()