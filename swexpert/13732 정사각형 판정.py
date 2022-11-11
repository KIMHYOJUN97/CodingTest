T = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
from collections import deque
import math

def bfs(graph,y,x,n):
    cnt = 1
    dq = deque()
    dq.append([y,x])
    visited = [[0]*n for i in range(n)]
    while(dq):
        now = dq.popleft()
        visited[now[0]][now[1]] = 1
        for i in range(4):
            ny = now[0]+dy[i]
            nx = now[1]+dx[i]
            if(nx >=0 and ny>=0 and nx <n and ny <n and visited[ny][nx]==0):
                if(graph[ny][nx]=='#'):
                    dq.append([ny,nx])
                    visited[ny][nx]=1
                    cnt+=1
    
    return cnt

for t in range(1,T+1):
    n = int(input())
    graph = []
    wall_count = 0
    for i in range(n):
        graph.append(list(input()))
    
    input_data = [-1,-1]
    for i in range(n):
        for j in range(n):
            if graph[i][j]=='#':
                wall_count+=1
                input_data[0]=i
                input_data[1]=j
    if(wall_count==bfs(graph,input_data[0],input_data[1],n)):
        if(math.sqrt(wall_count)==int(math.sqrt(wall_count))):
            print("#{} {}".format(t,"yes"))
        else:
            print("#{} {}".format(t,"no"))
    else:
        print("#{} {}".format(t,"no"))
    