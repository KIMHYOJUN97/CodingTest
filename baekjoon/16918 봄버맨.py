# dfs bfs
import sys
input = sys.stdin.readline
#O
r,c,n = map(int,input().rstrip().split())
graph = []
for i in range(r):
    graph.append(list(input()))
