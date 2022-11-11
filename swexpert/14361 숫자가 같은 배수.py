T = int(input())
from itertools import permutations

for t in range(1,T+1):
    n = int(input())
    num_list = list(str(n))
    lst = map(int,num_list)
    per_list = list(permutations(num_list,len(num_list)))
    real_list = []
    for per in per_list:
        tmp = ''
        for i in range(len(per)):
            tmp+= per[i]
        real_list.append(int(tmp))
    
    flag = 0
    for real in real_list:
        if(real>n and real % n ==0):
            flag = 1
            break
    if flag==1:
        print("#{} {}".format(t,"possible"))
    else:
        print("#{} {}".format(t,"impossible"))
