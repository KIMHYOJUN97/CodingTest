
T = int(input())
for t in range(1,T+1):
    n = int(input())
    weeks = map(int,input().split())
    weeks = list(weeks)
    answer = 0
    i = 0
    start = 0
    while(n !=0):
        if(weeks[i]==0):
            i+=1
            if(start == 1):
                answer+=1
        else:
            start = 1
            n-=1
            answer+=1
            i+=1
        if(i>6):
            i -= 7
    print("#{} {}".format(t,answer))