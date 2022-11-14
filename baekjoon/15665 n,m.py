n,m = map(int,input().split())
arr = list(map(int,input().split()))
s = []
arr.sort()

def dfs():
    if len(s) == m:
        print(*s)
        return
    
    pre_num = 0
    for i in range(n):
        if pre_num != arr[i]:
            s.append(arr[i])
            pre_num = arr[i]
            dfs()
            s.pop()

dfs()