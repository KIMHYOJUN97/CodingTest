import heapq
#리스트 remove사용해서 풀기도 가능할거같은데
#heap은 자동정렬 해주는것이 편해서 사용?
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville)>=2 and scoville[0] <K:
        sum = heapq.heappop(scoville) + 2*heapq.heappop(scoville)
        heapq.heappush(scoville,sum)
        answer += 1
    
    if scoville[0] <K:
        return -1
    return answer

print(solution([1, 2, 3, 9, 10, 12],7))