# from copy import deepcopy
# import sys
# from collections import deque
# input = sys.stdin.readline

# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
# graph = []
# n,l,r = map(int,input().rstrip().split())
# visited = [[0]*n for i in range(n)]
# for i in range(n):
#     graph.append(list(map(int,input().rstrip().split())))
# dummy = deepcopy(graph)
# sum = 0
# dq = deque()
# dq.append([0,0,0])#인구이동이 일어나는 기간 마지막 노드에 넣어주기.
# sum += graph[0][0]
# visited[0][0] = 1
# def check_visit():
#     for i in range(n):
#         for j in range(n):
#             if visited[i][j]==0:
#                 return [i,j]
    
#     return False
# def moving():
#     cnt = 0
#     for visit in visited:
#         for v in visit:
#             if v == 1:
#                 cnt += 1
#     for i in range(n):
#         for j in range(n):
#             if visited[i][j] == 1:
#                 graph[i][j] = int(sum/cnt)
# flag = 0
# day = 1
# while dq:
#     now = dq.popleft()
#     person = graph[now[0]][now[1]]
#     visited[now[0]][now[1]]=1
#     for i in range(4):
#         ny = now[0] + dx[i]
#         nx = now[1] + dy[i]
#         if nx >=0 and ny >=0 and nx < n and ny < n and visited[ny][nx] == 0 and l<=abs(person-graph[ny][nx])<=r:
#             dq.append([ny,nx,now[2]])
#             sum += graph[ny][nx]
#             visited[ny][nx] = 1
#             flag = 1#인구 이동이 일어난다는 뜻
#     #고려해야 할 점 => 인구가 막히면 다시 돌아가야 함.
#     if(not dq and flag == 0):
#         for i,visit in enumerate(visited):
#             for idx,v in enumerate(visit):
#                 if v==0:
#                     dq.append([i,idx,now[2]])
#                     break
#     if(not dq and flag ==1):
#         check_vis = check_visit()
#         moving()
#         if(check_vis):
#             dq.append([check_vis[0],check_vis[1],now[2]+1])
#     day = max(day,now[2])
# c = 0
# for i in range(n):
#     for j in range(n):
#         if(graph[i][j]!=dummy[i][j]):
#             c =1
#             break
# if c == 0:
#     print(0)
# else:
#     print(day)

#방문 횟수를 전부 돌았다면 sum값으로 graph를 초기화 해준 후 
#다시 리빌딩된 graph로 탐색하여 주기.

import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]
graph = []
n,l,r = map(int,input().rstrip().split())
for i in range(n):
    graph.append(list(map(int,input().rstrip().split())))

def bfs(start):
    dq = deque()
    dq.append(start)
    tmp = []
    tmp.append((start[0],start[1]))
    while dq:
        now = dq.popleft()
        for i in range(4):
            ny = now[0] + dy[i]
            nx = now[1] + dx[i]
            if nx>=0 and ny >=0 and nx <n and ny <n and visited[ny][nx]==0 and l<=(abs(graph[now[0]][now[1]]-graph[nx][ny])<=r):
                visited[ny][nx] = 1
                dq.append([ny,nx])
                tmp.append((ny,nx))
    
    return tmp

result = 0
while 1:
    flag = 0
    visited = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j]==0:
                visited[i][j]=1
                temp = bfs([i,j])
                if len(temp)>1:
                    flag = 1
                    sum = 0
                    for y,x in temp:
                        sum+=graph[y][x]
                    for y,x in temp:
                        graph[y][x]=sum
    if flag ==0:
        break
    result += 1

print(result)