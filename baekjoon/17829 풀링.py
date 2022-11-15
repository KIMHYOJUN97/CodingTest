n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

def dfs(x,y,N):
    if N ==2:
        lst = [graph[y][x],graph[y+1][x],graph[y][x+1],graph[y+1][x+1]]
        lst.sort()
        return lst[-2]

    first = dfs(x,y,N//2) 
    second = dfs(x,y+N//2,N//2)
    third = dfs(x+N//2,y,N//2)
    forth = dfs(x+N//2,y+N//2,N//2)
    lst = [first,second,third,forth]
    lst.sort()
    return lst[-2]

print(dfs(0,0,n))