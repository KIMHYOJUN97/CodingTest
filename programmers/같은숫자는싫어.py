#stack/queue

from collections import deque


def solution(arr):
    answer = []

    queue = deque(arr)
    answer.append(arr[0])
    i = 0
    while queue:
        if answer[i] == queue[0]:
            queue.popleft
        else:
            answer.append(arr[0])
            i+=1

    return answer