T = 10
from collections import deque

for t in range(1,T+1):
    n = int(input())
    number = deque(list(map(int,input().split())))
    
    k = 1
    while(True):
        number.append(number.popleft()-k)
        if(number[-1]<=0):
            number[-1]=0
            break
        k+=1
        if(k>5):
            k -=5
    print("#{}".format(n),end=' ')
    for i in range(len(number)):
        print(number[i],end=' ')
    print()
