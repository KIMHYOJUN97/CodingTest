import sys
input = sys.stdin.readline
def command1(i,x):
    light[i-1] = x

def command2(l,r):
    for i in range(l-1,r):
        if light[i]==0:
            light[i] = 1
        else:
            light[i] = 0

def command3(l,r):
    for i in range(l-1,r):
        if light[i]==1:
            light[i] = 0

def command4(l,r):
    for i in range(l-1,r):
        if light[i] ==0:
            light[i] = 1

n,m = map(int,input().rstrip().split())
light = list(map(int,input().rstrip().split()))
for i in range(m):
    a,b,c = map(int,input().rstrip().split())
    if (a==1):
        command1(b,c)
    elif (a==2):
        command2(b,c)
    elif (a==3):
        command3(b,c)
    else:
        command4(b,c)
for i in range(n):
    print(light[i],end=' ')