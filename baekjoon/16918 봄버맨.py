# dfs bfs
#bfs
#시간과 현재 그래프 상태를 queue에 넣어놓고
#하나씩 popleft 하면서 가져오기
import sys
input = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]
#O
r,c,n = map(int,input().rstrip().split())
graph = []
for i in range(r):
    graph.append(list(input().rstrip()))

#1초때는 그대로 =>위치 기억시키는 함수 만들기
location = []
def first(location):
    for i,g in enumerate(graph):
        for idx,_ in enumerate(g):
            if _ == 'O':
                location.append([i,idx])

#2초후
def bomb():
    for idx,g in enumerate(graph):
        for i,_ in enumerate(g):
            if _ == '.':
                graph[idx][i] = 'O'

#3초때 터지기
def exclusion():
    for l in location:
        graph[l[0]][l[1]] = '.'
        for i in range(4):
            nx = l[0] + dx[i]
            ny = l[1] + dy[i]
            if nx >=0 and ny >= 0 and nx < r and ny < c:
                graph[nx][ny] = '.'
first(location)
for i in range(2,n+1):
    if i % 2 == 0:
        bomb()
    else:
        exclusion()
        location = []
        first(location)
print()
for g in graph:
    for _ in g:
        print(_,end='')
    print()