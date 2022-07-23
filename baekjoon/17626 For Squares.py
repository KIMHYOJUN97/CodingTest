import math
def list_sum(num_list):
    sum = 0
    for num in num_list:
        sum += num*num
    return sum

n = int(input())
answer = 0
num_list = []
target = n
while True:
    n1 = int(math.sqrt(n))
    num_list.append(n1)
    if list_sum(num_list)== target:
        answer += 1
        break
    else:
        n = target
        n -= list_sum(num_list)
        answer += 1

print(answer)