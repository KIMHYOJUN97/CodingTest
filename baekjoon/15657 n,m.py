n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
s = []

def dfs(start):
    if len(s) == m:
        print(*s)
        return
    
    for i in range(start,n):
        s.append(arr[i])
        dfs(i)
        s.pop()

dfs(0)