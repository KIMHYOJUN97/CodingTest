import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
cow = [-1]*(11)
for i in range(n):
    a,b = map(int,input().split())
    prev = cow[a]
    cow[a] = b
    now = cow[a]
    if(prev != -1 and prev != now):
        cnt+=1
    else:
        continue
print(cnt)