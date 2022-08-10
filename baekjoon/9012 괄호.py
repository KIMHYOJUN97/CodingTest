n = int(input())
answer = []
for i in range(n):
    stack = []
    question = list(input())
    check = 0
    for i in range(len(question)):
        if question[i]=='(':
            stack.append('(')
        else:
            if stack:
                stack.pop()
            else:
                answer.append("NO")
                check = 1
                break
    if check == 1:
        continue
    if stack:
        answer.append("NO")
    else:
        answer.append("YES")
for i in range(len(answer)):
    print(answer[i])