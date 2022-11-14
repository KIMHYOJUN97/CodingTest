from itertools import permutations

n,m = map(int,input().split())
num = []
for i in range(1,n+1):
    num.append(i)
lst = list(permutations(num,m))
for l in lst:
    for number in l:
        print(number,end=' ')
    print()