T = int(input())

for t in range(1,T+1):
    # m초에 k개 만들 수 있다.
    n,m,k = map(int,input().split())
    arrived = list(map(int,input().split()))
    cnt = 0
    flag=0
    for i in range(max(arrived)+1):
        if i>0 and i%m==0:
            cnt+=k
        for person in arrived:
            if person==i:
                cnt-=1
                if(cnt<0):
                    flag = 1
                    break
        if flag==1:
            break
    if(flag==1):
        print("#{} {}".format(t,"Impossible"))
    else:
        print("#{} {}".format(t,"Possible"))
