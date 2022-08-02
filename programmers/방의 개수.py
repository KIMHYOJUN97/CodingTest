#graph
#LV 5
#해당 노드를 재방문 했을 때
#간선이 새롭게 추가된 경우
#모래시계 모양 함정
from collections import deque
from collections import defaultdict

def solution(arrows):
    answer = 0
    move = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
    now = (0,0)

    visited = defaultdict(int)
    visited_dir = defaultdict(int)

    q = deque([now])
    for i in arrows:
        for _ in range(2):
            next = (now[0]+move[i][0],now+move[i][1])
            q.append(next)

            now = next
    now = q.popleft()
    visited[now] = 1

    while q:
        next = q.popleft()
        if visited[next] ==1:
            if visited_dir[(now,next)] == 0:
                answer += 1
        else:
            visited[next] = 1
        
        visited_dir[(now,next)] = 1
        visited_dir[(next,now)] = 1
        now = next

    return answer

arrows = [6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]
print(solution(arrows))