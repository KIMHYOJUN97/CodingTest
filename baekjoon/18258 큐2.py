from collections import deque

dq = deque()
n = int(input())
answer = []
for i in range(n):
    question = list(input().split())
    if question[0] == "push":
        dq.append(question[1])
    elif question[0] == "front":
        if dq:
            answer.append(dq[0])
        else:
            answer.append(-1)
    elif question[0] == "size":
        answer.append(len(dq))
    elif question[0] == "back":
        if dq:
            answer.append(dq[-1])
        else:
            answer.append(-1)
    elif question[0] == "empty":
        if dq:
            answer.append(0)
        else:
            answer.append(1)
    else:
        if dq:
            answer.append(dq.popleft())
        else:
            answer.append(-1)
for i in range(len(answer)):
    print(answer[i])