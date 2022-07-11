import heapq
#전체 경우의수 고른 후 제일 작은거?=>시간복잡도가 너무 커진다
#도착 순서가 무조건 짧은거부터 하는게 가장 빠른 방법이다.
#도착 순서가 같은것도 있는지?

#하드 디스크가 사용중인데 다른 도착한것이 있다면 
#사용 시간이 짧은거 우선

#500000개 전체 돌것이 아니라 처리해야 할 시간을 처음에
#0으로 초기화 해준뒤 1씩 늘려가면서 접근한다.
def solution(jobs):
    answer = 0
    start,end,i = -1,0,0
    heap = []
    
    while i <len(jobs):
        for j in jobs:
            if start < j[0] <= end:
                heapq.heappush(heap,[j[1],j[0]])
        if len(heap) >0:
            present = heapq.heappop(heap)
            start = end
            end += present[0]
            answer += (end-present[1])
            i += 1
        else:
            end += 1

    return answer//len(jobs)

jobs = [[0, 3], [1, 9], [2, 6]]
# job =[1,2,3]
# heapq.heapify(jobs)

# print(jobs)