T = int(input())
for t in range(1,T+1):
    n = int(input())
    flag = 0 #alice win
    while(True):
        n/=2
        flag+=1
        if(int(n)!=n or n<1):
            break
    if(flag%2==0):
        print("#{} {}".format(t,"Alice"))
    else:
        print("#{} {}".format(t,"Bob"))

# 100 -> 50 50 alice
# 50 50 25 25 25 25 bob
# 25 12.5 12.5 12.5 12.5 