import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]
graph = []
n,l,r = map(int,input().rstrip().split())
visited = [[0]*n for i in range(n)]
for i in range(n):
    graph.append(list(map(int,input().rstrip().split())))

sum = 0
open_door = 0
dq = deque()
dq.append([0,0,0])#인구이동이 일어나는 기간 마지막 노드에 넣어주기.
sum += graph[0][0]
visited[0][0] = 1
flag = 0
#고려해야 할 점 => 인구가 막히면 다시 돌아가야 함.
while dq:
    now = dq.popleft()
    person = graph[now[0]][now[1]]
    for i in range(4):
        ny = now[0] + dx[i]
        nx = now[1] + dy[i]
        if nx >=0 and ny >=0 and nx < n and ny < n and visited[ny][nx] == 0 and l<=abs(person-graph[ny][nx])<=r:
            dq.append([ny,nx])
            sum += graph[ny][nx]
            visited[ny][nx] = 1
            flag = 1#인구 이동이 일어난다는 뜻

cnt = 0
for visit in visited:
    for v in visit:
        if v == 1:
            cnt += 1
if flag ==1:
    open_door += 1
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 1:
                graph[i][j] = int(sum/cnt)
print(graph)
print(open_door)