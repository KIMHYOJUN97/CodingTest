T = int(input())

for t in range(1,T+1):
    memory = input().rstrip()
    native = [0]*len(memory)
    cnt = 0
    flag = 0
    for i in range(len(memory)):
        if memory==''.join(map(str,native)):
            break
        if memory[i]=='1':
            flag = 1
            for j in range(i,len(native)):
                native[j]=1
            cnt+=1
        if flag==1 and memory[i]=='0':
            for j in range(i,len(native)):
                native[j]=0
            cnt+=1
    print("#{} {}".format(t,cnt))