n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
visited = [False] * n
s = []

def dfs():
    if len(s)==m:
        print(*s)
        return
    
    pre_num = 0
    for i in range(n):
        if not visited[i] and pre_num != arr[i]:
            visited[i] = True
            s.append(arr[i])
            pre_num = arr[i]
            dfs()
            visited[i] = False
            s.pop()
    
dfs()