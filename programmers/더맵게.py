import heapq

def solution(scoville, K):
    answer = 0
    heap_scovile = []
    for i in range(len(scoville)):
        heapq.heappush(heap_scovile,scoville[i])
    while True:
        answer += 1
        sum_scovile = heap_scovile[0]+heap_scovile[1]*2
        if sum_scovile>=K:
            return answer
        else:
            heapq.heappop(heap_scovile)
            heapq.heappop(heap_scovile)
            heapq.heappush(heap_scovile,sum_scovile)

    return answer

print(solution([1, 2, 3, 9, 10, 12],7))