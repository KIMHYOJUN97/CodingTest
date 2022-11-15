n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
p_a = 0
p_b = 0
answer = []
while(True):
    if(p_b ==len(b)):
        for i in range(p_a,len(a)):
            answer.append(a[i])
        break
    elif(p_a ==len(a)):
        for i in range(p_b,len(b)):
            answer.append(b[i])
        break

    if a[p_a]>=b[p_b]:
        answer.append(b[p_b])
        p_b += 1
    else:
        answer.append(a[p_a])
        p_a+=1

print(*answer)