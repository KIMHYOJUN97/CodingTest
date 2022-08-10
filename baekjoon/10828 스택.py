n = int(input())
stack = []
answer = []
for i in range(n):
    input_list = list(input().split())
    if input_list[0] == "push":
        stack.append(int(input_list[1]))
    elif input_list[0] == "top":
        if stack:
            answer.append(stack[-1])
        else:
            answer.append(-1)
    elif input_list[0] == "size":
        answer.append(len(stack))
    elif input_list[0] == "empty":
        if len(stack)==0:
            answer.append(1)
        else:
            answer.append(0)
    else:
        if stack:
            answer.append(stack.pop())
        else:
            answer.append(-1)

for i in range(len(answer)):
    print(answer[i])