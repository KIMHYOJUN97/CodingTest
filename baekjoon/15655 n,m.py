n,m = map(int,input().split())
arr = list(map(int,input().split()))
s = []
arr.sort()

def dfs(start):
    if len(s)==m:
        print(*s)
        return
    
    for i in range(start,n):
        if arr[i] not in s:
            s.append(arr[i])
            dfs(i+1)
            s.pop()

dfs(0)