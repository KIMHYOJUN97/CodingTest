#LV2
from itertools import permutations

def is_prime_num(n):
    if(n<2):
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False # i로 나누어 떨어지면 소수가 아니므로 False 리턴
    
    return True
def solution(numbers):
    answer = 0
    p = []
    result = []
    
    for i in range(1, len(numbers)+1):
        p.extend(permutations(numbers, i))
        result = [int(''.join(i)) for i in p]
    
    for i in set(result):
        if is_prime_num(i):
            answer+=1
            
    return answer