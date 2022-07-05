#상하좌우

N = int(input())
str_list = input().split()
n,m = 1,1

for i in range(len(str_list)):
    if(str_list[i] == 'L'):
        if(n > 1):
            n -= 1
            continue
        else:
            continue
    elif(str_list[i] == 'R'):
        if(n < N):
            n += 1
            continue
        else:
            continue
    elif(str_list[i] == 'U'):
        if(m > 1):
            m -= 1
            continue
        else:
            continue
    else:
        if(m < N):
            m += 1
            continue
        else:
            continue

print(m,n)

