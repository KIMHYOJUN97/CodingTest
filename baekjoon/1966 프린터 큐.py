#단순 for문은 자주 사용하는 인덱스 표현인 i 쓰지않기

n = int(input())
answer = []
for _ in range(n):
    N,M = list(map(int,input().split()))
    priority = list(map(int,input().split()))
    cnt = 0
    max_list = sorted(priority,reverse=True)
    for i in range(len(priority)):
        priority[i] = [priority[i],i]
    # priority[M][1] = [priority[M],-1]
    priority[M][1] =-1
    while priority:
        if priority[0][0]==max_list[0]:
            cnt += 1
            if priority[0][1] == -1:
                answer.append(cnt)
                break
            priority.pop(0)
            max_list.pop(0)
        else:
            priority.append(priority.pop(0))

for i in range(len(answer)):
    print(answer[i])