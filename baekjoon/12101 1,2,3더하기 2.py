from sys import stdin
input = stdin.readline
import sys

cnt = 0
def dfs(S,sum_list):
    global cnt
    if S>n:
        return
    if S==n:
        cnt+=1
        if(cnt==k):
            for i in range(len(sum_list)-1):
                print(str(sum_list[i]) + "+",end='')
            print(sum_list[-1])
            exit()
        
    for i in [1,2,3]:
        sum_list.append(i)
        dfs(S+i,sum_list)
        sum_list.pop()

n,k = map(int,input().split())
dfs(0,[])
print(-1)