#LV3
#graph
from collections import deque

def solution(n, edge):
    answer = 0
    adj = [[] for _ in range(n+1)]
    visited = [0] * (n+1)

    for e in edge:
        adj[e[0]].append(e[1])
        adj[e[1]].append(e[0])

    visited[1] = 1
    q = deque([1])

    while q:
        x = q.popleft()
        for next in adj[x]:
            if not visited[next]:
                visited[next] = visited[x]+1
                q.append(next)

    count = max(visited)
    answer = visited.count(count)
    return answer

vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
n = 6
print(solution(n,vertex))