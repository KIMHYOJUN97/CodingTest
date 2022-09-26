#최소 신장 트리
import sys
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b
n,m = map(int,input().split())
parent = [0] * (n+1)
edges = []
for i in range(n+1):
    parent[i] = i
for i in range(m):
    a,b,c = map(int,input().split())
    edges.append((a,b,c))

edges.sort()
last = 0
result = 0
for edge in edges:
    cost,a,b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost
        last = cost
        # last = max(last,cost)#일 필요가 없는게 정렬로 인해서 cost는 정렬됐다.

print(result-last)