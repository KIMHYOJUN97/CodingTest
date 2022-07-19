#Greedy
#섬 연결하기
#LV3

#graph 문제?
#각 섬들의 최단거리에 있는 섬들부터 잇기 시작
#visited가 전부 1로 되었다면 종료
#간선을 사용해야 함
def solution(n, costs):
    answer = 0
    visited = [0] * n
    vertex = []
    costs.sort(key=lambda x:(x[2],x[0],x[1]))
    for cost in costs:
        if visited[cost[0]]==0 and visited[cost[1]]==0:
            answer += cost[2]
            visited[cost[0]]=1
            visited[cost[1]]=1
            vertex.append([cost[0],cost[1]])
        elif visited[cost[0]]==1 and visited[cost[1]]==0:
            answer += cost[2]
            visited[cost[1]]=1
            vertex.append([cost[0],cost[1]])
        else:
            continue
    
    return answer

def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2]) # 비용기준으로 오름차순 정렬
    connect = set([costs[0][0]]) # 연결을 확인하는 집합
    
    # Kruskal 알고리즘으로 최소 비용 구하기
    while len(connect) != n:
        for cost in costs:
            if cost[0] in connect and cost[1] in connect:
                continue
            if cost[0] in connect or cost[1] in connect:
                connect.update([cost[0], cost[1]])
                answer += cost[2]
                break
                
    return answer

print(solution(5,[[0, 1, 1], [0, 4, 5], [2, 4, 1], [2, 3, 1], [3, 4, 1]]))

# 5 [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4], [2, 4, 6], [4, 0, 7]] 15
# 5 [[0, 1, 1], [3, 4, 1], [1, 2, 2], [2, 3, 4]] 8
# 4 [[0, 1, 5], [1, 2, 3], [2, 3, 3], [1, 3, 2], [0, 3, 4]] 9
# 5 [[0, 1, 1], [3, 1, 1], [0, 2, 2], [0, 3, 2], [0, 4, 100]] 104
# 6 [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]] 11
# 5 [[0, 1, 1], [2, 3, 1], [3, 4, 2], [1, 2, 2], [0, 4, 100]] 6
# 5 [[0, 1, 1], [0, 4, 5], [2, 4, 1], [2, 3, 1], [3, 4, 1]] 8
# 5 [[0, 1, 1], [0, 2, 2], [0, 3, 3], [0, 4, 4], [1, 3, 1]] 8