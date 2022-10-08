import sys
input = sys.stdin.readline
student = [0]*31
for i in range(28):
    student[int(input().rstrip())]=1
for i in range(1,31):
    if student[i]==0:
        print(i)
