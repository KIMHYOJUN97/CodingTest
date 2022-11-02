n = int(input())
answer = []
for i in range(n):
    t = int(input())
    question = list(map(int,input().split()))
    max_num = question[-1]
    benefit = 0
    for j in range(t-1,-1,-1):
        if(question[j]>max_num):
            max_num = question[j]
        else:
            benefit += max_num-question[j]
    answer.append(benefit)

for i in range(len(answer)):
    print("#{} {}".format(i+1,answer[i]))