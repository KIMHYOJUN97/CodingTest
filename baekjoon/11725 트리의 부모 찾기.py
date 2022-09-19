#메모리 초과

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
# n = int(input())
# tree = dict()
# answer = []
# graph = [[0]*(n+1) for _ in range(n+1)]
# #1이 부모노드인 것은 그 다음의 부모노드이다.
# #그 외의것은 부모,자식 순이다.
# question = []
# for i in range(n-1):
#     a,b = map(int,input().split())
#     graph[a][b] = graph[b][a] = 1
#     #입력값 재저장
#     question.append([a,b])

# #1과 이어진 노드 탐색
# second_node = []
# for i in range(1,n+1):
#     if graph[1][i] == 1:
#         second_node.append(i)
#         tree[i] = 1
        
# for i in range(n-1):
#     if question[i][0] in second_node:
#         tree[question[i][1]] = question[i][0]
#     elif question[i][1] in second_node:
#         tree[question[i][0]] = question[i][1]
#     else:
#         tree[question[i][1]] = question[i][0]

# for i in range(2,n+1):
#     print(tree[i])
# 이 문제는 노드의 개수가 최대 100,000개 이므로 이차원 배열에서 연결상태를 표시하게 되면 
# 10만*10만 = 100억개의 칸을 사용하기 때문에 메모리 초과가 날 수 밖에 없다.

from collections import deque

N = int(input())
graph = [[] for i in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque()
queue.append(1)

ans = [0]*(N+1)

def bfs():
    while queue:
        now = queue.popleft()
        for nxt in graph[now]:
            if ans[nxt] == 0:
                ans[nxt] = now
                queue.append(nxt)

bfs()
res = ans[2:]
for x in res:
    print(x)