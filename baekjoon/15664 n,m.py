n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
s = []
visited = [False] * n

def dfs(start):
    if len(s) == m:
        print(*s)
        return
    
    pre_num = 0
    for i in range(start,n):
        if not visited[i] and pre_num!=arr[i]:
            s.append(arr[i])
            pre_num = arr[i]
            visited[i]=True
            dfs(i)
            visited[i]=False
            s.pop()

dfs(0)