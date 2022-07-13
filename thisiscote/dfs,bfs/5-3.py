#음료수 얼려 먹기

#내가 푼 식
def dfs(x,y):
    if graph[x][y] == 0:
        graph[x][y] =1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if(nx >=0 and nx < n and ny >=0 and ny <m and graph[nx][ny] ==0):
                dfs(nx,ny)
                # return True =>하나만 있는 경우에는 fail이 날 수 있음.
        return True
    else:
        return False

dx = [1,-1,0,0]
dy = [0,0,1,-1]

n,m = map(int,input().split())
graph =[]
for i in range(n):
    graph.append(list(map(int,input())))

answer = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            answer += 1

print(answer)

#책 내용
def dfs2(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False



# visited = [[False] * n for i in range(m) ]
# graph = [[]*n for i in range(m)]

# print(graph)
# print(visited)
