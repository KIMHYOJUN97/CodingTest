n = int(input())
answer = []
num = []
stack = []
cnt = 1
for i in range(n):
    num.append(int(input()))
while num:
    if num[0] > cnt:
        for i in range(cnt,num[0]+1):
            stack.append(i)
            answer.append('+')
        cnt = num.pop(0)
    else:
        num.pop(0)
        stack.pop()
        answer.append('-')
    