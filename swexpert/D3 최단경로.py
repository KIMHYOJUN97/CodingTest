T = int(input())

def dfs(start,depth):
    global ans
    ans = max(ans,depth)

    for next in graph[start]:
        if visited[next]:
            continue
        visited[next] = True
        dfs(next,depth+1)
        visited[next] = False

for t in range(1,T+1):
    n,m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    ans = 0
    
    for i in range(m):
        x,y = map(int,input().split())
        graph[x].append(y)
        graph[y].append(x)
    visited = [False]*(n+1)

    for i in range(1,n+1):
        visited[i] = True
        dfs(i,1)
        visited[i] = False
    print("#{} {}".format(t,ans))