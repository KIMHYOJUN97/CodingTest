#LV2
#DFS/BFS
#n,m에 도착하지 못하면 return -1
#=>graph를 -1로 초기화 시키고 answer을 n,m으로
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def solution(maps):
    answer = 0
    graph = [[-1 for _ in range(len(maps[0]))] for _ in range(len(maps))]

    queue = deque()
    queue.append([0,0])

    graph[0][0] = 1

    while queue:
        y,x = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]) and maps[ny][nx] == 1:
                if graph[ny][nx] == -1:
                    graph[ny][nx] = graph[y][x]+1
                    queue.append([ny,nx])

    answer = graph[-1][-1]
    return answer

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps))