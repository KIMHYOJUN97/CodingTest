#상하좌우

N = int(input())
str_list = input().split()  #list()사용 하지 않아도 됨.
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


#책 풀이
n = int(input())
x,y = 1,1
plans = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x +dy[i]
            ny = y +dy[i]
    if nx <1 or ny <1 or nx > n or ny >n:
        continue

    x,y = nx, ny

print(x,y)