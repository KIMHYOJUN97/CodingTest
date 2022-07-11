from collections import deque

def solution(priorities,location):
    answer =0
    queue = []
    for i in range(len(priorities)):
        queue.append([priorities[i],i])

    while True:
        if max(priorities) == queue[0][0]:
            answer += 1
            if location == queue[0][1]:
                return answer
            queue.pop(0)
            priorities.remove(max(priorities))
        else:
            queue.append(queue.pop(0))
    return answer

priorities = [1, 1, 9, 1, 1, 1]
print(solution(priorities,0))

# queue = []
# for i in range(len(priorities)):
#     queue.append([priorities[i],i])
# print(queue[0][0])
# print(queue[0][1])
# print(queue.append(queue.pop(0)))
# print(queue)
# print(queue.append(queue.pop(0)))
# print(queue)
# print(queue[0][1])
# print(max(priorities))