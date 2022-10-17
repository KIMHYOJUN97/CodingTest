import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]
r,c,t = map(int,input().split())
graph = []
#처음 미세먼지가 있는 곳도 미세먼지를 받는다
#graph를 두개 만드는 게 효율적.

#공기청정기가 시작 또는 끝 지점에 머물러 있을 경우
for i in range(r):
    graph.append(list(map(int,input().split())))

def up_cycle(graph,location):
    for i in range(location[0]-1,0,-1):
        graph[i][0] = graph[i-1][0]
    for i in range(c-1):
        graph[0][i] = graph[0][i+1]
    for i in range(location[0]):
        graph[i][c-1]=graph[i+1][c-1]
    for i in range(c-1,1,-1):
        graph[location[0]][i]=graph[location[0]][i-1]
    graph[location[0]][1] = 0

def down_cycle(graph,location):
    graph[location[1]+1][0] = 0
    for i in range(location[1]+1,r-1):
        graph[i][0] = graph[i+1][0]
    for i in range(0,c-1):
        graph[r-1][i] = graph[r-1][i+1]
    for i in range(r-1,location[1],-1):
        graph[i][c-1]=graph[i-1][c-1]
    for i in range(c-1,1,-1):
        graph[location[1]][i] = graph[location[1]][i-1]
    graph[location[1]][1]=0

def dust(graph):
    dust_list = []
    dq = deque()
    for i in range(r):
        for j in range(c):
            if(graph[i][j]>=5):
                dust_list.append([i,j])
    
    for d in dust_list:
        direct_cnt = 0
        for i in range(4):
            nx = d[1] + dx[i]
            ny = d[0] + dy[i]
            if(nx >=0 and nx <c and ny >=0 and ny<r and graph[ny][nx]!=-1):
                dq.append([ny,nx,(graph[d[0]][d[1]])//5])
                direct_cnt += 1
        graph[d[0]][d[1]]-=(graph[d[0]][d[1]]//5)*direct_cnt
    while dq:
        now = dq.pop()
        graph[now[0]][now[1]] += now[2]

location_list = []
for i in range(r):
    if(graph[i][0]==-1):
        location_list.append(i)

for i in range(t):
    dust(graph)
    up_cycle(graph,location_list)
    down_cycle(graph,location_list)
    
answer =0
for i in range(r):
    for j in range(c):
        answer += graph[i][j]
print(answer+2)
