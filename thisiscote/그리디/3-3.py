#숫자 카드 게임
def min_value(lst):
    min = 10000
    for i in range(len(lst)):
        if(lst[i] <min):
            min = lst[i]
    
    return min

n,m = map(int,input().split())
min_list = []
for i in range(n):
    lst = list(map(int,input().split()))
    min_list.append(min_value(lst))

min_list.sort()
print(min_list[-1])