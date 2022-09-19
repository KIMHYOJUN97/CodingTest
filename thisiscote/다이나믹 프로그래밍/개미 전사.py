import sys
input = sys.stdin.readline

n = int(input())
question = list(map(int,input().split()))
d = [0] * 100
d[0] = question[0]
d[1] = max(question[0],question[1])
for i in range(2,n):
    d[i] = max(d[i-1],d[i-2]+question[i])

print(d[n-1])