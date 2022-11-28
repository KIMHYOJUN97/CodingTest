#heapq는 앞 숫자를 기준으로 정렬한다. 앞 숫자가 같다면 그 다음 인덱스를 기준으로 정렬한다.

import sys
input = sys.stdin.readline
# from queue import PriorityQueue

# n = int(input())
# q = PriorityQueue()
# answer = []
# for _ in range(n):
#     x = int(input())
#     if x == 0:
#         if not q.empty():
#             answer.append(q.get()[1])
#         else:
#             answer.append(0)
#     else:
#         q.put((abs(x),x))

# for i in range(len(answer)):
#     print(answer[i])

import heapq

n = int(input())
hq = []

for _ in range(n):
    x = int(input())
    if x ==0:
        if hq:
            print(heapq.heappop(hq)[1])
        else:
            print(0)
    else:
        heapq.heappush(hq,(abs(x),x))