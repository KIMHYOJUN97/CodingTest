T = int(input())
import math

for t in range(1,T+1):
    n,d = map(int,input().split())
    #1 2 3 . . .  n
    d = d*2 + 1
    answer = math.ceil(n/d)
    #1 2 3 4 5 6 
    #1 2 3 4 5 6 7 
    #1 2 3 4 5 6 7 8
    #1 2 3 4 5 6 7 8 9
    print("#{} {}".format(t,answer))