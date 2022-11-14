#union - find Algorithm
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m = map(int,input().split())
parent = [0] *(n+1)
for i in range(n+1):
    parent[i] = i

def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)

    if a==b:
        return
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(m):
    a,b,c = map(int,input().split())
    if a ==0:
        union(b,c)
    elif a == 1:
        if find(b) == find(c):
            print("YES")
        else:
            print("NO")