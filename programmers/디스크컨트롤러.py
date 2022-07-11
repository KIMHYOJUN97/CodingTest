import heapq
#전체 경우의수 고른 후 제일 작은거?=>시간복잡도가 너무 커진다

def solution(jobs):
    answer = 0
    heap = []
    for i in range(len(jobs)):
        heapq.heappush(heap,jobs[i])
    return answer

jobs = [[0, 3], [1, 9], [2, 6]]
job =[1,2,3]
heapq.heapify(jobs)

print(jobs)