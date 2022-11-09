T = int(input())

for t in range(T):
    alpha = list(input())
    cnt = 0
    flag = 0
    if(alpha[0]!='a'):
        print("#{} {}".format(t+1,cnt))
        continue
    else:
        cnt=1
    for i in range(len(alpha)-1):
        if(ord(alpha[i])==ord(alpha[i+1])-1):
            cnt+=1
        else:
            flag =1
            break
    
    if(flag == 0 and ord(alpha[len(alpha)-2])==ord(alpha[-1])):
        cnt+=1
    print("#{} {}".format(t+1,cnt))