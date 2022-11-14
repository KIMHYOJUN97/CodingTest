n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
s = []

def dfs():
    if len(s) == m:
        print(*s)
        return
    
    for i in range(n):
        s.append(arr[i])
        dfs()
        s.pop()

dfs()