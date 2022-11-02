import sys
input = sys.stdin.readline

t = 1
for j in range(t):
    n = int(input())
    answer = 0
    building = list(map(int,input().split()))
    for i in range(2,n-1):
        flag = 0
        if(building[i-2]>building[i] or building[i-1]>building[i] or building[i+1]>building[i] or building[i+2]>building[i]):
            continue
        height = [building[i-2],building[i-1],building[i+1],building[i+2]]
        height.sort()
        answer += building[i]-height[-1]
    print("#{} {}".format(j+1,answer))
