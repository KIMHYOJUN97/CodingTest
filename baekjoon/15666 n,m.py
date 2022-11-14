n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
s = []

def dfs(start):
    if len(s) == m:
        print(*s)
        return
    
    pre_num = 0
    for i in range(start,n):
        if pre_num != arr[i]:
            s.append(arr[i])
            pre_num = arr[i]
            dfs(i)
            s.pop()

dfs(0)