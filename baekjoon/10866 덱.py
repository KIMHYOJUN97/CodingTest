from collections import deque

n = int(input())
dq = deque()
answer = []
for i in range(n):
    question = list(input().split())
    if question[0] == "push_back":
        dq.append(question[1])
    elif question[0] == "push_front":
        print(question[1])
        dq.insert(0,question[1])
    elif question[0] == "front":
        if dq:
            answer.append(dq[0])
        else:
            answer.append(-1)
    elif question[0] == "back":
        if dq:
            answer.append(dq[-1])
        else:
            answer.append(-1)
    elif question[0] == "pop_front":
        if dq:
            answer.append(dq.popleft())
        else:
            answer.append(-1)
    elif question[0] == "pop_back":
        if dq:
            answer.append(dq.pop())
        else:
            answer.append(-1)
    elif question[0] == "size":
        answer.append(len(dq))
    else:
        if dq:
            answer.append(0)
        else:
            answer.append(1)
print(dq)
for i in range(len(answer)):
    print(answer[i])