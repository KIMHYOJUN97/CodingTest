import sys
input = sys.stdin.readline

t = int(input().rstrip())
answer = []
for i in range(t):
    n = int(input().rstrip())
    num_list = list(map(int,input().rstrip().split()))
    answer.append((min(num_list),max(num_list)))
for x,y in answer:
    print(x, y)