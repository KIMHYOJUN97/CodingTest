#LV2
#완전탐색
#brown+yellow = answer[0]*answer[1]
#2*answer[0]+2*(answer[1]-2) = sum

def solution(brown, yellow):
    answer = []
    sum = brown + yellow
    
    for i in range(1,sum+1):
        if sum % i == 0:
            answer.append(i)
    
    for i in answer:
        for j in answer:
            if i >= j and i*j == sum and (2*i+2*(j-2)) ==brown:
                return [i,j]
