# from itertools import permutations

# n,m = map(int,input().split())
# num = []
# for i in range(1,n+1):
#     num.append(i)
# lst = list(permutations(num,m))
# for l in lst:
#     for number in l:
#         print(number,end=' ')
#     print()

n,m = list(map(int,input().split()))
s = []
def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()
dfs()