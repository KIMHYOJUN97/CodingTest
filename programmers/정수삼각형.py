#DP
#LV3
#dfs와 dp의 차이 구하기
#heapq에 넣고 가장 큰거 구하기?

# import heapq

# def solution(triangle):
#     answer = 0
#     num = []
#     for t in triangle:
#         for number in t:
#             heapq.heappush(num,-number)
#     for i in range(len(triangle)):
#         answer += (-heapq.heappop(num))
#     return answer

def solution(triangle):
    for i in range(1,len(triangle)):
        for j in range(i+1):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == i:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j],triangle[i-1][j-1])
    
    return max(triangle[-1])

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))