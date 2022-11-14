n,m = map(int,input().split())

s = []
def dfs(start):
    if len(s) == m:
        print(" ".join(map(str,s)))
        return
    
    for i in range(1,n+1):
        if not s:
            s.append(i)
        else:
            if s[len(s)-1]<=i:
                s.append(i)
            else:
                continue
        dfs(i)
        s.pop()


def dfs2(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(start, n+1):
        s.append(i)
        dfs2(i)
        s.pop()
    
dfs2(1)
dfs(1)