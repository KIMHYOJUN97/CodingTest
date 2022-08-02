#graph
#LV3
#모든 노드와 연결된 노드 하나 찾고
#그 노드에게 진 노드 찾기?
#완전탐색 느낌으로 풀어야하나
from collections import defaultdict
from collections import deque

def solution(n, results):
    answer = 0
    win_graph = defaultdict(set)    # 이긴 애들
    lose_graph = defaultdict(set)   # 진 애들
    
    for winner,loser in results:        # 결과에서 이기고 진 애들 그래프화
        win_graph[loser].add(winner)
        lose_graph[winner].add(loser)

    for i in range(1,n+1):         
        for winner in win_graph[i]:                    # i한테 진 애들은 i를 이긴 애들한테도 진 것
            lose_graph[winner].update(lose_graph[i])
        for loser in lose_graph[i]:                     # i한테 이긴 애들은 i한테 진 애들한테도 이긴 것
            win_graph[loser].update(win_graph[i])
    
    for i in range(1,n+1):
        if len(win_graph[i]) + len(lose_graph[i]) == n-1:   # i한테 이기고 진 애들 합쳐서 n-1이면 순위가 결정된 것
            answer += 1

    return answer

def solution(n, results):
    answer = 0

    win = [[] for _ in range(n+1)]
    loser = [[] for _ in range(n+1)]

    for result in results:
        win[result[0]].append(result[1])
        loser[result[1]].append(result[0])
    
    for i in range(1,n+1):
        visited = [False for _ in range(n+1)]
        visited[0] = visited[i] = True
        for nodes in [win,loser]:
            q = deque([i])
            while q:
                idx = q.popleft()
                for node in nodes[idx]:
                    if not visited[node]:
                        visited[node] = True
                        q.append(node)
        if False not in visited:
            answer += 1
    return answer

n =5
result =[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n,result))