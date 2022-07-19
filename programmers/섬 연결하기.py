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
    costs.sort(key=lambda x:(x[2],x[0],x[1]))
    for cost in costs:
        count = 0
        if visited[cost[0]]==0 and visited[cost[1]]==0:
            answer += cost[2]
            visited[cost[0]]=1
            visited[cost[1]]=1
        elif visited[cost[0]]==1 and visited[cost[1]]==0:
            answer += cost[2]
            visited[cost[1]]=1
        else:
            continue
        for v in visited:
            if v == 0:
                count +=1
        if count ==0:
            print(costs)
            print(cost)
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