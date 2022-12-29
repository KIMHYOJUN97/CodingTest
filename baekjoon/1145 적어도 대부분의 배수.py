from itertools import combinations

def gcd(tuple_num):
    number_range = 1
    for t in tuple_num:
        number_range = number_range*t        
    for i in range(1,number_range+1):
        if(i%tuple_num[0]==0 and i%tuple_num[1]==0 and i%tuple_num[2]==0):
            return i
    return int(1e9)

num = list(map(int,input().split()))
num_combi = combinations(num,3)
answer = []
for number in num_combi:
    answer.append(gcd(number))

answer.sort()
print(answer[0])