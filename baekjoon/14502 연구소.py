import sys
from itertools import combinations
from collections import deque
import copy
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]
wall = 3
n,m = map(int,input().rstrip().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input().rstrip().split())))
#조합과 bfs?
start = []
for i in range(n):
    for j in range(m):
        if graph[i][j]==2:
            start.append([i,j])
def bfs():
    dq = deque()
    for s in start:
        dq.append(s)
    while dq:
        now = dq.popleft()
        for i in range(4):
            ny = now[0] + dy[i]
            nx = now[1] + dx[i]
            if nx >=0 and ny >= 0 and nx < m and ny < n and dummy_graph[ny][nx]==0:
                dummy_graph[ny][nx]=2
                dq.append([ny,nx])

def counting():
    cnt = 0
    for i in range(len(dummy_graph)):
        for j in range(len(dummy_graph[0])):
            if(dummy_graph[i][j]==0):
                cnt+=1
    return cnt

zero_list = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            zero_list.append([i,j])
answer = []
combi = combinations(zero_list,3)
for com in combi:
    dummy_graph = copy.deepcopy(graph)
    for c in com:
        dummy_graph[c[0]][c[1]]=1
    bfs()
    answer.append(counting())
print(max(answer))