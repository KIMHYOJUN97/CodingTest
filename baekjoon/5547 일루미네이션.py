import sys
from collections import deque
input = sys.stdin.readline

# dx = [-1,1,0,0,-1,-1]
# dy = [0,0,-1,1,-1,1]
# #1.현 좌표의 양쪽 아래 건물 존재 시 3m
# #2.현 좌표의 오른쪽 위 아래 존재시 2m
# #3.현 좌표의 왼쪽 위 아래 존재 시 2m 
# w,h = map(int,input().rstrip().split())
# graph = []
# for i in range(h):
#     graph.append(list(map(int,input().rstrip().split())))

# def bfs():
#     dq = deque()
#     dq.append([0,0])
#     answer = 0
#     while dq:
#         visited = [0]* 6
#         now = dq.popleft()
#         for i in range(6):
#             nx = now[0] + dx[i]
#             ny = now[1] + dy[i]
#             if nx >=0 and ny >=0 and nx <w and ny < h and graph[ny][nx]==1:
#                 visited[i] = 1
#                 dq.append([ny,nx])
# #visited 순서
# #왼쪽, 오른쪽,오른쪽 위,오른쪽 아래, 왼쪽 위, 왼쪽 아래
# #64가지 조합중 같은 쌍을 제외하면 32가지 조합
# #전부 나눠야 하는가?
# # 1 2 3 4 5 6 


#흰색을 중심으로 크기를 재면 된다.
#앞으로 크기 재는 문제가 나오면 이런식으로 풀 것
#새로운 행과 열을 추가해주는 것이 가장 이상적이다.
W, H = map(lambda x: int(x)+2, input().split())
maps = [[0] * W for _ in range(H)]
for i in range(1,H-1):
    maps[i] = [0]+list(map(int, input().split()))+[0]
visited = [[False] * W for _ in range(H)]

def bfs(start):
    queue = deque([start])
    dy = [0,1,0,-1,1,-1]
    cnt = 0

    while queue:
        y,x = queue.popleft()
        dx = [-1,0,1,0,-1,-1] if y%2==0 else [-1,0,1,0,1,1]
        for i in range(6):
            ny, nx = y+dy[i], x+dx[i]
            if 0<=ny<H and 0<=nx<W:
                if maps[ny][nx] == 0 and not visited[ny][nx]:
                    queue.append((ny,nx))
                    visited[ny][nx] = True
                elif maps[ny][nx] == 1:
                    cnt += 1
    return cnt

visited[0][0] = True
print(bfs((0,0)))