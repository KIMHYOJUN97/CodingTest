T = int(input())

for t in range(1,T+1):
    a,b = map(int,input().split())
    if(a>9 or b>9):
        print("#{} {}".format(t,-1))
    else:
        print("#{} {}".format(t,a*b))